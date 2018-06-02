from __future__ import print_function
import sys
import zerorpc
from subprocess import Popen, PIPE
from common import parse_scenedetect_result
from common import extract_keypoints

class VirtualAdsApi(object):
    def echo(self, text):
        """echo any text"""
        return text

    def detect_shot(self, path):
        path = path.replace("file://", "")
        cmd = 'scenedetect --input {} --detector content --threshold 30'.format(path)
        print(cmd)
        args = ['scenedetect', '--input', path, '--detector', 'content', '--threshold', '30']
        process = Popen(args, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        #print(stdout)
        return parse_scenedetect_result(stdout)

    def extract_keypoints(self, path):
        return extract_keypoints(path)


def parse_port():
    port = 4242
    try:
        port = int(sys.argv[1])
    except Exception as e:
        pass
    return '{}'.format(port)

def main():
    addr = 'tcp://127.0.0.1:' + parse_port()
    s = zerorpc.Server(VirtualAdsApi())
    s.bind(addr)
    print('start running on {}'.format(addr))
    s.run()

if __name__ == '__main__':
    main()
    #path = 'file:///Users/yangliu/code/virtualads/web/video/Game_Of_Hunting_EP1_new.mp4'
    #VirtualAdsApi().detect_shot(path)
