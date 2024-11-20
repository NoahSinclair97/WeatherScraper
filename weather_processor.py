"""
 ADEV-3005 (254275) Programming in Python
 Name: Noah Sinclair
 Student Number: 0385289
 Final Project

 Creates a menu for a user to input data
"""
from menu import Menu
import db_operations as db
import plot_operations as po

class WeatherProcessor:
  """
  A class for processing the weather data through a menu
  """
  def __init__(self):
    self.database = db.DBOperations()
    self.plot = po.PlotOperations(self.database)

    # Sets the settings menu options
    self.setting_menu_options = [
      ("Reinitialize database table", self.database.initialize_db),
      ("Destroy data from database", self.database.purge_data),
      ("Insert data into the database", self.database.save_data),
      ("Return to main menu", Menu.CLOSE)
    ]
    # Initializaes settings rover menu
    self.settings_menu = Menu(
        title="Settings",
        message="Please choose an option.",
        prompt=">",
        options=self.setting_menu_options)

    # Sets the main menu options
    self.main_menu_options = [
      ("Update dataset", self.update_data),
      ("Create a Boxplot", self.create_boxplot),
      ("Create a Lineplot", self.create_lineplot),
      ("Settings", self.settings_menu.open),
      ("Exit", Menu.CLOSE)
    ]
    # Initializaes the main menu
    self.main_menu = Menu(
        title="Main Menu",
        message="Please choose an option.",
        prompt=">",
        options=self.main_menu_options)

  def update_data(self):
    self.database.save_data()

  def run(self):
    self.main_menu.open()

  def create_boxplot(self):
    try:
      start_year = input("Please enter a start year format (YYYY): ")
      end_year = input("Please enter an end year format (YYYY): ")
      start_date = f"{start_year}-01-01"
      end_date = f"{end_year}-01-01"
      self.plot.box_plot(start_date,end_date)
    except:
      self.main_menu.message = "Incorrect format input!"

  def create_lineplot(self):
    try:
      year = input("Please enter a year format (YYYY): ")
      month = input("Please enter a month format (MM): ")
      date = f"{year}-{month}-01"
      self.plot.line_plot(date)
    except:
      self.main_menu.message = "Incorrect format input!"

if __name__ == "__main__":
  WeatherProcessor().run()