import csv

def get_multiplier():
    prices = []
    with open('menu.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) >= 2:
                price = float(row[1])
                prices.append(price)
    return prices

# Call the function and print the prices
price_array = get_multiplier()
for price in price_array:
    print(price)