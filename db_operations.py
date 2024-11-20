"""
 ADEV-3005 (254275) Programming in Python
 Name: Noah Sinclair
 Student Number: 0385289
Final Project

 Database operations for the weather scraper.
"""
import sqlite3
import calendar
import scrape_weather as sw

class DBOperations:
    """
    A class for the database operations
    """
    def __init__(self):
        """
        Initializes the database
        """
        self.conn = sqlite3.connect("")
        self.cursor = self.conn.cursor()
        self.initialize_db()

    def fetch_data(self,range1,range2 = None):
        """
        Gets the data in the database based on given ranges
        """
        data = []

        if range2 is not None:
            # Iterates over the rows between two dates
            for row in self.cursor.execute(f"select sample_date, avg_temp from weather where sample_date between date('{range1}') and date('{range2}')"):
                data.append(row)
        else:
            month = range1[5:7]
            year = range1[0:4]
            last_day = calendar.monthrange(int(year),int(month))[1]
            end_date = f"{year}-{month}-{last_day}"
            # Iterates over the rows for a given month
            for row in self.cursor.execute(f"select sample_date, avg_temp from weather where sample_date between date('{range1}') and date('{end_date}')"):
                data.append(row)

        return data

    def save_data(self):
        """
        Saves the weather data to the database
        """
        weather = sw.WeatherScraper(12, 2023).get_weather()
        sql = """insert or ignore into weather (sample_date,location,max_temp,min_temp,avg_temp)
                values (?,?,?,?,?)"""

        # Iterates through the dictionaries and inserts a new row to the table.
        for k,v in weather.items():
            try:
                data = (f'{k}','Winnipeg, MB',float(f'{v["Max"]}'),float(f'{v["Min"]}'),float(f'{v["Mean"]}'))
                self.cursor.execute(sql, data)
            except:
                pass # Catches missing data and passes over it
        self.conn.commit()

    def initialize_db(self):
        """
        Creates the table for the database if it doesn't exist
        """
        self.cursor.execute("""create table if not exists weather
                  (id integer primary key autoincrement not null,
                  sample_date text not null,
                  location text not null,
                  max_temp real not null,
                  min_temp real not null,
                  avg_temp real not null,
                  unique(sample_date,location));""")

    def purge_data(self):
        """
        Purges data from the database
        """
        self.cursor.execute("""delete from weather""")
        self.conn.commit()

    def update_data(self):
        """
        Updates the weather data in the database
        """
        date = ""

        for row in self.cursor.execute("select sample_date from weather order by date(sample_date) desc limit 1;"):
            date = row

        try:
            weather = sw.WeatherScraper(int(date[0][5:7]), int(date[0][0:4])).get_weather()
            sql = """insert or ignore into weather (sample_date,location,max_temp,min_temp,avg_temp)
                    values (?,?,?,?,?)"""

            # Iterates through the dictionaries and inserts a new row to the table.
            for k,v in weather.items():
                try:
                    data = (f'{k}','Winnipeg, MB',float(f'{v["Max"]}'),float(f'{v["Min"]}'),float(f'{v["Mean"]}'))
                    self.cursor.execute(sql, data)
                except:
                    pass # Catches missing data and passes over it
            self.conn.commit()
        except:
            print("Error updating dataset")
