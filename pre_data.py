"""
@Project : code
@File    : pre_data
@Author  : XiaoBanni
@Date    : 2021-11-06 15:58
@Desc    : 
"""
import pandas as pd


def pre_groceries():
    df = pd.read_csv("Groceries.csv")
    transactions = df['items'].to_numpy()
    transactions = [sorted(i.lstrip('{').rstrip('}').split(',')) for i in transactions]
    items = set()
    for e in transactions:
        for ee in e:
            items.add(ee)
    items = sorted(list(items))
    # print("number of transactions %d, number of items %d" % (len(transactions), len(items)))
    return [transactions, items]


def pre_unix_usage():
    return None


def get_dataset(dateset_id):
    if dateset_id == 1:
        return pre_groceries()
    else:
        return pre_unix_usage()


if __name__ == '__main__':
    pre_groceries()
