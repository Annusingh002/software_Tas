from PyQt5.QtWidgets import QTabBar, QHBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QColor, QPainterPath
from PyQt5.QtCore import QRectF, Qt, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTabWidget, QWidget,QVBoxLayout

import sys
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
from matplotlib.backends.backend_template import FigureCanvas
import pandas as pd
from PyQt5.QtCore import QTimer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class CustomTabBar(QTabBar):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(50)
        self.setMovable(True)

    def tabSizeHint(self, index):
        size = QSize(450, 50)
        return size

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for index in range(self.count()):
            rect = self.tabRect(index)
            color = QColor(200, 200, 200) if self.currentIndex() == index else QColor('#a2e7f5')
            painter.setBrush(color)


            path = QPainterPath()
            path.addRoundedRect(QRectF(rect), 20, 20)
            painter.drawPath(path)

            painter.setPen(Qt.black)
            font = QFont("Arial", 15)
            painter.setFont(font)
            painter.drawText(rect, Qt.AlignCenter, self.tabText(index))





class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle(" KALPANA SOFTWARE TASK ")
        self.setGeometry(0,0,1900,920)
        self.setStyleSheet('background-color:#030369;')

        Central_Widget = QWidget(self)
        self.setCentralWidget(Central_Widget)
        self.tabs = QTabWidget(Central_Widget)
        self.tabs.setTabBar(CustomTabBar())


        self.tabs.setGeometry(20,50,400,400)
        self.create_tabs()
        layout = self.centralWidget().layout() or QVBoxLayout()
        layout.addWidget(self.tabs)
        main_layout = QVBoxLayout()
        Central_Widget.setLayout(main_layout)
        ##########
        self.data = self.load_data('trial_data.csv')
        self.current_index = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_graphs)
        self.timer.start(1000)



#top lable

        label_layout = QVBoxLayout()
        button_layout = QHBoxLayout()


        label = QLabel("                    SOFTWARE STATE          "
                            "                TEAM KALPANA : 2024-CANSAT-ASI-O23            "
                            "             TIME                        "
                            "              PACKET COUNT               ", self)

        label.setFont(QFont("Arial", 13))
        label.setFixedSize(1900,50)
        label.setStyleSheet('color: #a2e7f5;'
                            'background-color: #030369')
        label_layout.addWidget(label)

        label2 = QLabel(self)



        label2.setFixedSize(100,70)
        label2.setStyleSheet('color: blue;'
                             'background-color: #030369')
        logo = QPixmap("Logo2.png")
        label2.setPixmap(logo)
        label2.setScaledContents(True)


