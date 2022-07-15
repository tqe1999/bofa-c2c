import datetime
from src.transaction_recon import *

date1 = datetime.date(2022, 7, 1)
date2 = datetime.date(2022, 7, 2)

ledger_transactions = [ {
    "amount": 10,
    "date": date1,
    "credit_debit": "DBIT",
    "count": 1
}, {
    "amount": 20,
    "date": date1,
    "credit_debit": "CRDT",
    "count": 3
}, {
    "amount": 20,
    "date": date2,
    "credit_debit": "CRDT",
    "count": 1
}, {
    "amount": 15,
    "date": date2,
    "credit_debit": "DBIT",
    "count": 2
} ]

ledger_count = {
    10: 0,
    20: 0,
    15: 2
}

swift_transactions = [ {
    "amount": 10,
    "date": date1,
    "credit_debit": "DBIT",
    "count": 1
}, {
    "amount": 20,
    "date": date1,
    "credit_debit": "CRDT",
    "count": 3
}, {
    "amount": 20,
    "date": date2,
    "credit_debit": "CRDT",
    "count": 1
}, {
    "amount": 10,
    "date": date2,
    "credit_debit": "DBIT",
    "count": 3
} ]

swift_count = {
    10: 3,
    20: 0
}

def test_one_to_one():
    reconciled, ledger_count_test, swift_count_test = one_to_one(ledger_transactions, swift_transactions) 
    assert ledger_count_test == ledger_count
    assert swift_count_test == swift_count

def test_subset_sum():
    sums, combis = subset_sum([1,2,3,4])
    assert sums == set([0,1,2,3,4,5,6,7,8,9,10])

    sums, combis = subset_sum([1,1,4])
    assert sums == set([0,1,2,4,5,6])

    sums, combis = subset_sum([])
    assert sums == set([0])