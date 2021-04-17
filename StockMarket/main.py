import csv

ticker = "AAPL"
date_purchased = "04/18/2016"
date_sold = "04/17/2020"

def main():
    with open(f'assets/{ticker}.csv', 'r') as csv_file:
        csv_file = csv.DictReader(csv_file)
        sale_price = find_value(csv_file, date_sold)
        purchase_price = find_value(csv_file, date_purchased)
        profit = sale_price - purchase_price
        print()
        print(f"If you would have purchased {ticker} on {date_purchased} and sold on {date_sold},"
              f" then your profit would be ${profit} per share")


def remove_dollar(dollar_value):
    value = dollar_value.replace('$', '')
    return float(value)


def find_value(csv_file, action_date):
    for row in csv_file:
        day = row['Date']
        if day == action_date:
            high_num = remove_dollar(row["High"])
            low_num = remove_dollar(row["Low"])
            return float(((high_num + low_num) / 2))


if __name__ == '__main__':
    main()

