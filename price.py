import requests
import time

price = ""


def store(name,url):
	global price

	data = requests.get(url).json()

	if "Coinsecure"  in name:
		bid = data["bid"] 
		ask = data["ask"]
	else:
		bid = data["buy"]
		ask = data["sell"]
	
	if("Coinsecure" in name):
		price = "Coinsecure : \nBid : %s   Ask : %s\n" %(bid/100,ask/100)

	else:
		price = price + "%s :\nBid : %s   Ask : %s\n" %(name,bid,ask)


def getPrice():
	while True:
		
		store("Coinsecure","https://api.coinsecure.in/v0/noauth/newticker")
		store("Unocoin","https://www.unocoin.com/trade?all")
		store("Zebpay","https://api.zebpay.com/api/v1/ticker?currencyCode=INR")

		time.sleep(300)
