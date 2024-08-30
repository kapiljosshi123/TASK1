# TASK1
# Web Scraping and Data Storage Script

## Overview

This Python script scrapes business information from a specified website and saves the data into a CSV file and a MySQL database. The script uses web scraping techniques with Selenium and BeautifulSoup to gather information from multiple pages of a business directory.

## Features

- Scrapes business information (Company Name, Address, Revenue) from a series of web pages.
- Saves the scraped data into a CSV file.
- Optionally, stores the data into a MySQL database.
- Saves HTML pages locally for reference or re-processing.

## Dependencies

To run this script, you need the following Python libraries:
- `mysql-connector-python`
- `beautifulsoup4`
- `selenium`
- `lxml`

You can install these dependencies using pip:

```bash
pip install mysql-connector-python beautifulsoup4 selenium lxml

Setup
Install Python: Ensure Python is installed on your system.

Install Required Libraries: Run the following command to install the required Python libraries:

bash
Copy code
pip install mysql-connector-python beautifulsoup4 selenium lxml
Download Chrome WebDriver: Download and place the chromedriver executable in your system PATH or specify its location in the script.

Set Up MySQL Database: Ensure you have a MySQL server running and create a database named dnb_dat_aus. Create a table tbl_dnb_data with the following schema:

sql
Copy code
CREATE TABLE tbl_dnb_data (
    Company_Name VARCHAR(255),
    Address TEXT,
    Revenue VARCHAR(255)
);
Usage
Adjust the Script: Modify the script to match your database configuration and WebDriver location if necessary.

Run the Script: Execute the script using Python:

bash
Copy code
python your_script_name.py
The script will:

Create a folder named HtmlFiles if it doesn't already exist.
Scrape data from multiple pages of the specified website.
Save the HTML pages and data in a CSV file named dnb_data.csv.
Insert the data into the MySQL database if the database code section is not commented out.
Notes
Page Delay: The script includes delays to ensure pages are loaded properly. Adjust time.sleep() values if needed based on your network speed.
Error Handling: Basic error handling is included, but additional error handling may be necessary depending on the stability of the website being scraped.
Data Handling: The script assumes a specific HTML structure. Changes to the website’s structure may require updates to the scraping logic.

Author
KAPIL JOSHI
kapiljosshi@gmail.com
