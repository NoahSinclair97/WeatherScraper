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

class WeatherParser(HTMLParser):
  """
  A class for parsing html
  """
  warning = "search by station name"
  dailyTemps = {}
  day = 0
  parsable = False
  abbr = False
  tbody = False
  td = False
  d = 0
  maxTemp = 0
  minTemp = 0
  meanTemp = 0

  def __init__(self, *, convert_charrefs: bool = True) -> None:
    super().__init__(convert_charrefs=convert_charrefs)
    self.weather = {}
    self.year = int(datetime.datetime.now().strftime("%Y"))
    self.month = int(datetime.datetime.now().strftime("%m"))
    while True:
      with urllib.request.urlopen(f'http://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year={self.year}&Month={self.month}#') as response:
          html = str(response.read())
      #self.feed(html)
      t = threading.Thread(target=self.feed,args=(html,))
      t.start()
      self.month = self.month - 1
      if self.month == 0:
        self.year = self.year - 1
        self.month = 12
      if self.year == 2022:
        if self.month == 1:
          break

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
      self.d = 0
      self.last = False
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
    if self.tbody:
      if self.abbr:
        if data.isnumeric():
          print(data)
          self.day = data
          self.parsable = True
        else:
          self.parsable = False
      elif self.td and self.d < 3:
        if self.parsable:
          print(data)
          if self.d == 0:
            self.maxTemp = data
          elif self.d == 1:
            self.minTemp = data
          elif self.d == 2:
            self.meanTemp = data
          self.d += 1

    def set_daily_temp(self,year,month,day):
      date = datetime.date(year,month,day)
      self.weather[f"{date}"] = {"Max": self.maxTemp, "Min": self.minTemp, "Mean": self.meanTemp}

    def weatherDictionary():
      return self.weather

if __name__ == "__main__":
  myparser = WeatherParser()