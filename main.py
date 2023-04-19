import sys
from pyowm import OWM
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

owm = OWM('06d8b784623c5bab9cbd4dc9886fa343')

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        #Название города
        self.place_name = QLineEdit(self)
        self.place_button = QPushButton(self)
        self.a = QLabel(self)

        #Ввод данных
        self.place_label = QLabel('<h3 style="color: rgb(250, 255, 255);">Город:</h3>', self)
        self.temperature_label = QLabel('<h3 style="color: rgb(250, 255, 255);">Температура:</h3>', self)
        self.wind_label = QLabel('<h3 style="color: rgb(250, 255, 255);">Скорость ветра:</h3>', self)
        self.humidity_label = QLabel('<h3 style="color: rgb(250, 255, 255);">Влажность:</h3>', self)
        self.clouds_label = QLabel('<h3 style="color: rgb(250, 255, 255);">Облачность:</h3>', self)
        self.status_label = QLabel('<h3 style="color: rgb(250, 255, 255);">Статус:</h3>', self)
        self.status_image = QLabel(self)
        self.detail_label = QLabel('<h3 style="color: rgb(250, 255, 255);">Детали:</h3>', self)
        self.time_label = QLabel('<h3 style="color: rgb(250, 255, 255);">Время замера:</h3>', self)
        self.pixmap_sunny = QPixmap('E:/PythonProjects/PyWeather/icons/sunny.png')
        self.pixmap_clouds = QPixmap('E:/PythonProjects/PyWeather/icons/clouds.png')
        self.pixmap_rain = QPixmap('E:/PythonProjects/PyWeather/icons/rain.png')
        self.pixmap_shower_rain = QPixmap('E:/PythonProjects/PyWeather/icons/shower_rain.png')
        self.pixmap_broken_clouds = QPixmap('E:/PythonProjects/PyWeather/icons/broken_clouds.png')
        self.pixmap_clear = QPixmap('E:/PythonProjects/PyWeather/icons/clear.png')
        self.pixmap_snow = QPixmap('E:/PythonProjects/PyWeather/icons/snow.png')
        self.pixmap_rain = QPixmap('E:/PythonProjects/PyWeather/icons/rain.png')
        self.pixmap_mist = QPixmap('E:/PythonProjects/PyWeather/icons/mist.png')

        self.place_information = QLabel(self)
        self.temperature_information = QLabel(self)
        self.wind_information = QLabel(self)
        self.humidity_information = QLabel(self)
        self.clouds_information = QLabel(self)
        self.status_information = QLabel(self)
        self.detail_information = QLabel(self)
        self.time_information = QLabel(self)

        self.place_button.clicked.connect(self.get_information)

        self.init_ui()




    def init_ui(self):
        self.place_button.setStyleSheet("background-color: rgba(3,155,228,0.9)")
        self.place_name.setStyleSheet("background-color: rgba(3,155,228,0.9)")
        self.place_button.setText("Поиск")
        self.resize(400, 500)
        self.setWindowTitle('Weather')

        vbox, hbox = QVBoxLayout(), QHBoxLayout()

        hbox.addWidget(self.place_name)
        hbox.addWidget(self.place_button)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.place_label)
        hbox.addWidget(self.place_information)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.temperature_label)
        hbox.addWidget(self.temperature_information)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.wind_label)
        hbox.addWidget(self.wind_information)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.humidity_label)
        hbox.addWidget(self.humidity_information)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.clouds_label)
        hbox.addWidget(self.clouds_information)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.status_label)
        hbox.addWidget(self.status_information)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.detail_label)
        hbox.addWidget(self.detail_information)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.time_label)
        hbox.addWidget(self.time_information)
        vbox.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.status_image)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def get_information(self):
        place = self.place_name.text()
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place)
        w = observation.weather
        t = w.temperature("celsius")
        t1 = t['temp']
        t2 = t['feels_like']
        t3 = t['temp_max']
        t4 = t['temp_min']
        wi = w.wind()['speed']
        humi = w.humidity
        cl = w.clouds
        st = w.status
        dt = w.detailed_status
        ti = w.reference_time('iso')

        self.place_information.setText(place)
        self.temperature_information.setText(str(t1) + "°C" + "\nMAX:" + str(t3) + "°C" + "\nMIN:" + str(t4))
        self.wind_information.setText(str(wi) + "м/с")
        self.humidity_information.setText(str(humi) + "%")
        self.clouds_information.setText(str(cl) + "%")
        self.time_information.setText(ti)
        print(st)
        print(dt)
        if st == "Clouds" and dt == "overcast clouds":
            self.status_image.setPixmap(self.pixmap_clouds)
            self.status_information.setText("Облака")
            self.detail_information.setText("Затянутые облака")
        elif st == "Clouds" and dt == "broken clouds":
            self.status_image.setPixmap(self.pixmap_broken_clouds)
            self.status_information.setText("Облака")
            self.detail_information.setText("Разорванные облака")
        elif st == "Rain" and dt == "light intensity shower rain":
            self.status_image.setPixmap(self.pixmap_shower_rain)
            self.status_information.setText("Дождь")
            self.detail_information.setText("Ливень")
        elif st == "Clear" and dt == "clear sky":
            self.status_image.setPixmap(self.pixmap_clear)
            self.status_information.setText("Ясно")
            self.detail_information.setText("Чистое небо")
        elif st == "Snow" and dt == "light snow":
            self.status_image.setPixmap(self.pixmap_snow)
            self.status_information.setText("Снег")
            self.detail_information.setText("Легкий снег")
        elif st == "Rain" and dt == "light rain":
            self.status_image.setPixmap(self.pixmap_rain)
            self.status_information.setText("Дождь")
            self.detail_information.setText("Небольшой дождь")
        elif st == "Mist" and dt == "mist":
            self.status_image.setPixmap(self.pixmap_mist)
            self.status_information.setText("Туман")
            self.detail_information.setText("Лёгкий туман")
        elif st == "Fog" and dt == "fog":
            self.status_image.setPixmap(self.pixmap_mist)
            self.status_information.setText("Туман")
            self.detail_information.setText("Густой туман")



app = QApplication(sys.argv)
window = MainWindow()
window.setObjectName("MainWindow")
window.setStyleSheet("#MainWindow{background-color:#039be4}")
window.show()
app.exec()