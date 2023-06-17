import tkinter as tk
from tkinter import messagebox
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHAVANTAGE_API_KEY = 'YOUR_ALPHAVANTAGE_API_KEY'
NEWSAPI_API_KEY = 'YOUR_NEWSAPI_API_KEY'
TWILIO_ACCOUNT_SID = 'YOUR_TWILIO_ACCOUNT_SID'
TWILIO_AUTH_TOKEN = 'YOUR_TWILIO_AUTH_TOKEN'
TWILIO_PHONE_NUMBER = 'YOUR_TWILIO_PHONE_NUMBER'
RECIPIENT_PHONE_NUMBER = 'YOUR_RECIPIENT_PHONE_NUMBER'

ALPHAVANTAGE_URL = 'https://www.alphavantage.co/query'
NEWSAPI_URL = 'https://newsapi.org/v2/everything'

def send_message():
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': STOCK,
        'apikey': ALPHAVANTAGE_API_KEY,
        'interval': '60min',
        'slice': 'year1month1'
    }

    response = requests.get(ALPHAVANTAGE_URL, params=params)
    data = response.json()

    if 'Time Series (60min)' in data:
        time_series = data['Time Series (60min)']
        timestamps = list(time_series.keys())
        close_price_yesterday = float(time_series[timestamps[0]]['4. close'])
        close_price_day_before_yesterday = float(time_series[timestamps[1]]['4. close'])

        price_change_percent = round((close_price_yesterday - close_price_day_before_yesterday) / close_price_day_before_yesterday * 100, 2)

        if abs(price_change_percent) >= 5:
            news_params = {
                'q': COMPANY_NAME,
                'apiKey': NEWSAPI_API_KEY
            }

            news_response = requests.get(NEWSAPI_URL, params=news_params)
            news_data = news_response.json()

            if news_response.status_code == 200:
                articles = news_data['articles'][:3]
                message = f"{STOCK}: {'🔺' if price_change_percent > 0 else '🔻'}{abs(price_change_percent)}%\n\n"

                for article in articles:
                    title = article['title']
                    description = article['description']
                    message += f"Title: {title}\n"
                    message += f"Description: {description}\n"
                    message += "-------------------------\n"

                client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

                message = client.messages.create(
                    body=message,
                    from_=TWILIO_PHONE_NUMBER,
                    to=RECIPIENT_PHONE_NUMBER
                )

                messagebox.showinfo("Success", "Message sent successfully!")
            else:
                messagebox.showerror("Error", "An error occurred while fetching news articles.")
        else:
            messagebox.showinfo("No Change", "No significant price change.")
    else:
        messagebox.showinfo("No Data", "No data available.")

window = tk.Tk()
window.title("Stock News Alert")
window.geometry("300x200")

button = tk.Button(window, text="Send Message", command=send_message)
button.pack(pady=50)

window.mainloop()
