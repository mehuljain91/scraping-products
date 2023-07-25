import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Part 1: Scrape product listings

def scrape_product_listing(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    product_data = []
    products = soup.select('div[data-asin]')
    for product in products:
        product_url = 'https://www.amazon.in' + product.select_one('.a-link-normal')['href']
        product_name = product.select_one('.a-text-normal').text.strip()
        product_price = product.select_one('.a-offscreen').text.strip()
        product_rating = product.select_one('.a-icon-alt').text.strip().split()[0]
        product_reviews = product.select_one('.a-size-base').text.strip().replace(',', '')
        product_data.append((product_url, product_name, product_price, product_rating, product_reviews))

    return product_data

def scrape_multiple_pages(base_url, num_pages):
    all_product_data = []
    for page_num in range(1, num_pages + 1):
        url = base_url + '&page=' + str(page_num)
        print(f"Scraping page {page_num}...")
        product_data = scrape_product_listing(url)
        all_product_data.extend(product_data)
        time.sleep(2)  # Add a small delay to avoid overwhelming the server
    return all_product_data

# Part 2: Scrape individual product pages

def scrape_product_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    product_description = soup.select_one('#productDescription').text.strip() if soup.select_one('#productDescription') else ""
    asin = soup.select_one('[name="ASIN"]').get('value') if soup.select_one('[name="ASIN"]') else ""
    manufacturer = soup.select_one('#bylineInfo').text.strip() if soup.select_one('#bylineInfo') else ""

    return product_description, asin, manufacturer

def scrape_multiple_products(product_urls):
    product_details = []
    for url in product_urls:
        print(f"Scraping product details: {url}")
        description, asin, manufacturer = scrape_product_details(url)
        product_details.append((url, description, asin, manufacturer))
        time.sleep(2)  # Add a small delay to avoid overwhelming the server
    return product_details

if __name__ == '__main__':
    # Part 1
    base_url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_'
    num_pages_to_scrape = 20

    all_products = scrape_multiple_pages(base_url, num_pages_to_scrape)

    # Part 2
    num_products_to_scrape = 200
    product_urls = [product[0] for product in all_products[:num_products_to_scrape]]

    product_details = scrape_multiple_products(product_urls)

    # Combine the data from Part 1 and Part 2
    combined_data = [(all_products[i] + product_details[i][1:]) for i in range(len(product_details))]

    # Export the data to CSV
    df = pd.DataFrame(combined_data, columns=["Product URL", "Product Name", "Product Price", "Rating", "Number of Reviews", "Product Description", "ASIN", "Manufacturer"])
    df.to_csv("amazon_products.csv", index=False)

    print("Data scraped and exported to amazon_products.csv")
