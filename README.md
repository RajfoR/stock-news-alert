## Stock News Alert

Stock News Alert is a Python application that retrieves stock market data and news articles related to a specific stock and sends them as SMS messages using the Twilio API. The application uses Alpha Vantage to fetch stock data and News API to fetch news articles. It provides a simple GUI interface for sending the messages.

### Prerequisites

Before running the application, you need to have the following:

- Python 3 installed on your machine
- Twilio account credentials (Account SID and Auth Token)
- Alpha Vantage API key
- News API key

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/stock-news-alert.git
   ```

2. Navigate to the project directory:

   ```
   cd stock-news-alert
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Open the `main.py` file and replace the following placeholders with your own credentials:

   - `YOUR_NEWSAPI_API_KEY`: Replace with your News API key.
   - `YOUR_TWILIO_ACCOUNT_SID`: Replace with your Twilio account SID.
   - `YOUR_TWILIO_AUTH_TOKEN`: Replace with your Twilio auth token.
   - `YOUR_TWILIO_PHONE_NUMBER`: Replace with your Twilio phone number.
   - `YOUR_RECIPIENT_PHONE_NUMBER`: Replace with the recipient's phone number.

### Usage

To run the application, execute the following command:

```
python main.py
```

This will launch the GUI window.

1. Click the "Send Message" button to trigger the stock data and news retrieval process.

2. If the percentage change in the stock price is greater than or equal to 5%, the application will fetch the top 3 news articles related to the stock and send them as an SMS message.

3. A success or error message will be displayed in a dialog box.

### License

This project is licensed under the MIT License.

### Acknowledgments

- The application uses the Alpha Vantage API to retrieve stock market data. Visit [Alpha Vantage](https://www.alphavantage.co/) for more information.
- The application uses the News API to fetch news articles. Visit [News API](https://newsapi.org/) for more information.
- The application utilizes the Twilio API for sending SMS messages. Visit [Twilio](https://www.twilio.com/) for more information.
