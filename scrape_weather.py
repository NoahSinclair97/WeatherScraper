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

class WeatherScraper(HTMLParser):
  """
  A class for parsing html
  """
  warning = "search by station name"
  def handle_starttag(self, tag, attrs):
    """
    Handles start tag of an element
    """
    #print("Found start tag :", tag)


  def handle_endtag(self, tag):
    """
    Handles end tag of an element
    """
    #print("Found end tag :", tag)


  def handle_data(self, data):
    """
    Handles data of an element
    """
    #print("Found some data :", data)
    if self.warning in data.lower():
      print("The page needs correct data")


def get_ip():
  """
  Gets the current ip address.
  """
  year = datetime.datetime.year
  month = datetime.datetime.month

  myparser = WeatherScraper()
  with urllib.request.urlopen(f'http://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1740&EndYear=2018&Day=1&Year=2024&Month=12#') as response:
    html = str(response.read())
  myparser.feed(html)
  return myparser

if __name__ == "__main__":
  print(get_ip())