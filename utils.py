import pandas as df


def read_file(pats):
    file_json = df.read_json(pats)
    return file_json


def change_typse_colmuns(file_json):
    file_json['total_amount'] = file_json['total_amount'].str.replace('$', ' ').astype(float)
    file_json['shipping_days'] = file_json['shipping_days'].astype(int)
    file_json['customer_age'] = file_json['customer_age'].astype(int)
    file_json['rating'] = file_json['rating'].astype(float)
    file_json['order_date'] = df.to_datetime(file_json.order_date)
    return file_json


def clean_html(file_json):
    file_json['items_html'] = file_json['items_html'].str.replace(r'<[^<>]*>', ' ', regex=True)
    return file_json


def empty_value(file_json):
    file_json['coupon_used'] = file_json['coupon_used'].replace("", "no coupon")
    return file_json


def order_month(file_json):
    file_json['order_date'] = df.to_datetime(file_json['order_date'])
    file_json['order_month'] = file_json['order_date'].dt.month
    return file_json


def high_value_order(file_json):
    file_json['high_value_order'] = (file_json['total_amount'] > file_json.total_amount.mean())
    file_json = file_json.sort_values(by='total_amount', ascending=False)
    return file_json


def avg(file_json):
    df = file_json.groupby(file_json.country).agg(rating_avg=('rating', 'mean')).reset_index()
    file_json = file_json.merge(df, on='country')
    return file_json


def delete_colmun(file_json):
    file_json = file_json[(file_json['total_amount'] > 1000) & (file_json['rating'] > 4.5)]
    return file_json


def delivery_status(file_json):
    file_json['delivery_status'] = file_json['shipping_days'].apply(
        lambda value: 'delayed' if value > 1000 else 'on time')
    return file_json






