from alpaca_trade_api.rest import REST, TimeFrame

api = REST()

# --------------- Iterate Over Bars ---------------
# def process_bar(bar):
#     # process bar
#     print(bar)
#
#
# bar_iter = api.get_bars_iter("AAPL", TimeFrame.Hour, "2021-06-08", "2021-06-08", adjustment='raw')
# for bar in bar_iter:
#     process_bar(bar)

# --------------- Get All Bars Once ---------------
bars = api.get_bars("AAPL", TimeFrame.Hour, "2022-05-10", "2022-05-10", adjustment='raw').df
print(bars)