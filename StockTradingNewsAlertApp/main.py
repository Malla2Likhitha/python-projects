import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = '4LB3NGD5ICTJF3LR'
stock_api_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY
}
stock_response = requests.get(url='https://www.alphavantage.co/query', params=stock_api_parameters)
stock_response.raise_for_status()
day_2_closing_price = float(stock_response.json()['Time Series (Daily)']['2024-05-31']['4. close'])
day_1_closing_price = float(stock_response.json()['Time Series (Daily)']['2024-05-30']['4. close'])
change = day_2_closing_price - day_1_closing_price
change_per = abs(change) / day_2_closing_price * 100
if change_per >= 5:
    # print('Get News!')
    news_api_parameters = {
        'q': COMPANY_NAME,
        'sortBy': 'relevancy',
        'apiKey': 'f0821fd98f7148c0a38737d4fddda398',
        'language': 'en'
    }
    news_response = requests.get(url='https://newsapi.org/v2/everything', params=news_api_parameters)
    news_response.raise_for_status()
    articles = news_response.json()['articles']
    news_dict = [{'Headline': articles[i]['title'], 'Brief': articles[i]['description']} for i in range(3)]

    account_sid = 'AC3245e55cd725b448d6a1c19d84d40382'
    auth_token = '719e7381f7c6bc7329682b7864fd5009'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f"TSLA: {'🔺' if change > 0 else '🔻'}{change_per}%"
             f"\n\nHeadline: {news_dict[0]['Headline']}\nBrief: {news_dict[0]['Brief']}"
             f"\n\nHeadline: {news_dict[1]['Headline']}\nBrief: {news_dict[1]['Brief']}"
             f"\n\nHeadline: {news_dict[2]['Headline']}\nBrief: {news_dict[2]['Brief']}",
        to='whatsapp:+918332047072'
    )
    print(message.status)

