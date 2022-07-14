import datetime
from src.balance_recon import *

date1 = datetime.date(2022, 7, 1)
date2 = datetime.date(2022, 7, 2)
balances = [ {
    "date": date1,
    "code": "OPBD",
    "amount": 100,
    "currency": "SGD"
}, {
    "date": date1,
    "code": "CLBD",
    "amount": 150,
    "currency": "SGD"
}, {
    "date": date2,
    "code": "OPBD",
    "amount": 150,
    "currency": "SGD"
}, {
    "date": date2,
    "code": "CLBD",
    "amount": 125,
    "currency": "SGD"
}]

account = "user"

paired_balances = {
    date1: {
        "account": "user",
        "currency": "SGD",
        "open": 100,
        "close": 150
    }, date2: {
        "account": "user",
        "currency": "SGD",
        "open": 150,
        "close": 125
    }
}

transactions = [ {
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

checked_balances = {
    date1: {
        "account": "user",
        "currency": "SGD",
        "open": 100,
        "close": 150,
        "difference": 50,
        "outstanding": 0,
        "reconciled": True
    }, date2: {
        "account": "user",
        "currency": "SGD",
        "open": 150,
        "close": 125,
        "difference": -25,
        "outstanding": -15,
        "reconciled": False
    }
}

def test_pair_balances():
    assert pair_balances(balances, account) == paired_balances

def test_check_balances():
    assert check_balances(paired_balances, transactions) == checked_balances