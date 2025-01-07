# WEATHER SCRAPER

**Author: Noah Sinclair**

This project uses historical weather data scarrped from the Government of Canada website to graph the data in a line plot or box plot.

## How it's made:
**Languages**: Python

The app was built in Visual Studio Code using Python. Data is scraped from the Government of Canada website:
https://climate.weather.gc.ca/historical_data/search_historic_data_e.html
The scrape_weather.py file scrapes the data from the website. 
The db_operations.py file takes the data from the scarper and puts it in to a sqlite3 database while the plot_operations.py file plots the data in the database. 
weather_processor.py runs the application on the command line where it will promt the user with a menu. It also has a windows application that can be used and installed on a windows machine.

## Usage:
- Go to the settings.
- Insert the data into the database.
- Return to the main menu.
- Create a box plot or a line plot.
- Aside from those options, reinitalizing the database add the dates since it was last ran to the current date, in the settings menu, reinitalizing data table creates a whole new table for the database while Destroy data from database just gets rid of the data from the table.
