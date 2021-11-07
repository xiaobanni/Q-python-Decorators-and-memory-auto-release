"""
@Project : code
@File    : apriori
@Author  : XiaoBanni
@Date    : 2021-11-06 16:31
@Desc    : 
"""
import itertools
from utils import count_memory


def has_infrequent_subset(candidate, k_frequent_itemsets):
    """
    Determine whether all the size_k subsets of size_{k+1} candidate  are in k_frequent_itemsets
    :param candidate: list, include k+1 string
    :param k_frequent_itemsets: list(list): sets of all size_k frequent itemsets
    :return:
    """
    length = len(candidate)
    for subset in itertools.combinations(candidate, length - 1):  # return type: list(tuple)
        if subset not in k_frequent_itemsets:
            return True
    return False


def judge_equal(list1, list2):
    """
    Determine whether the elements of two equal-length ordered arrays except the last element are equal
    :param list1: include k string
    :param list2: include k string
    :return:
    """
    length = len(list1)
    for i in range(length - 1):
        if list1[i] != list2[i]:
            return False
    return True


def apriori_gen(k_frequent_itemsets):
    """
    Generate candidate frequent (k+1) itemset
    :param k_frequent_itemsets: list(tuple), each itemset include k items(string)
    :return: list(tuple), each candidate itemset include k+1 items(string)
    """
    candidate_frequents_itemsets = []
    for i in range(len(k_frequent_itemsets)):
        for j in range(i + 1, len(k_frequent_itemsets)):
            if judge_equal(k_frequent_itemsets[i], k_frequent_itemsets[j]):
                candidate = k_frequent_itemsets[i] + tuple([k_frequent_itemsets[j][-1]])
                if has_infrequent_subset(candidate, k_frequent_itemsets) is False:
                    candidate_frequents_itemsets.append(candidate)
    return candidate_frequents_itemsets


def find_one_frequent_itemset(dataset, args):
    """

    :param dataset: [list(list),list(string)], [transactions, items], each transaction and items are ordered
    :param args:
    :return: list(tuple), one_itemsets
    """
    transactions, items = dataset
    one_itemsets = dict.fromkeys(items, 0)
    for transaction in transactions:
        for item in items:
            if item in transaction:
                one_itemsets[item] += 1
    ret_one_itemsets = []
    for k, v in one_itemsets.items():
        if 1.0 * v / args.data_size >= args.support:
            ret_one_itemsets.append(tuple([k]))
    return ret_one_itemsets


def get_frequent_itemsets(dataset, args):
    """

    :param dataset: [list,set], [transactions, items], each transaction and items are ordered
    :param args:
    :return: [tuple], all frequent itemsets
    """
    all_frequent_itemsets = []
    k_frequent_itemsets = find_one_frequent_itemset(dataset, args)
    length = 1
    while True:
        if len(k_frequent_itemsets) <= 0:
            break
        length += 1
        all_frequent_itemsets.extend(k_frequent_itemsets)
        # print(all_frequent_itemsets, len(all_frequent_itemsets))
        k_plus_candidate_frequent_itemsets = apriori_gen(k_frequent_itemsets)
        k_plus_candidate_frequent_itemsets_dict = dict.fromkeys(k_plus_candidate_frequent_itemsets, 0)
        for transaction in dataset[0]:
            for subset in itertools.combinations(transaction, length):
                if subset in k_plus_candidate_frequent_itemsets_dict:
                    k_plus_candidate_frequent_itemsets_dict[subset] += 1
        k_frequent_itemsets = []
        for k, v in k_plus_candidate_frequent_itemsets_dict.items():
            if 1.0 * v / args.data_size >= args.support:
                k_frequent_itemsets.append(k)
    return all_frequent_itemsets


def run_apriori(dataset, args):
    return get_frequent_itemsets(dataset, args)


@count_memory
def main():
    from pre_data import pre_groceries
    from utils import get_args

    args = get_args()
    dataset = pre_groceries()
    args.data_size = len(dataset[0])
    frequent_itemsets = run_apriori(dataset, args)
    print(len(frequent_itemsets))


if __name__ == '__main__':
    main()
