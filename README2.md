# Web Scraping Script for Extracting Meeting Details from JPMorgan Funds Website

## Overview
This Python script is designed to scrape meeting details from the JPMorgan Funds website. It iterates through a list of funds and collects information about meetings associated with each fund. The script makes use of the `requests`, `re`, `BeautifulSoup`, and `pandas` libraries to perform web scraping and data manipulation.

## Prerequisites
Before running this script, ensure that you have the following installed:

- Python 3.x
- Required Python libraries: `requests`, `re`, `BeautifulSoup`, `pandas`

## Usage
1. Modify the `indexs` list with the fund IDs and names that you want to scrape. Each fund should be represented as a list containing the fund ID and name.

2. Run the script by executing it with Python. It will visit the JPMorgan Funds website, extract meeting details for each fund, and store the data in a Pandas DataFrame.

3. The scraped data is saved to an Excel file named `scraped_data.xlsx` in the current working directory.

## Script Structure
- The script first imports the necessary libraries and sets the target URL for scraping.
- It defines a regular expression pattern to extract data from HTML attributes.
- A list `data_list` is initialized to store the scraped data.

- The main loop iterates through the funds in the `indexs` list.
- For each fund, it sends a POST request to the website with specific parameters to retrieve meeting details.
- Within a nested loop, the script extracts meeting links, processes them, and collects meeting details.
- Extracted data includes company name, ticker, meeting date, agenda number, security ID, meeting type, and ISIN.
- Extracted meeting items (item number, proposal, type, vote, and for/against) are also collected.
- All data is appended to the `data_list`.

- The script then creates a Pandas DataFrame from the collected data.
- Finally, it saves the DataFrame to an Excel file.

## Output
The script generates an Excel file named `scraped_data.xlsx` containing a structured dataset with meeting details for the specified funds.

## Author
[Kamran Ali Kazmi]

## License
This script is released under the [MIT License](LICENSE).

Please use this script responsibly and considerate of the website's policies and guidelines.