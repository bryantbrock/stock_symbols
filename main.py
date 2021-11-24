import requests

def get_symbols(
  limit=100,
  offset=0, 
  exchanges=['nyse'],
  marketcap='small',
  region='north_america',
  screener=lambda x: True,
  sector=None,
  country=None,
  recommendations=[],
  exchange_sub_categories={},
):

  result = []

  headers = {
    'authority': 'api.nasdaq.com',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    'origin': 'https://www.nasdaq.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.nasdaq.com/',
    'accept-language': 'en-US,en;q=0.9',
  }

  filters = {
    'tableonly': False,
    'limit': limit,
    'offset': offset,
    'marketcap': marketcap,
    'recommendation': recommendations,
  }

  for exchange in exchanges:
    if exchange_sub_categories[exchange]:
      filters['exsubcategory'] = exchange_sub_category

    res = requests.get(
      'https://api.nasdaq.com/api/screener/stocks', headers=headers, params=params
    ).json()

    for ticker in res['data']['table']['rows']:
      # Fix small bug
      if ticker['pctchange'][-1] != '%':
        ticker['pctchange'] = '0.0%'

      ticker['exchange'] = exchange
      ticker['symbol'] = ticker['symbol'].split(' ')[0]
      ticker['lastsale'] = float(ticker['lastsale'][1:])
      ticker['pctchange'] = float(ticker['pctchange'][:-2])/100

      passed = screener(ticker)

      if passed:
        result.append(ticker)


  return result
