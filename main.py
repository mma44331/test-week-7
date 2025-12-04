import pandas as pd
from utils import *

pats = 'orders_simple.json'





def main():
    data = read_file(pats)
    data = change_typse_colmuns(data)
    data = clean_html(data)
    data = empty_value(data)
    data = order_month(data)
    data = high_value_order(data)
    data = avg(data)
    data = delete_colmun(data)
    data = delivery_status(data)
    data.to_csv('clean_orders_315292904')




if __name__ == '__main__':
    main()