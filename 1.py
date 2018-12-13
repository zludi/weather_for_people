KEY = '2ac1ca92a1aad9b8338de9c7065349ab'
from darksky import forecast
import geocoder
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import Qt
from widget import Ui_MainWindow
 
 
class MyWidget(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.prm = set()
        self.periodbtn.buttonClicked.connect(self.timeperiod)
        self.temp.stateChanged.connect(self.params)
        self.wind.stateChanged.connect(self.params)
        self.all.stateChanged.connect(self.params)
        self.pressure.stateChanged.connect(self.params)
        self.cloud.stateChanged.connect(self.params)
        self.viewbtn.buttonClicked.connect(self.set_view)
        self.btnOK.clicked.connect(self.show_weather)


    def timeperiod(self, sender):
        self.tp = sender.text()


    def params(self, state):
        if state == Qt.Checked:
            self.prm.add(self.sender().text())


    def set_view(self, sender):
        self.view = sender.text()


    def show_weather(self):
        print(1)
        city = self.setcity.text()
        country = self.setcountry.text()
        location = geocoder.yandex(city + ' ' + country)
        print(location.latlng)
        forecast = forecast(KEY, int(location.latlng[0]), f'{locaton.latlng[1]}?lang=ru&units=si')
        #self.options = self.set_options(self.prm)
        print(forecast.currently.temperature)
        


app = QApplication(sys.argv)
main = MyWidget()
main.show()
sys.exit(app.exec_())
