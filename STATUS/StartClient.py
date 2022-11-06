import threading

from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import *
# from PySide2.QtUiTools import QUiLoader
from PyQt5 import uic, QtGui
from PyQt5.QtCore import QFile
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import PyQt5
import os
import sys
from src import user
from client import Ui_MainWindow
from login import Ui_loginForm

dirname = os.path.dirname(PyQt5.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


class LoginWin(QDialog, Ui_loginForm):
    def __init__(self, parent=None):
        super(LoginWin, self).__init__(parent)

        self.setupUi(self)

        self.closeBtn.clicked.connect(self.close)

        # an example
        self.sessionTbl.insertRow(0)
        for col, text in enumerate(['whuftp', 'Francis', 'FTP', '21', '172.16.20.239', '123456']):
            self.sessionTbl.setItem(0, col, QTableWidgetItem(text))

        self.sessionTbl.setColumnHidden(5, True)  # 隐藏密码

    def get_selected_row(self):
        row = self.sessionTbl.currentIndex().row()
        user = self.sessionTbl.item(row, 1).text()
        port = self.sessionTbl.item(row, 3).text()
        host = self.sessionTbl.item(row, 4).text()
        password = self.sessionTbl.item(row, 5).text()

        return user, port, host, password


class ClientUI(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(ClientUI, self).__init__(parent)

        self.setupUi(self)

        self.loginWin = LoginWin()

    def closeEvent(self, e):
        reply = QMessageBox.question(self,
                                     '询问',
                                     "确定要退出客户端吗？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            e.accept()
            sys.exit(0)
        else:
            e.ignore()


class Stats:
    def __init__(self):
        # 从文件中加载UI定义
        self.ftpserver = None  # 所连接到的服务器实例
        self.current_remote_dir = None  # 当前服务器目录
        qfile_stats = QFile("client.ui")
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.loginWin = LoginWin()
        self.ui = ClientUI()
        # self.ui.button.clicked.connect(self.handleCalc)

        # signal slots
        self.ui.eButton.clicked.connect(self.exit)  # 退出按键操作
        self.ui.ulButton.clicked.connect(self.upload)  # 上传按键操作
        self.ui.upButton.setEnabled(False)  # 返回上层按键操作
        self.ui.dButton.setEnabled(False)  # 下载按键操作
        self.ui.qButton.clicked.connect(self.connect_server)  # 查询按键操作

        self.loginWin.connectBtn.clicked.connect(self.connect_shortcut)

        self.client_root = 'home'
        self.modelt = QFileSystemModel()
        self.modelt.setRootPath(self.client_root)

        # 为控件添加模式。
        self.ui.treeView.setModel(self.modelt)
        self.ui.treeView.setRootIndex(self.modelt.index(self.client_root))  # 只显示设置的那个文件路径。
        self.ui.treeView.header().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.ui.treeView.doubleClicked.connect(self.file_name)  # 双击文件打开

        # 远程文件目录的icon
        cur_dir = os.getcwd()
        icon_dir_path = os.path.join(cur_dir, 'resources/common/directory.png')
        icon_file_path = os.path.join(cur_dir, 'resources/common/text.png')
        icon_ukn_path = os.path.join(cur_dir, 'resources/common/unknown.png')
        self.icon_dir = QIcon()
        self.icon_file = QIcon()
        self.icon_ukn = QIcon()
        self.icon_dir.addPixmap(QPixmap(icon_dir_path))
        self.icon_file.addPixmap(QPixmap(icon_file_path))
        self.icon_ukn.addPixmap(QPixmap(icon_ukn_path))
        self.server_root = '/'
        self.is_root = True  # 是否已经在用户目录的根目录
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.ui.tableWidget.verticalHeader().setVisible(False)
        self.ui.tableWidget.doubleClicked.connect(self.change_dir)

    def upload(self):
        QMessageBox.about(
            self.ui, '登入信息',
            f'''域名：\n{self.ui.domainEdit.text()}\n端口：\n{self.ui.portEdit.text()}\n用户名：\n{self.ui.nameEdit.text()}\n口令：\n{self.ui.pwEdit.text()}'''
        )

    def file_name(self, Qmodelidx):
        print(self.modelt.filePath(Qmodelidx))  # 输出文件的地址。
        print(self.modelt.fileName(Qmodelidx))  # 输出文件名

    def exit(self):
        reply = QMessageBox.question(self.ui,
                                     '询问',
                                     "确定要退出客户端吗？",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit(app.exec())  # 更正退出
        else:
            pass

    def connect_shortcut(self):
        user, port, host, password = self.loginWin.get_selected_row()
        self.ui.nameEdit.setText(user)
        self.ui.portEdit.setText(port)
        self.ui.domainEdit.setText(host)
        self.ui.pwEdit.setText(password)
        self.loginWin.close()

    def connect_server(self):
        # 注册线程来连接服务器，防止服务器未开启等情况时客户端卡死
        thread = threading.Thread(target=self._connect_server)
        thread.setDaemon(True)
        thread.start()

    def _connect_server(self):
        self.ui.serverLbl.setStyleSheet("color: rgb(255, 255, 255); background-color: rgba(128, 128, 128, 200);")
        self.ui.serverLbl.setText('远程目录列表（连接中……）：')
        try:
            self.ftpserver = user.ftpconnect(
                host=self.ui.domainEdit.text(),
                username=self.ui.nameEdit.text(),
                password=self.ui.pwEdit.text(),
                port=int(self.ui.portEdit.text()))
            self.current_remote_dir = self.ftpserver.pwd()

            self.ui.serverLbl.setStyleSheet("color: rgb(255, 255, 255); background-color: rgba(0, 170, 255, 200);")
            self.ui.serverLbl.setText('远程目录列表：')
            root_files = user.get_server_files(self.ftpserver)
            for Name, Size, Type, Date in root_files:
                file = [Name, Size, Type, Date]

                if file[-2] == 'file':
                    icon = self.icon_file
                elif file[-2] == 'dir':
                    icon = self.icon_dir
                else:
                    # unknown file type
                    icon = self.icon_ukn
                row_count = self.ui.tableWidget.rowCount()
                self.ui.tableWidget.insertRow(row_count)
                for col, text in enumerate(file):
                    if col == 0:
                        self.ui.tableWidget.setItem(row_count, col, QTableWidgetItem(icon, text))
                    else:
                        self.ui.tableWidget.setItem(row_count, col, QTableWidgetItem(text))

        except Exception as e:
            self.ui.serverLbl.setStyleSheet("color: rgb(255, 255, 255); background-color: rgba(255, 0, 0, 200);")
            self.ui.serverLbl.setText('远程目录列表（连接失败！）：')
            print(e)
            # QMessageBox.warning(self.ui, '警告', f'''{e}''')    # 弹窗会卡死

    def change_dir(self):
        row = self.ui.tableWidget.currentRow()
        target_type = self.ui.tableWidget.item(row, 2).text()
        target_dir = self.ui.tableWidget.item(row, 0).text()
        cur_dir = user.get_server_files(self.ftpserver)
        # 返回上一级目录
        if row == 0 and target_dir == '..' and cur_dir != '/':
            self.ftpserver.cwd('..')
            files = user.get_server_files(self.ftpserver)
            cur_dir = self.ftpserver.pwd()
            if cur_dir == '/':  # 回到了根目录
                self.ui.tableWidget.setRowCount(0)
                self.ui.tableWidget.clearContents()
            else:   # 不是根目录
                self.ui.tableWidget.setRowCount(1)  # 第一行用于返回上一级目录
                self.ui.tableWidget.clearContents()
                for col, text in enumerate(['..', ' ', ' ', ' ', ' ']):
                    self.ui.tableWidget.setItem(0, col, QTableWidgetItem(text))
        # 进入子目录
        elif target_type == 'dir':
            self.ftpserver.cwd(target_dir)
            files = user.get_server_files(self.ftpserver)
            self.ui.tableWidget.setRowCount(1)
            self.ui.tableWidget.clearContents()
            for col, text in enumerate(['..', ' ', ' ', ' ', ' ']):
                self.ui.tableWidget.setItem(0, col, QTableWidgetItem(text))

        # 无法进入文件
        else:
            # TODO: 打开文件
            return

        # 显示当前目录的文件并贴上图标
        for Name, Size, Type, Date in files:
            file = [Name, Size, Type, Date]
            if file[-2] == 'file':
                icon = self.icon_file
            elif file[-2] == 'dir':
                icon = self.icon_dir
            else:
                # unknown file type
                icon = self.icon_ukn
            row_count = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row_count)
            for col, text in enumerate(file):
                if col == 0:
                    self.ui.tableWidget.setItem(row_count, col, QTableWidgetItem(icon, text))
                else:
                    self.ui.tableWidget.setItem(row_count, col, QTableWidgetItem(text))

app = QApplication([])
stats = Stats()
stats.loginWin.exec()
stats.ui.show()
sys.exit(app.exec())  # 安全结束
