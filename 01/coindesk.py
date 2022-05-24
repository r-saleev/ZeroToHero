import requests
import json
import btc_counter
from datetime import date


#print(data)

def get_data(url):
    r = requests.get(url)
    data = json.loads(r.text)
    return data


def get_rate(data, code):
    for i in data["bpi"] :
        if i == code:
            string_rate = data["bpi"][i]["rate"]

    return float(string_rate.replace(",", ""))
        

def btc_log(code, bitcoin_count, price):
    f = open("btc_log.txt", "a")
    f.write(f"[{date.today()}]: Валюта : {code}, Количество битков: {bitcoin_count} : общая стоимость: {price} \n")

def btc_print(price):
    print(f"Цена Битка сейчас = {price}")


# слой транспорта ( HTTP, SSH )

if  __name__ == "__main__":
    bitcoin_count = 5
    code_usd = "USD"
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    data = get_data(url)
    rate = get_rate(data, code_usd)
    price = btc_counter.btc_cost_counter(bitcoin_count, rate)

    # Сохраняем данные в файл, в формате
    # [date] Название валюты , количество битков : общая стоимость 
    btc_log(code_usd, bitcoin_count, price)
    

# Поключить sql lite 
# Создать таблицу
# Записывать туда данные 
# date
# code
# count
# price

# Создать скрипт, который подключается к этим данным, и выводит среднюю стоимость 
# битка. 

# dir(a)
# string 
# list 
# dict 
# Алиасы bash
#

# Слой формирования данных для программы
# Слой получения данных из источников
    json
# Слой бизнес логики 
# Слой представления