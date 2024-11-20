"""
 ADEV-3005 (254275) Programming in Python
 Name: Noah Sinclair
 Student Number: 0385289

 Plots weather for a certain period of time.
"""
import db_operations as db
import matplotlib.pyplot as plt
import numpy as np

class PlotOperations:
  def __init__(self):
      self.database = db.DBOperations()
      self.database.purge_data()
      self.database.save_data()
      self.data = []

  def box_plot(self, range1, range2):
    self.data = self.database.fetch_data(range1,range2)
    print(self.data)
    l = np.concatenate(self.data)
    plt.boxplot(self.data)
    plt.show()

  def line_plot(self, date):
    self.data = self.database.fetch_data(date)
    x = []
    y = []
    for i in self.data:
      x.append(i[0][8:10])
    for i in self.data:
      y.append(i[1])
    plt.plot(x,y)
    plt.xlabel('Day')
    plt.ylabel('Temperature')
    plt.show()

  def reorder_data(self, data):

    return data

if __name__ == "__main__":
  po = PlotOperations()
  #po.box_plot("2022-06-01","2022-09-01")
  po.line_plot("2022-06-01")