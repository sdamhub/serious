"""
1. create a dictionary from the list
with the date as key and the count of each product
e.g
2019-12-29: {soda: 1, popcorn: 1}

2. Iterate over the dict and calculate the amount
owed for each day

3. return the result

"""
prices = {
    'bundle': 9,
    'popcorn': 7,
    'soda': 2.50
}


def convert_list(tab):  # aggregate product counts for each day
    daily_record = dict()
    for each_item in tab:
        date, product = each_item.split(",")
        if not daily_record.get(date):
            daily_record[date] = {"soda": 0, "popcorn": 0}
        daily_record[date][product] = daily_record[date][product] + 1
    return daily_record


def tally(tab):
    daily_record = convert_list(tab)  # O(N)
    amount_owed = 0
    for _, each_day in daily_record.items():  # O(N)
        if each_day['soda'] > 0 and each_day[
            'popcorn'] > 0:  # Bundle is actually the minimum of the product count for each day. It's ok if they are the same
            bundle = min(each_day['soda'], each_day['popcorn'])
            soda = 0
            popcorn = 0
            # Subtracting the highest product count from bundle
            if each_day['soda'] > each_day['popcorn']:
                soda = each_day['soda'] - bundle
            else:
                popcorn = each_day['popcorn'] - bundle
            amount_owed += (bundle * prices['bundle']) + prices['popcorn'] * popcorn + (prices['soda'] * soda)
        else:
            amount_owed += prices['soda'] * each_day['soda'] + prices['popcorn'] * each_day['popcorn']

    return amount_owed


if __name__ == "__main__":
    print(tally([
        "2021-11-15,popcorn",
        "2021-11-16,popcorn",
        "2021-11-17,soda",
        "2021-11-17,soda",
        "2021-11-15,soda",
        "2021-11-15,popcorn",
    ]))