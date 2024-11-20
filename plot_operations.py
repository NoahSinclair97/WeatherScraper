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
      pass

  def get_data_between(self, range1, range2):
    data = db.DBOperations().fetch_data(range1,range2)

  plt.boxplot("")
  plt.show()

if __name__ == "__main__":
  po = PlotOperations()