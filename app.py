from datetime import datetime
import requests
from bs4 import BeautifulSoup
import pytz
import time
from flask import Flask, render_template
from threading import Thread

# Initialize Flask app
app = Flask(__name__)

# Global variable to store scraped data
scraped_data = []
last_updated = ""

# Function to scrape cryptocurrency data
def scrape_crypto_data():
    global scraped_data, last_updated
    while True:
        tz_NY = pytz.timezone('Asia/Kolkata')
        now = datetime.now(tz_NY)
        current_time = now.strftime("%H:%M:%S")
        
        url = "https://finance.yahoo.com/cryptocurrencies/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        }
        
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table', {'class': 'markets-table'})  # Adjust the class if needed

            headings = soup.find_all('tr')[0] 
            headings_list = [] 
            for x in headings:
                if x.text.strip() != '':
                    headings_list.append(x.text.strip()) 
            headings_list = headings_list[:10]
            print(headings_list)
            data = [] 

            for x in range(1, 6): 
                row = soup.find_all('tr')[x] 
                column_value = row.find_all('td') 
                dict = {} 
                k=0
                for i in range(11):
                    if i!=2:
                        dict[headings_list[k]] = column_value[i].text.strip().split(' ')[0]
                        k+=1
                data.append(dict)
                scraped_data = data
                last_updated = current_time
                print(f"Data scraped successfully at {current_time}")
        else:
            print(f"Failed to fetch data. Status Code: {response.status_code}")
        
        time.sleep(600)  # Wait 10 minutes before the next scrape

# Flask route for the webpage
@app.route('/')
def home():
    # Initialize total market cap to 0
    total_market_cap = 0
    total_volume = sum(float(coin['Volume'].replace('B', '').replace('T', ''))
                        * (1e9 if 'B' in coin['Volume'] else 1e12) for coin in scraped_data)
    # Loop through each coin and sum its market cap
    for coin in scraped_data:
        market_cap = coin.get('Market Cap', '').strip()
        
        if market_cap:
            try:
                market_cap_value = float(market_cap.replace('B', '').replace('T', '').replace('M', '').replace(',', ''))                
                if 'B' in market_cap:
                    total_market_cap += market_cap_value * 1e9
                elif 'T' in market_cap:
                    total_market_cap += market_cap_value * 1e12
                elif 'M' in market_cap:
                    total_market_cap += market_cap_value * 1e6
            except ValueError:
                print(f"Error converting market cap: {market_cap} for coin: {coin}")
        
    print("Total Market Cap:", total_market_cap)

    bitcoin_market_cap = next((coin['Market Cap'] for coin in scraped_data if coin['Name'] == 'Bitcoin'), None)
    if bitcoin_market_cap:
        bitcoin_market_cap_value = float(bitcoin_market_cap.replace('B', '').replace('T', '').replace('M', '').replace(',', '')) * (
            1e9 if 'B' in bitcoin_market_cap else
            1e12 if 'T' in bitcoin_market_cap else
            1e6 if 'M' in bitcoin_market_cap else 1
        )
        bitcoin_dominance = round((bitcoin_market_cap_value / total_market_cap) * 100, 3)
    else:
        bitcoin_dominance = 0
    return render_template('index.html', 
                           data=scraped_data, 
                           total_market_cap=total_market_cap/10**12, 
                           total_volume=total_volume/10**9, 
                           bitcoin_dominance=bitcoin_dominance, 
                           updated=last_updated)

# Start the scraper in a separate thread
def start_scraper():
    thread = Thread(target=scrape_crypto_data)
    thread.daemon = True
    thread.start()

# Run the app
if __name__ == '__main__':
    start_scraper()
    app.run(host='0.0.0.0', port=8080)
