"""Set up all main constants on the module."""

endpoints = {
    'test' : '/api/v3/ping',
    'server_time' : '/api/v3/time',
    'exchange_info' : '/api/v3/exchangeInfo',
    'order_book' : '/api/v3/depth',
    'candlestick' : '/api/v3/klines',
    'avg_price' : '/api/v3/avgPrice',
    'best_price' : '/api/v3/ticker/bookTicker',
    'acc_info' : '/api/v3/account',
    'acc_snapshot' : '/sapi/v1/accountSnapshot',
    'price' : '/api/v3/ticker/price',
    'price_hist' : '/api/v3/historicalTrades',
    'order' : '/api/v3/order',
    'test_order' : '/api/v3/order/test',
    'trades' : '/api/v3/myTrades',
    'options_info' : '/vapi/v1/optionInfo',
    'options_order_book' : '/vapi/v1/depth',
    'options_mark_price' : '/vapi/v1/mark',
}