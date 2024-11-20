"""
 ADEV-3005 (254275) Programming in Python
 Name: Noah Sinclair
 Student Number: 0385289
 Final Project
 Database context manager.
"""
import sqlite3

class DBCM:
  """
  A class for a database context manager.
  """
  def __init__(self):
    """
    Initializes the connection to the database
    """
    self.conn = sqlite3.connect("")

  def __enter__(self):
    """
    Returns the cursor for the database
    """
    return self.conn.cursor()

  def __exit__(self, exc_type,exc_value,exc_trace):
    """
    Commits the data to the database and closes the connection
    """
    self.conn.commit()
    self.conn.close()