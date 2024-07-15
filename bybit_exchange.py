from pybit.unified_trading import HTTP

def get_futures_name()->list:

    """Возвращает имена всех не эксперировавашихся срочных фьючерсов с биржи Байбит"""
    session = HTTP(testnet=True)
    all_tickers = (session.get_tickers(
        category="linear"
    ))
    
    dict_list = all_tickers.get('result').get('list')
    futures_ticker_list = []

    for dic in dict_list:
        ticker = dic.get('symbol')
        if ('-' in ticker):
            futures_ticker_list.append(ticker)

    return futures_ticker_list
    