# top buttons

        button1=QPushButton("  LAUNCH_PAD  ")
        button2=QPushButton("      0       ")
        button3=QPushButton("      0       ")
        button1.setFixedSize(250,50)
        button2.setFixedSize(250,50)
        button3.setFixedSize(250,50)

        button1.clicked.connect(self.button_clicked9)
        button2.clicked.connect(self.button_clicked10)
        button3.clicked.connect(self.button_clicked10)

        button1.setFont(QFont("Arial", 12))
        button2.setFont(QFont("Arial", 12))
        button3.setFont(QFont("Arial", 12))

        button1.setStyleSheet("border :3px solid red;"
                             "background-color : white;"
                              "border-radius : 25px;")
        button2.setStyleSheet("border :3px solid red;"
                             "background-color : white;"
                              "border-radius : 25px;")
        button3.setStyleSheet("border :3px solid red;"
                             "background-color : white;"
                              "border-radius : 25px;")

        label3 = QLabel(self)
        label3.setStyleSheet("background-color : #030369;")
        label3.setFixedSize(70,20)

        label4 = QLabel(self)
        label4.setStyleSheet("background-color : #030369;")
        label4.setFixedSize(70, 20)

        button_layout.addWidget(button1)
        button_layout.addWidget(label4)
        button_layout.addWidget(label2)
        button_layout.addWidget(label3)
        button_layout.addWidget(button2)
        button_layout.addWidget(button3)


        combine_layout = QVBoxLayout()
        combine_layout.addLayout(label_layout)
        combine_layout.addLayout(button_layout)



        button2_layout = QHBoxLayout()
        but1 = QPushButton("BOOT",self)
        but1.setFixedSize(150,50)
        but1.setStyleSheet("background-color : #087da1;"
                            'color: yellow;'
                            'border-radius : 15px;'
                            'border :3px solid black;')
        but1.setFont(QFont("Arial", 13))
        but1.clicked.connect(self.button_clicked1)

        but2 = QPushButton("Set Time",self)
        but2.setFixedSize(150, 50)
        but2.setStyleSheet("background-color : #087da1;"
                           'color: yellow;'
                           'border-radius : 15px;'
                           'border :3px solid black;')
        but2.setFont(QFont("Arial", 13))
        but2.clicked.connect(self.button_clicked2)

        but3 = QPushButton("calibrated",self)
        but3.setFixedSize(150, 50)
        but3.setStyleSheet("background-color : #087da1;"
                           'color: yellow;'
                           'border-radius : 15px;'
                           'border :3px solid black;')
        but3.setFont(QFont("Arial", 13))
        but3.clicked.connect(self.button_clicked3)

        but4 = QPushButton(" ON|OFF ",self)
        but4.setFixedSize(150, 50)
        but4.setStyleSheet("background-color : #087da1;"
                           'color: yellow;'
                           'border-radius : 15px;'
                           'border :3px solid black;')
        but4.setFont(QFont("Arial", 13))
        but4.clicked.connect(self.button_clicked4)

        but5 = QPushButton(" CX ",self)
        but5.setFixedSize(150, 50)
        but5.setStyleSheet("background-color : #087da1;"
                           'color: yellow;'
                           'border-radius : 15px;'
                           'border :3px solid black;')
        but5.setFont(QFont("Arial", 13))
        but5.clicked.connect(self.button_clicked5)

        but6 = QPushButton("SIM Enable",self)
        but6.setFixedSize(150, 50)
        but6.setStyleSheet("background-color : #087da1;"
                           'color: yellow;'
                           'border-radius : 15px;'
                           'border :3px solid black;')
        but6.setFont(QFont("Arial", 13))
        but6.clicked.connect(self.button_clicked6)

        but7 = QPushButton("SIM Active",self)
        but7.setFixedSize(150, 50)
        but7.setStyleSheet("background-color :#087da1;"
                           'color: yellow;'
                           'border-radius : 15px;'
                           'border :3px solid black;')
        but7.setFont(QFont("Arial", 13))
        but7.clicked.connect(self.button_clicked7)

        but8 = QPushButton("SIM Disable",self)
        but8.setFixedSize(150, 50)
        but8.setStyleSheet("background-color : #087da1;"
                           'color: yellow;'
                           'border-radius : 15px;'
                           'border :3px solid black;')
        but8.setFont(QFont("Arial", 13))
        but8.clicked.connect(self.button_clicked8)

        button2_layout.addWidget(but1)
        button2_layout.addWidget(but2)
        button2_layout.addWidget(but3)
        button2_layout.addWidget(but4)
        button2_layout.addWidget(but5)
        button2_layout.addWidget(but6)
        button2_layout.addWidget(but7)
        button2_layout.addWidget(but8)

        main_layout.addLayout(combine_layout)
        main_layout.addWidget(self.tabs)
        main_layout.addLayout(button2_layout)

    def button_clicked1(self):
        print("BOOT")
    def button_clicked2(self):
        print("Set Time")

    def button_clicked3(self):
        print("Calibrate")

    def button_clicked4(self):
        print("ON/OFF")

    def button_clicked5(self):
        print("CX")

    def button_clicked6(self):
        print("SIM Enable")

    def button_clicked7(self):
        print("SIM Active")

    def button_clicked8(self):
        print("SIM Disable")

    def button_clicked9(self):
        print("LAUNCH_PAD")

    def button_clicked10(self):
        print(" 0 ")



    def create_tabs(self):
        # Example of adding tabs (replace with your existing tab creation code)
        tab1 = QWidget()
        tab1_layout = QVBoxLayout()
        tab1_label = QLabel("This is the first tab")
        tab1_layout.addWidget(tab1_label)
        tab1.setLayout(tab1_layout)
        tab1.setStyleSheet("background-color:#d8affa")

        tab2 = QWidget()
        tab2_layout = QVBoxLayout()


        tab2.setStyleSheet("background-color:#d8affa")

        ######
        self.canvas, self.figure, self.axes = self.create_canvas()
        self.canvas.setStyleSheet("background-color:#d8affa")
        tab2_layout.addWidget(self.canvas)
        tab2.setLayout(tab2_layout)
        self.init_graphs()


        tab3 = QWidget()
        tab3_layout = QVBoxLayout()
        tab3_label = QLabel("This is the third tab")
        tab3_layout.addWidget(tab3_label)
        tab3.setLayout(tab3_layout)
        tab3.setStyleSheet("background-color:#d8affa")

        tab4 = QWidget()
        tab4_layout = QVBoxLayout()
        tab4_label = QLabel("This is the fourth tab")
        tab4_layout.addWidget(tab4_label)
        tab4.setLayout(tab4_layout)
        tab4.setStyleSheet("background-color:#d8affa")


        self.tabs.addTab(tab1, "     Telemetary Data          ")
        self.tabs.addTab(tab2, "       Graphs                   ")
        self.tabs.addTab(tab3, "    Location and 3D Plotiing   ")
        self.tabs.addTab(tab4, "      Live Telecast           ")

    def create_canvas(self):
        figure, axes = plt.subplots(2, 3, figsize=(15, 10))
        figure.set_facecolor('#d8affa')
        canvas = FigureCanvas(figure)

        return canvas, figure, axes

    def load_data(self, file_path):
        data = pd.read_csv('trial_data.csv')
        data = data.dropna(how='all')
        return data

    def init_graphs(self):
        pairs = [('TIME', 'PRESSURE'), ('ALTITUDE','TIME'), ('VOLTAGE', 'TIME'), ('GYRO_R', 'TIME'),
                     ('ACC_R', 'TIME'), ('GNSS_ALTITUDE', 'TIME')]  #
        colors = ['b', 'b', 'b', 'b', 'b', 'b']
        for ax, (y_col, x_col), color in zip(self.axes.flatten(), pairs, colors):
            ax.plot([], [], color=color)
            ax.set_title(f'{x_col} vs {y_col}')
            ax.grid(True)

    def update_graphs(self):
        if self.current_index < len(self.data):
            for ax in self.axes.flatten():
                ax.clear()
            pairs = [('TIME', 'PRESSURE'), ('TIME','ALTITUDE'), ('TIME', 'VOLTAGE'), ('TIME', 'GYRO_R'),
                     ('TIME', 'ACC_R'), ('TIME', 'GNSS_ALTITUDE')]
            colors = ['b', 'b', 'b', 'b', 'b', 'b']
            for ax, (x_col, y_col), color in zip(self.axes.flatten(), pairs, colors):
                ax.plot(self.data[x_col][:self.current_index + 1], self.data[y_col][:self.current_index + 1],
                        color=color)
                ax.set_title(f'{y_col} vs {x_col}')
                ax.grid(True)  # Add grid to the graph
            self.canvas.draw()
            self.current_index += 1
        else:
            self.timer.stop()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

