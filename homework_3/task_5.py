date = [int(input ("year ")), int(input("month ")), int(input("number "))]

initial_money = int( input("enter initial amount in USD - "))
from forex_python.bitcoin import BtcConverter
b=BtcConverter()
b. get_price("USD")