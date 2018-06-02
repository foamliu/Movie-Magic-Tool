const {app, Menu, dialog} = require('electron')

var showOpen = function(mainWindow) {
  dialog.showOpenDialog({ 
    properties: [ 'openFile'], 
    filters: [{ name: 'Movies', extensions: ['mkv', 'avi', 'mp4'] }]},
    selectedFiles => 
    {
      console.log(selectedFiles);
      mainWindow.webContents.send('file_open', selectedFiles);
    }
  );
};

var detectShot = function(mainWindow) {
  mainWindow.webContents.send('edit_detect_shot', null);
};

var extractKeypoints = function(mainWindow) {
  mainWindow.webContents.send('edit_extract_keypoints', null);
};


module.exports = {
  load: function(mainWindow) {
    const template = [
      {
        label: '文件',
        submenu: [
          {
            label: '新建影片',
            click: function() { showOpen(mainWindow); },
            accelerator: 'CmdOrCtrl+N'
          },
          {type: 'separator'},
          {
            label: '导入媒体',
            click: function() { showOpen(mainWindow); },
            accelerator: 'CmdOrCtrl+I'
          },
          {type: 'separator'},
          {
            label: '分享',
            submenu: [
              {
                label: '朋友圈...',
                click: function() { showOpen(mainWindow); }
              },
              {
                label: '优酷...',
                click: function() { showOpen(mainWindow); }
              }
            ]
          }, 
        ]
      },    
      {
        label: '编辑',
        submenu: [
          {label: '撤销', role: 'undo'},
          {label: '重做', role: 'redo'},
          {type: 'separator'},
          {label: '剪切', role: 'cut'},
          {label: '拷贝', role: 'copy'},
          {label: '粘贴', role: 'paste'},
          {type: 'separator'},
          {
            label: '切分镜头',
            click: function() { detectShot(mainWindow); },
            accelerator: 'CmdOrCtrl+D'
          },
          {
            label: '提关键点',
            click: function() { extractKeypoints(mainWindow); },
            accelerator: 'CmdOrCtrl+E'
          }
        ]
      },
      {
        label: '视图',
        submenu: [
          {label: '重新加载', role: 'reload'},
          {label: '强制重新加载', role: 'forcereload'},
          {label: '开发者工具', role: 'toggledevtools'},
          {type: 'separator'},
          {label: '恢复缩放', role: 'resetzoom'},
          {label: '拉近', role: 'zoomin'},
          {label: '推远', role: 'zoomout'}
        ]
      },
      {
        label: '窗口',
        role: 'window',
        submenu: [
          {label: '最小化', role: 'minimize'},
          {label: '缩放', role: 'zoom'},
          {type: 'separator'},
          {label: '前置全部窗口', role: 'front'},
          {type: 'separator'},
          {role: 'togglefullscreen'}
        ]
      },
      {
        label: '帮助',
        role: 'help',
        submenu: [
          {
            label: '了解一下',
            click () { require('electron').shell.openExternal('13.65.250.1/demo3') }
          }
        ]
      }
    ]

    if (process.platform === 'darwin') {
      template.unshift({
        label: app.getName(),
        submenu: [
          {label: '关于 Movie Magic', role: 'about'},
          {type: 'separator'},
          {label: '服务', role: 'services', submenu: []},
          {type: 'separator'},
          {label: '隐藏', role: 'hide'},
          {label: '隐藏其他', role: 'hideothers'},
          {label: '显示全部', role: 'unhide'},
          {type: 'separator'},
          {label: '退出', role: 'quit'}
        ]
      })
    }

    Menu.setApplicationMenu(Menu.buildFromTemplate(template));
  }

}
  