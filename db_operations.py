"""
 ADEV-3005 (254275) Programming in Python
 Name: Noah Sinclair
 Student Number: 0385289

 Database operations for the weather scraper.
"""
import scrape_weather as sw
import dbcm
import sqlite3
import calendar

class DBOperations:
  def __init__(self):
    self.conn = sqlite3.connect("")
    self.cursor = self.conn.cursor()
    self.initialize_db()

  def fetch_data(self,range1,range2 = None):
    data = []
    if range2 != None:
      for row in self.cursor.execute(f"select * from weather where sample_date between date('{range1}') and date('{range2}')"):
        data.append(row)
    else:
      month = range1[5:7]
      year = range1[0:4]
      last_day = calendar.monthrange(int(year),int(month))[1]
      end_date = f"{year}-{month}-{last_day}"
      for row in self.cursor.execute(f"select * from weather where sample_date between date('{range1}') and date('{end_date}')"):
        data.append(row)
    return data

  def save_data(self):
    weather = sw.WeatherScraper().get_weather()
    sql = """insert or ignore into weather (sample_date,location,max_temp,min_temp,avg_temp)
            values (?,?,?,?,?)"""

    # Iterates through the dictionaries and inserts a new row to the table.
    for k,v in weather.items():
      try:
        data = (f'{k}','Winnipeg, MB',float(f'{v["Max"]}'),float(f'{v["Min"]}'),float(f'{v["Mean"]}'))
        self.cursor.execute(sql, data)
      except:
        pass

  def initialize_db(self):
    self.cursor.execute("""create table if not exists weather
              (id integer primary key autoincrement not null,
              sample_date text not null,
              location text not null,
              max_temp real not null,
              min_temp real not null,
              avg_temp real not null,
              unique(sample_date,location));""")

  def purge_data(self):
    self.cursor.execute("""delete from weather""")

if __name__ == "__main__":
  c = DBOperations()
  #c.purge_data()
  #c.save_data()
  #print(c.fetch_data("2022-06-01"))