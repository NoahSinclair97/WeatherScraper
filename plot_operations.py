"""
 ADEV-3005 (254275) Programming in Python
 Name: Noah Sinclair
 Student Number: 0385289
 Final Project

 Plots weather for a certain period of time.
"""
import db_operations as db
import matplotlib.pyplot as plt

class PlotOperations:
  """
  A class for plotting weather data
  """
  def __init__(self):
      """
      Initializes the data for the weather data
      """
      self.database = db.DBOperations()
      self.database.purge_data()
      self.database.save_data()

  def box_plot(self, range1, range2):
    """
    Shows a box plot for the input data
    """
    data = self.database.fetch_data(range1,range2)
    reordered_data = self.reorder_data(data)
    plt.boxplot(reordered_data)
    plt.show()

  def line_plot(self, date):
    """
    Shows a line plot for the input data
    """
    data = self.database.fetch_data(date)
    x = []
    y = []
    # Ierates over the data on the x axie
    for i in data:
      x.append(i[0][8:10])
    # Iterates over the data on the y axis
    for i in data:
      y.append(i[1])

    plt.plot(x,y)
    plt.xlabel('Day')
    plt.ylabel('Temperature')
    plt.show()

  def reorder_data(self, data):
    """
    Reorders the data per month to be plotted
    """
    jan = []
    feb = []
    mar = []
    apr = []
    may = []
    jun = []
    jul = []
    aug = []
    sep = []
    oct = []
    nov = []
    dec = []

    # Iterates over the data and puts it in to its own month
    for i in data:
      if i[0][5:7] == "01":
        jan.append(i[1])
      if i[0][5:7] == "02":
        feb.append(i[1])
      if i[0][5:7] == "03":
        mar.append(i[1])
      if i[0][5:7] == "04":
        apr.append(i[1])
      if i[0][5:7] == "05":
        may.append(i[1])
      if i[0][5:7] == "06":
        jun.append(i[1])
      if i[0][5:7] == "07":
        jul.append(i[1])
      if i[0][5:7] == "08":
        aug.append(i[1])
      if i[0][5:7] == "09":
        sep.append(i[1])
      if i[0][5:7] == "10":
        oct.append(i[1])
      if i[0][5:7] == "11":
        nov.append(i[1])
      if i[0][5:7] == "12":
        dec.append(i[1])
    finalData = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]

    return finalData

#if __name__ == "__main__":
#  po = PlotOperations()
#  po.box_plot("2022-01-01","2022-12-01")
#  #po.line_plot("2022-06-01")