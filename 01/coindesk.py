import requests
import json


#print(data)
def btc_cost_counter(countBtc, code):
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    data = json.loads(r.text)


    for i in data["bpi"] :
        if i == code:
            string_rate = data["bpi"][i]["rate"]
            return countBtc*float(string_rate.replace(",", ""))




bitcoin_count = 5
code_usd = "USD"

price = btc_cost_counter(bitcoin_count, code_usd)
print(f"Цена Битка сейчас = {price}")


a = "sdsdsds"
# dir(a)
# string 
# list 
# dict 

#
