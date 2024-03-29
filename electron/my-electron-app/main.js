const electron = require('electron');

const {
    app, // 控制应用生命周期的模块。
    BrowserWindow, // 创建原生浏览器窗口的模块。
    ipcMain,
} = electron;


let mainWindow;


function createWindow() {
    // 创建浏览器窗口。
    mainWindow = new BrowserWindow({
        width: 800,
        heigth: 600,
        //增加以下配置，不然汇报Uncaught ReferenceError: require is not defined
        webPreferences: {
            nodeIntegration: true,
            enableRemoteModule: true,
            contextIsolation: false,
        }

    });

    // 加载应用的 index.html。
    // 这里使用的是 file 协议，加载当前目录下的 index.html 文件。
    // 也可以使用 http 协议，如 mainWindow.loadURL('http://nodejh.com')。
    mainWindow.loadFile('index.html');

    // 启用开发者工具。
    mainWindow.webContents.openDevTools();

    // 当 window 被关闭，这个事件会被触发。
    mainWindow.on('closed', () => {
        // 取消引用 window 对象，如果你的应用支持多窗口的话，
        // 通常会把多个 window 对象存放在一个数组里面，
        // 与此同时，你应该删除相应的元素。
        mainWindow = null;
    });
}

// Electron 会在初始化后并准备
// 创建浏览器窗口时，调用这个函数。
// 部分 API 在 ready 事件触发后才能使用。
app.on('ready', createWindow);

// 当全部窗口关闭时退出。
app.on('window-all-closed', () => {
    // 在 macOS 上，除非用户用 Cmd + Q 确定地退出，
    // 否则绝大部分应用及其菜单栏会保持激活。
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

app.on('activate', () => {
    // 在 macOS 上，当点击 dock 图标并且该应用没有打开的窗口时，
    // 绝大部分应用会重新创建一个窗口。
    if (mainWindow === null) {
        createWindow();
    }
});

// 监听渲染进程发送的消息
ipcMain.on('asynchronous-message', (event, arg) => {
    const reply = arg.split('').reverse().join('');
    console.log('reply: ', reply);
    // 发送消息到主进程
    event.sender.send('asynchronous-reply', reply);
});