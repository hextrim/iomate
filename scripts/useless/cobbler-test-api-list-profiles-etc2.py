import os

stocks = [{ 'IBM': 146.48, 'MSFT':44.11, 'CSTO':25.54 }, { 'IBM': 32.48, 'MSFT':99.11, 'CSTO':11.54 }]
#print out all the keys
for c in stocks:
    print c['IBM']

#print key n values
#for k, v in stocks.items():
#    print("Code : {0}, Value : {1}".format(k, v))
