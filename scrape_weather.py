"""
 ADEV-3005 (254275) Programming in Python
 Name: Noah Sinclair
 Student Number: 0385289
 Final Project

 A file for scraping weather data
"""

from html.parser import HTMLParser
import urllib.request
import datetime
import threading

class WeatherScraper(HTMLParser):
    """
    A class for parsing html
    """
    def __init__(self, last_month, last_year):
        super().__init__()
        self.weather = {}
        self.year = int(datetime.datetime.now().strftime("%Y"))
        self.month = int(datetime.datetime.now().strftime("%m"))
        self.parsable = False
        self.error = False
        self.abbr = False
        self.tbody = False
        self.td = False
        self.value_idx = 0
        self.max_temp = 0
        self.min_temp = 0
        self.mean_temp = 0
        self.thread = {}
        self.thread_count = 0

        # Scrapes data till a certain date
        while not self.error:
            with urllib.request.urlopen(f'http://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year={self.year}&Month={self.month}#') as response:
                html = str(response.read())
            #self.feed(html)
            self.thread[f"{self.thread_count}"] = threading.Thread(target=self.feed,args=(html,))
            self.thread[f"{self.thread_count}"].start()
            self.thread[f"{self.thread_count}"].join()
            self.thread_count = self.thread_count + 1

            if self.year == last_year:
                if self.month == last_month:
                    break

            self.month = self.month - 1
            if self.month == 0:
                self.year = self.year - 1
                self.month = 12

    def handle_starttag(self, tag, attrs):
        """
        Handles start tag of an element
        """
        if "td" in tag:
            self.td = True
        if "abbr" in tag:
            self.abbr = True
        if "tbody" in tag:
            self.tbody = True

    def handle_endtag(self, tag):
        """
        Handles end tag of an element
        """
        if "tr" in tag:
            if self.parsable:
                try:
                    self.set_daily_temp(self.year, self.month, self.day)
                except:
                    pass
            self.value_idx = 0
            self.max_temp = 0
            self.min_temp = 0
            self.mean_temp = 0
        if "td" in tag:
            self.td = False
        if "abbr" in tag:
            self.abbr = False
        if "tbody" in tag:
            self.tbody = False

    def handle_data(self, data):
        """
        Handles data of an element
        """
        # Checks if it reaches an unreadable date
        if "search by station name" in data.lower():
            self.error = True

        if self.tbody:
            if self.abbr:
                if data.isnumeric():
                    self.day = int(data)
                    self.parsable = True
                else:
                    self.parsable = False
            elif self.td and self.value_idx < 3:
                if self.parsable:
                    if self.value_idx == 0:
                        if "M" in data or "LegendM" in data or "\xa0" in data:
                            self.max_temp = "Missing"
                        else:
                            self.max_temp = data
                    elif self.value_idx == 1:
                        if "M" in data or "LegendM" in data or "\xa0" in data:
                            self.min_temp = "Missing"
                        else:
                            self.min_temp = data
                    elif self.value_idx == 2:
                        if "M" in data or "LegendM" in data or "\xa0" in data:
                            self.mean_temp = "Missing"
                        else:
                            self.mean_temp = data
                    self.value_idx += 1

    def set_daily_temp(self,year,month,day):
        """
        Sets dictionary for the temperature per day
        """
        date = datetime.date(year,month,day)
        self.weather[f"{date}"] = {"Max": self.max_temp, "Min": self.min_temp, "Mean": self.mean_temp}

    def get_weather(self):
        """
        Returns a dictionary of dictionaries of weather data
        """
        return self.weather
