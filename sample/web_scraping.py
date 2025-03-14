import requests
from bs4 import BeautifulSoup

def get_weather():
    # 取得する都市のYahoo!天気URL（例: 東京）
    url = "https://weather.yahoo.co.jp/weather/jp/13/4410.html"

    # HTTPリクエストを送信（User-Agentを指定してボット対策を回避）
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # HTMLをパース
        soup = BeautifulSoup(response.text, "html.parser")


        # 今日の天気情報を取得
        weather = soup.find("p", class_="pict").text.strip()
        temperature_high = soup.find("li", class_="high").text.strip()
        temperature_low = soup.find("li", class_="low").text.strip()

        print(f"📍 東京の天気情報")
        print(f"☀️ 天気: {weather}")
        print(f"🌡 最高気温: {temperature_high}")
        print(f"❄️ 最低気温: {temperature_low}")
    else:
        print("天気情報を取得できませんでした")

def main():
    get_weather()

if __name__=="__main__":
    main()
