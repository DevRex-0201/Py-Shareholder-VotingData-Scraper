# Shareholder Meeting Voting Data Scraper

## Overview
This Python script is designed to scrape voting details from the shareholder meeting information available on the [https://vds.issproxy.com/](https://vds.issproxy.com/) website. The script utilizes web scraping techniques to gather data from the main meeting list page and individual meeting detail pages, providing valuable insights into voting outcomes for various funds.

## Project Structure
- **`main.py`**: The main Python script containing the web scraping logic.
- **`scraped_data.xlsx`**: An Excel file where the scraped data is stored.
- **`README.md`**: This file providing an overview, instructions, and information about the project.

## Prerequisites
Ensure that you have the following Python libraries installed before running the script:
```bash
pip install requests beautifulsoup4 pandas
```

## How to Run
1. Open the `main.py` file in your preferred Python environment.
2. Run the script. It will generate the `scraped_data.xlsx` file containing the scraped information.

## Project Details
The script performs the following tasks:

1. **Fetching Meeting Links:**
   - Sends a POST request to the main meeting list page with specified parameters for each fund ID.
   - Parses the HTML content using BeautifulSoup to extract meeting links.

2. **Fetching Meeting Details:**
   - Iterates through the meeting links, extracts meeting IDs, and sends another POST request to the individual meeting detail page.
   - Parses the HTML content to extract details such as company name, ticker, meeting date, record date, security ID, meeting type, etc.

3. **Data Storage:**
   - Appends the extracted data for each meeting to a list (`data_list`).
   - Creates a Pandas DataFrame from the list.

4. **Excel Output:**
   - Saves the DataFrame to an Excel file named `scraped_data.xlsx`.

## Parameters
- `url`: The main URL for the meeting list page.
- `indexs`: List of fund IDs for which data is to be scraped.
- `pattern`: Regular expression pattern for extracting meeting details from links.

## Customization
- Modify the `FromDateSubmit` and `ToDateSubmit` parameters in the `form_fund` dictionary to set the date range for the data to be scraped.

## Notes
- The script uses a while loop to handle paginated data on the website (`RecNum` parameter is increased by 25 in each iteration).
- Error handling is implemented to print error messages and break the loop in case of unsuccessful requests.

## Output
The scraped data is stored in the `scraped_data.xlsx` file, providing a comprehensive dataset for further analysis or reporting.

## Disclaimer
Web scraping may be subject to terms of service of the website being scraped. Ensure compliance with the website's policies before running the script. The script is provided as-is, and any modifications or use are at the user's discretion.
