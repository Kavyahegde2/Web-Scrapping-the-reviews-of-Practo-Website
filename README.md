# Hospital Reviews Scraper

This Python script scrapes hospital reviews from the Practo website and stores them in an Excel sheet.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- Selenium
- BeautifulSoup4
- Pandas
- Chrome WebDriver

You can install the required Python packages using pip:
``` pip install selenium beautifulsoup4 pandas```

## Usage

1. Download and install the Chrome WebDriver from this repository or (https://sites.google.com/a/chromium.org/chromedriver/downloads). Make sure to place the WebDriver executable in the specified path or update the `chrome_driver_path` variable in the script accordingly.

2. Clone this repository or download the script directly.

3. Run the script using the following command:

``` python practo.py```

4. After execution, the script will save the scraped data in an Excel file named `new-manipal-laser-dental-clinic-hsr-layout.xlsx` in the same directory.

## About

This script automates the process of scraping hospital reviews from the Practo website. It utilizes Selenium for web scraping and interaction with the website, BeautifulSoup for parsing HTML content, and Pandas for data manipulation. Reviews are extracted from the specified URL, and additional reviews are loaded dynamically by clicking the "View more" button. Extracted data includes reviewer name, review time, visited doctor, review text, and recommendation status.

## Note

- Ensure that you have a stable internet connection while running the script to avoid interruptions during the scraping process.
- Review the Practo website's terms of service and usage policy before scraping data. Avoid excessive requests to their servers to prevent being blocked.
## For more steps refer the .txt file in this repository
