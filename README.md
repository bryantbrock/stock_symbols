# Stock Symbols
#### Access every stock Symbol (or Ticker) available on the stock market.
A small Python function to fetch all stock symbols (and last price) for public use. It mocks the Nasdaq.com network requests and provides filter documentation for easier use.

### Motivation
This small function and request has proved immensly useful while building stock market trading strategies. I would want to not just test specific tickers/symbols, I wanted to test any that were in a given price range, and as many as possible to test my strategy. With this simple function, you can provide a `screener` function that will help you filter out results on a price basis as well. See the documentation below for more information. I couldn't find anything like this when I browsed the web (I know fintech is a pretty closed book), so here is a smaller helper in your journey.

### Contributions
All contributions welcome!

## Documentation
There is only one function available, `get_symbols`. If you see the code, it is less than 100 lines long, and is simply coopying a network request made the nasdaq api.

`getSymbol(**args)`: accepts a number of optional arguments and returns a Python list of dictionaries. No arguments are required.

### Arguments
As noted above, none are required - all are optional.

| argument | type | options |
| --- | --- | --- |
| limit | number | A number between 0 - infinity. Note: the higher the number, the longer the request. Make use of the `offset` for performance if an option. |
| offset | number | To paginate symbols and make sure you get all of them. Symbols are ranked by `marketcap`.
| exchange | list | Options: `nyse`, `
