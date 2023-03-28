import requests


def get_info():
    response = requests.get(url="https://yobit.net/api/3/info")

    with open("info.txt", "w") as file:
        file.write(response.text)

    return response.text

def get_ticker(coin1="btc", coin2="usdt"):
    #response = requests.get(url="https://yobit.net/api/3/ticker/btc_usdt")
    response = requests.get(url=f"https://yobit.net/api/3/ticker/{coin1}_{coin2}")
    with open("info.txt", "w") as file:
        file.write(response.text)

    return response.text

def main():
    #print(get_ticker())
    print(get_ticker(coin1='btc'))
    #print(get_info())
    
if __name__ == '__main__':
    main()