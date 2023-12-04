import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QComboBox
from PyQt5.QtGui import QPixmap
import requests

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Weather App')

        self.location_input = QLineEdit()
        self.location_input.setPlaceholderText('Enter location or enable GPS')
        self.location_button = QPushButton('Get Weather', clicked=self.get_weather)
        self.unit_combobox = QComboBox()
        self.unit_combobox.addItems(['Metric', 'Imperial'])
        self.weather_label = QLabel()
        self.weather_icon_label = QLabel()

        form_layout = QFormLayout()
        form_layout.addRow('Location:', self.location_input)
        form_layout.addRow('Unit:', self.unit_combobox)
        form_layout.addRow('', self.location_button)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addWidget(self.weather_label)
        layout.addWidget(self.weather_icon_label)

        self.setLayout(layout)

    def get_weather(self):
        location = self.location_input.text()
        unit = self.unit_combobox.currentText().lower()

        if not location:
            self.weather_label.setText('Please enter a location.')
            return

        weather_data = self.fetch_weather(location, unit)

        if weather_data:
            self.display_weather(weather_data)
        else:
            self.weather_label.setText('Unable to fetch weather data.')

    def fetch_weather(self, location, unit):
        base_url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {
            'q': location,
            'appid': self.api_key,
            'units': unit,
        }

        try:
            response = requests.get(base_url, params=params)
            data = response.json()

            if response.status_code == 200:
                return data
            else:
                self.weather_label.setText(f"Error: {data['message']}")
                return None
        except requests.ConnectionError:
            self.weather_label.setText('Error: Unable to connect to the weather API.')
            return None

    def display_weather(self, weather_data):
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        weather_condition = weather_data['weather'][0]['description']
        icon_id = weather_data['weather'][0]['icon']

        self.weather_label.setText(
            f'Temperature: {temperature}°C\nHumidity: {humidity}%\nWeather Condition: {weather_condition}'
        )

        icon_url = f"http://openweathermap.org/img/w/{icon_id}.png"
        icon_data = requests.get(icon_url).content
        pixmap = QPixmap()
        pixmap.loadFromData(icon_data)
        self.weather_icon_label.setPixmap(pixmap)

def main():
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
