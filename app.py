from datetime import datetime
import requests
import pandas as pd
from bs4 import BeautifulSoup 
import time 
while(True):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("At time: ", current_time)
    url = "https://finance.yahoo.com/cryptocurrencies/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the table containing cryptocurrency data
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
            
        for coin in data: 
            print(coin) 
            print('')
        time.sleep(600) # 10 minutes
    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")
