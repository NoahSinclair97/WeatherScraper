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
  def __init__(self):
    super().__init__()
    self.weather = {}
    self.year = int(datetime.datetime.now().strftime("%Y"))
    self.month = int(datetime.datetime.now().strftime("%m"))
    self.parsable = False
    self.abbr = False
    self.tbody = False
    self.td = False
    self.d = 0
    self.maxTemp = 0
    self.minTemp = 0
    self.meanTemp = 0

    # Scrapes data till a certain date
    while True:
      with urllib.request.urlopen(f'http://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2018&Day=1&Year={self.year}&Month={self.month}#') as response:
          html = str(response.read())
      #self.feed(html)
      t = threading.Thread(target=self.feed,args=(html,))
      t.start()
      t.join()
      self.month = self.month - 1
      if self.month == 0:
        self.year = self.year - 1
        self.month = 12
      if self.year == 2021:
        if self.month == 12:
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
      if self.parsable:
        self.set_daily_temp(self.year, self.month, self.day)
      self.d = 0
      self.maxTemp = 0
      self.minTemp = 0
      self.meanTemp = 0
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
          self.day = int(data)
          self.parsable = True
        else:
          self.parsable = False
      elif self.td and self.d < 3:
        if self.parsable:
          if self.d == 0:
            if "M" in data or "LegendM" in data or "\xa0" in data:
              self.maxTemp = "Missing"
            else:
              self.maxTemp = data
          elif self.d == 1:
            if "M" in data or "LegendM" in data or "\xa0" in data:
              self.minTemp = "Missing"
            else:
              self.minTemp = data
          elif self.d == 2:
            if "M" in data or "LegendM" in data or "\xa0" in data:
              self.meanTemp = "Missing"
            else:
              self.meanTemp = data
          self.d += 1

  def set_daily_temp(self,year,month,day):
    """
    Sets dictionary for the temperature per day
    """
    date = datetime.date(year,month,day)
    self.weather[f"{date}"] = {"Max": self.maxTemp, "Min": self.minTemp, "Mean": self.meanTemp}

  def get_weather(self):
    """
    Returns a dictionary of dictionaries of weather data
    """
    return self.weather

#if __name__ == "__main__":
#  test = WeatherScraper()
#  print(test.get_weather())