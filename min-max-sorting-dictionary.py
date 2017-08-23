#create a dictnary
stocks = {
    'GOOG' : 76.7,
    'FB' : 50.45,
    'YHOO' : 79.3,
    'AMZN' : 99.98,
    'AAPL' : 99.99
}
#u can not sort a dictionary but u can sort a zipped

#sorting by zipping the shit
print(sorted(zip(stocks.values(), stocks.keys())))

#sorting using zip function, by stock values and the min price
print(min(zip(stocks.values(), stocks.keys())))

#again max
print(max(zip(stocks.values(), stocks.keys())))
