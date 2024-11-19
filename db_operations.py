"""
 ADEV-3005 (254275) Programming in Python
 Name: Noah Sinclair
 Student Number: 0385289

 Database operations for the weather scraper.
"""
import scrape_weather as sw
import dbcm
import sqlite3

class DBOperations:
  def __init__(self):
    self.conn = sqlite3.connect("")
    self.cursor = self.conn.cursor()
    self.initialize_db()

  def fetch_data(self):
    for row in self.cursor.execute("select * from samples"):
      print(row)

  def save_data(self):
    weather = sw.WeatherScraper().get_weather()
    sql = """insert or ignore into samples (sample_date,location,max_temp,min_temp,avg_temp)
            values (?,?,?,?,?)"""

    # Iterates through the dictionaries and inserts a new row to the table.
    for k,v in weather.items():
      try:
        data = (f'{k}','Winnipeg, MB',f'{v["Max"]}',f'{v["Min"]}',f'{v["Mean"]}')
        self.cursor.execute(sql, data)
      except:
        print("The data contained missing values.")

  def initialize_db(self):
    self.cursor.execute("""create table if not exists samples
              (id integer primary key autoincrement not null,
              sample_date text not null,
              location text not null,
              max_temp real not null,
              min_temp real not null,
              avg_temp real not null,
              unique(sample_date,location));""")
    print("Table created successfully.")

  def purge_data(self):
    self.cursor.execute("""delete from samples""")

if __name__ == "__main__":
  c = DBOperations()
  c.purge_data()
  c.save_data()
  c.fetch_data()