# Amazon Product Scraper

This Python script scrapes this [URL](https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1). It collects information such as the product URL, name, price, rating, number of reviews, product description, ASIN, and manufacturer. The scraped data is then exported to a CSV file.

## Requirements

To run this script, you need to have the following installed:

- Python 3.x
- `requests` library 
- `beautifulsoup4` library 
- `pandas` library 

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4 pandas
```

## How to Use

1. Clone this repository to your local machine or download the `scrape_products.py` file.

2. Make sure you have the required libraries installed as mentioned in the Requirements section.

3. Open the terminal or command prompt and navigate to the directory where the `scrape_products.py` file is located.

4. Run the script using the following command:

```bash
python scrape_products.py
```

5. The script will start scraping the product data from Amazon's search results. It will then proceed to scrape individual product pages for additional information.

6. After completing the scraping process, the script will create a CSV file named `amazon_products.csv` in the same directory, containing all the scraped data.
