from flask import Flask
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

app = Flask(__name__)

def get_chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    
    # Specify the ChromeDriver path (matches Dockerfile installation location)
    service = Service(executable_path='/usr/local/bin/chromedriver')
    
    # Create driver with service and options
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

@app.route('/')
def scrape_example():
    try:
        driver = get_chrome_driver()
        driver.get('https://example.com')
        title = driver.title
        driver.quit()
        return f"Successfully scraped title: {title}"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)