from key import KEY
from darksky import forecast
import geocoder
import sys
import pyqtgraph as pg
import time
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QInputDialog, QLabel, QMessageBox, QListWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot
from widget import Ui_MainWindow
from graph import Ui_Form


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.prm = []
        self.view = 'Столбик'
        self.tp = 'В данный момент'
        self.periodbtn.buttonClicked.connect(self.timeperiod)
        self.temp.stateChanged.connect(self.params)
        self.wind.stateChanged.connect(self.params)
        self.all.stateChanged.connect(self.params)
        self.pressure.stateChanged.connect(self.params)
        self.cloud.stateChanged.connect(self.params)
        self.viewbtn.buttonClicked.connect(self.set_view)
        self.btnhelp.clicked.connect(self.show_help)
        self.btnOK.clicked.connect(self.show_weather)

    def show_help(self):
        self.hw = QWidget()
        helpl = QLabel(self.hw)
        helpl.setText(open('help.txt').read())
        self.hw.setWindowTitle('Справка')
        self.hw.setGeometry(100, 100, 300, 300)
        self.hw.show()

    def timeperiod(self, sender):
        self.tp = sender.text()

    def params(self, state):
        if state == Qt.Checked:
            self.prm.append(self.sender().text())
        else:
            self.prm.remove(self.sender().text())

    def set_view(self, sender):
        self.view = sender.text()

    def show_weather(self):
        try:
            city = self.setcity.text()
            country = self.setcountry.text()
            location = geocoder.yandex(city + ' ' + country)
            data = forecast(KEY, location.latlng[0],
                            f'{location.latlng[1]}?lang=ru&units=si')
        except Exception:
            answ = QMessageBox.question(
                self, 'Ошибка',
                'Город/страна не найден(а) Попробуете еще раз?')
            if answ == QMessageBox.No:
                self.close()
            else:
                cc = ''
                while ', ' not in cc:
                    cc, btn = QInputDialog.getText(self, 'Погода для народа',
                                                   'Введите город, страну:')
                    if not btn:
                        self.close()
                        break
                if btn:
                    cc = cc.split(', ')
                    self.setcity.setText(cc[0])
                    self.setcountry.setText(cc[1])
                    self.show_weather()
        else:
            options = self.set_options(self.prm)
            timeper = self.set_timeper(self.tp)
            weather = Weather(data, options, timeper, self.view)
            weather.show_widget()

    def set_options(self, params):
        op = []
        transl = {'Температура': ('temperature', ' °C (температура)'),
                  'Облачность': ('cloudCover', ' (коэффициент облачности)'),
                  'Ветер': ('windSpeed', 'м/с (скорость ветра)'),
                  'Давление': ('pressure', ' гПа (давление)')}
        if 'Все показатели' not in params:
            for i in params:
                op.append(transl[i])
        return op

    def set_timeper(self, time):
        transl = {'В данный момент': ('currently', 0),
                  'На сегодня': ('hourly', (0, 12)),
                  'На завтра': ('hourly', (12, 34)),
                  'На неделю': ('daily', (0, 7))}
        return transl[time]


class GraphWidget(QWidget, Ui_Form):
    def __init__(self, data, par, tp):
        super().__init__()
        self.setupUi(self)
        self.d = data
        self.p = par
        self.tp = tp
        if self.p == []:
            self.p = [('cloudCover', ' (коэффициент облачности)')]
        if self.tp[0] == 'currently':
            self.tp = ('hourly', (0, 12))
        self.run()

    def run(self):
        x, y = [], []
        for i in range(self.tp[1][0], self.tp[1][1]):
            b = time.strptime(time.ctime(
                self.d[self.tp[0]]['data'][i]['time']),
                                "%a %b %d %H:%M:%S %Y")
            if self.tp[0] == 'hourly' and b[3] == 0:
                break
            if self.tp[0] == 'hourly':
                x.append(b[3])
            else:
                x.append(b[2])
            if self.p[-1][0] == 'temperature' and self.tp[0] == 'daily':
                y.append(self.d[self.tp[0]]['data'][i]['temperatureHigh'])
                self.graphicsView.setLabel('left', 'Температура')
            else:
                self.graphicsView.setLabel('left', self.p[-1][1])
                y.append(self.d[self.tp[0]]['data'][i][self.p[-1][0]])
        self.graphicsView.plot(x, y, pen='r')
        self.graphicsView.showGrid(x=True, y=True)
        self.graphicsView.setLabel('bottom', 'Bремя')


class Weather:
    def __init__(self, data, params, timeperiod, view):
        self.data = data
        self.par = params
        self.time = timeperiod
        self.view = view
        self.op = [('temperature', ' °C (температура)'),
                   ('temperatureHigh', ' °C (температура)'),
                   ('cloudCover', ' (коэффициент облачности)'),
                   ('humidity', ' (коэффициент влажности)'),
                   ('pressure', ' гПа  (давление)'),
                   ('windSpeed', ' м/с  (скорость ветра)')]

    def show_widget(self):
        if self.view == 'Столбик':
            self.ordinary()
        else:
            self.graph()

    def ordinary(self):

        main.widg = QWidget()
        mainlabel = QListWidget(main.widg)
        text = self.data[self.time[0]]['summary']
        pic = QPixmap(self.data[self.time[0]]['icon'] + '.png')
        mainlabel.addItem(text)
        mainlabel.addItem('')
        if self.time[1]:
            for j in range(self.time[1][0], self.time[1][1]):
                b = time.strptime(time.ctime(
                                  self.data[self.time[0]]['data'][j]['time']),
                                  "%a %b %d %H:%M:%S %Y")
                t = f'{b[2]}.{b[1]} {b[3]}:{b[4]}'
                text = t + '\n' + self.data[self.time[0]]['data'][j]['summary']
                mainlabel.addItem('')
                mainlabel.addItem(text)
                if self.par:
                    for i in self.par:
                        if i[0] == 'temperature' and self.time[0] == 'daily':
                            e = 'temperatureHigh'
                        else:
                            e = i[0]
                        text = str(self.data[self.time[0]]['data']
                                   [j][e]) + i[1]
                        mainlabel.addItem(text)
                else:
                    for i in self.op:
                        if i[0] in self.data[self.time[0]]['data'][j]:
                            text = str(self.data[self.time[0]]['data']
                                       [j][i[0]]) + i[1]
                            mainlabel.addItem(text)
        else:
            if self.par:
                for i in self.par:
                    text = str(self.data[self.time[0]][i[0]]) + i[1]
                    mainlabel.addItem(text)
            else:
                for i in self.op:
                    if i[0] in self.data[self.time[0]]:
                        text = str(self.data[self.time[0]][i[0]]) + i[1]
                        mainlabel.addItem(text)
        icon = QLabel(main.widg)
        icon.setPixmap(pic)
        icon.move(310, 10)
        mainlabel.resize(300, 600)
        main.widg.setWindowTitle('Прогноз погоды')
        main.widg.show()

    def graph(self):
        main.gw = GraphWidget(self.data, self.par, self.time)
        main.gw.setWindowTitle('Прогноз погоды')
        main.gw.show()


app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
