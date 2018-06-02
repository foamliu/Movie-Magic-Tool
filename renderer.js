const zerorpc = require("zerorpc")
let client = new zerorpc.Client({timeout: 600, heartbeatInterval: 600000})

client.connect("tcp://127.0.0.1:4242")

client.invoke("echo", "server ready", (error, res) => {
  if(error || res !== 'server ready') {
    console.error(error)
  } else {
    console.log("server is ready")
  }
})

const {ipcRenderer} = require('electron')

ipcRenderer.on('file_open', (event, arg) => {
	var selectedFiles = arg;
  if (selectedFiles != null) {
    console.log(selectedFiles)
    var video = document.getElementById('video');
    video.setAttribute('src', selectedFiles[0]);
  }
})

function capture(video, scaleFactor) {
  if(scaleFactor == null){
    scaleFactor = 1;
  }
  var w = video.videoWidth * scaleFactor;
  var h = video.videoHeight * scaleFactor;
  var canvas = document.createElement('canvas');
  canvas.width  = w;
  canvas.height = h;
  var ctx = canvas.getContext('2d');
  ctx.drawImage(video, 0, 0, w, h);
  return canvas;
}

function seek(shots, index) {
  var video  = document.getElementById('video');
  console.log('onclick');
  console.log(shots);
  console.log(index);

  if (index < 0) {
    video.currentTime = 0.00;
  }
  else {
    var newtime = shots[index];
    console.log(newtime);
    video.currentTime = newtime;
  }
}

ipcRenderer.on('edit_detect_shot', (event, arg) => {
	var video = document.getElementById('video');
	var path = video.src;

  console.log('start detecting shots...')
  client.invoke("detect_shot", path, (error, res) => {
	  if(error) {
	    console.error(error)
	  } else {
      console.log(res);

      var shots = res;
      var scaleFactor = 0.10;
      var video  = document.getElementById('video');
      var output = document.getElementById('output');
      output.innerHTML = '';

      var i = 0;
      var event = setInterval(function(){
          var canvas = capture(video, scaleFactor);
          canvas.id = i;
          canvas.onclick = function(){
            var index = canvas.id;
            seek(shots, index);
          };
          output.appendChild(canvas);

          video.currentTime = shots[i];
          i++;
          if(i === shots.length) {
              clearInterval(event);
          }
      }, 200);

	  }
	})
})

ipcRenderer.on('edit_extract_keypoints', (event, arg) => {
  var video = document.getElementById('video');
  var path = video.src;

  console.log('start extracting keypoints...')  
    client.invoke("extract_keypoints", path, (error, res) => {
    if(error) {
      console.error(error)
    } else {
      console.log(res.toString());
    }
  })
})

