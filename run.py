import requests
import threading
import price

token = "" #Telegram bot token
url = "https://api.telegram.org/bot%s/" %(token)
n = 0

def sendMsg(message,chatid):
    requests.post(url + "sendMessage", data={"chat_id":chatid,"text":message},timeout=10)

def process(message,username,chatid):
    message = message.split(" ")
    for i in range(message.count(' ')):
        message.remove(' ')

    if "/indianmarket" in message[0]:
        try:
            sendMsg(price.price,chatid)
        except:
            sendMsg("Error",chatid)
    
    elif "/price" in message[0] and len(message[1]) != 0:
        try:
           pass
        except:
           pass



p = threading.Thread(target=price.getPrice)
p.start()



while True:
    try:
        data = requests.get(url+"getUpdates", data={"offset":n}, timeout=10).json()
        print(data)
        if len(data["result"]) > 0:
            n = data["result"][0]["update_id"] + 1
            username = data["result"][0]["message"]["from"]['username']
            chatid = data["result"][0]["message"]["chat"]["id"]
            message = data["result"][0]["message"]["text"]
            process(message,username,chatid)
    except:
        print("error")
