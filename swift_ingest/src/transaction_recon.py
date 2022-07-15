from heapq import heappush
import itertools

def count_transactions(transactions):
    """
    get a count of transactions of a given value
    returns a dictionary in the format:

    {
        amount: count,
        amount: count
    }
    """
    di = {}
    for transaction in transactions:
        amount = transaction["amount"]
        count = transaction["count"]
        di[amount] = di.get(amount, 0) + count

    return di

def one_to_one(ledger, swift):
    """
    finds and reconciles one to one matching transactions 
    returns outstanding unreconciled ledger and swift transactions
    """
    # process data
    ledger_count = count_transactions(ledger)
    swift_count = count_transactions(swift)

    # handle 1:1 matches
    reconciled = []
    for amount in swift_count.keys():
        if amount in ledger_count:
            count = min(ledger_count[amount], swift_count[amount])
            reconciled.append({
                "amount": amount,
                "count": count
            })
            ledger_count[amount] -= count
            swift_count[amount] -= count

    return reconciled, ledger_count, swift_count

def dict_to_sorted_list(di):
    """
    converts a dictionary of counts to a sorted list
    for example, given {1:1, 2:2, 3:3}, outputs [1, 2, 2, 3, 3, 3]
    """
    heap = []
    for key in di.keys():
        for _ in range(di[key]):
            heappush(heap, key)
    return heap

def subset_sum(li):
    """gets all possible combinations and sums thereof given a list of numbers"""
    sums = set()
    combis = set()
    for l in range(0, len(li) + 1):
        for subset in itertools.combinations(li, l):
            subset_list = list(subset)
            sums.add(sum(subset_list))
            combis.add((sum(subset_list), subset))
    return sums, combis

def find_combi(sum, combi):
    """finds a combination with a given sum"""
    for i in combi:
        if i[0] == sum:
            return i[1]

def many_to_many(ledger_count, swift_count):
    """finds and reconciles many to many matching transactions"""
    # calculate all sums and combinations of transactions
    ledger_list = dict_to_sorted_list(ledger_count)
    swift_list = dict_to_sorted_list(swift_count)
    ledger_sums, ledger_combis = subset_sum(ledger_list)
    swift_sums, swift_combis = subset_sum(swift_list)

    # find maximum sum and combination for reconciliation
    max_sum = max(ledger_sums.intersection(swift_sums))
    ledger_recon = find_combi(max_sum, ledger_combis)
    reconciled = []
    for amount in ledger_recon:
        reconciled.append({
            "amount": amount,
            "count": 1
        })
    return reconciled