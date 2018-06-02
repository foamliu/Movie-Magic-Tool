import cv2 as cv
import re
import numpy as np

from find_obj import init_feature
from find_obj import filter_matches

FLANN_INDEX_KDTREE = 1  # bug: flann enums are missing
FLANN_INDEX_LSH = 6


def get_sec(time_str):
    time_str, millisec = time_str.split('.')
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s) + int(millisec) / 1000.0


def parse_scenedetect_result(input):
    result = []
    pattern = '(?P<code>\d+:\d+:\d+.\d+),?'
    r = re.compile(pattern)

    match = [m.groupdict() for m in r.finditer(input)]
    # print(match)

    for m in match:
        # print(m['code'])
        result.append(get_sec(m['code']))

    return result


# def generate_a_random_hex_color():
#     import random
#     r = lambda: random.randint(0, 255)
#     return ('#%02X%02X%02X' % (r(), r(), r()))

def generate_a_random_hex_color():
    import random
    r = lambda: random.randint(0, 255)
    return (r(), r(), r())


def get_key_points2(key_points1, src_pts, dst_pts):
    key_points2 = []
    for i in range(0, len(dst_pts)):
        src_pt = tuple(src_pts[i])
        dst_pt = tuple(dst_pts[i])
        list = [kp for kp in key_points1 if kp['pt'] == src_pt]
        if len(list) > 0:
            key_point = list[0]
            key_points2.append({'pt': dst_pt, 'color': key_point['color']})
        else:
            key_points2.append({'pt': dst_pt, 'color': generate_a_random_hex_color()})

    return key_points2


def extract_keypoints(path, scale_factor=1.0):
    cap = cv.VideoCapture(path)

    detector, matcher = init_feature('surf')

    raw_result = []
    first_frame = True
    frame_idx = 0
    kp1 = None
    kp2 = None
    des1 = None
    des2 = None
    key_points1 = None
    key_points2 = None

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        kp, des = detector.detectAndCompute(frame, None)

        if first_frame:
            first_frame = False
            kp1 = kp
            des1 = des
            key_points1 = [{'pt': p.pt, 'color': generate_a_random_hex_color()} for p in kp]
            raw_result.append({'frame_idx': frame_idx, 'key_points': key_points1})

        else:
            kp2 = kp
            des2 = des
            raw_matches = matcher.knnMatch(des1, des2, k=2)
            src_pts, dst_pts, kp_pairs = filter_matches(kp1, kp2, raw_matches)
            key_points2 = get_key_points2(key_points1, src_pts, dst_pts)
            raw_result.append({'frame_idx': frame_idx, 'key_points': key_points2})

            kp1 = kp2
            des1 = des2
            key_points1 = key_points2

        frame_idx += 1

        print(frame_idx)

    cap.release()

    result = []
    for f in raw_result:
        key_points = []
        raw_key_points = f['key_points']
        for kp in raw_key_points:
            key_points.append({'pt': (int(round(kp['pt'][0] * scale_factor)), int(round(kp['pt'][1] * scale_factor))),
                               'color': kp['color']})

        result.append({'frame_idx': f['frame_idx'], 'key_points': key_points})

    return result


if __name__ == '__main__':
    path = '../../web/video/Game_Of_Hunting_EP1_new.mp4'
    ret = extract_keypoints(path)

    import json

    with open('data.json', 'w') as output:
        json.dump(ret, output, sort_keys=True, indent=4)
