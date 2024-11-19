import sqlite3

class DBCM:
  """
  A clas for opening a file.
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