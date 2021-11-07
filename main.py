"""
@Project : code
@File    : main.py
@Author  : XiaoBanni
@Date    : 2021-11-06 15:41
@Desc    : 
"""

from utils import get_args, count_memory
from pre_data import get_dataset
from baseline import run_baseline
from apriori import run_apriori
from fp_growth import run_fp_growth


@count_memory
def main():
    args = get_args()
    dataset = get_dataset(args.dataset)
    args.data_size = len(dataset[0])
    if args.alg == "baseline":
        frequent_itemsets = run_baseline(dataset, args)
    elif args.alg == "apriori":
        frequent_itemsets = run_apriori(dataset, args)
    else:
        frequent_itemsets = run_fp_growth(dataset, args)
    print(len(frequent_itemsets))


if __name__ == "__main__":
    main()
