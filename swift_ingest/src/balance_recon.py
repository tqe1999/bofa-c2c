def pair_balances(balances, account_id):
    """
    match pairs of balances to get the open and close amounts for a given date
    adds account id and currency
    returns a dictionary in the format:

    { 
        DateTime: {
            "account": string,
            "currency": string,
            "open": double,
            "close": double
        }
    }
    """
    balances_dict = {}
    for balance in balances:
        date = balance["date"]
        balances_dict.setdefault(date, {
            "account": account_id,
            "currency": balance["currency"]
        })
        if balance["code"] == "OPBD":
            balances_dict[date]["open"] = balance["amount"]
        elif balance["code"] == "CLBD":
            balances_dict[date]["close"] = balance["amount"]
    return balances_dict

def get_transaction_delta(date, transactions):
    """finds total change in balance caused by transactions on a given date"""
    delta = 0
    for transaction in transactions:
        if transaction["date"] == date:
            if transaction["credit_debit"] == "CRDT":
                credit_debit = 1
            elif transaction["credit_debit"] == "DBIT":
                credit_debit = -1
            delta += transaction["amount"] * transaction["count"] * credit_debit
    return delta

def check_balances(balances, transactions):
    """
    annotate balances with day on day differences, outstanding unexplained differences if any, and reconciliation status
    returns values in a dictionary in the format:

    { 
        DateTime: {
            "account": string,
            "currency": string,
            "open": double,
            "close": double
            "difference": double,
            "outstanding": double,
            "reconciled": boolean
        }
    }
    """
    for date in balances.keys():
        pair = balances[date]
        balance_delta = pair["close"] - pair["open"]
        transaction_delta = get_transaction_delta(date, transactions)
        outstanding = balance_delta - transaction_delta
        pair["difference"] = balance_delta
        pair["outstanding"] = outstanding
        pair["reconciled"] = outstanding == 0
    return balances
    
def swift_recon(balances, transactions, account_id):
    """
    perform reconciliation for swift balances and transactions for a given account id
    returns checked balances in the format: 

    { 
        DateTime: {
            "account": string,
            "currency": string,
            "open": double,
            "close": double
            "difference": double,
            "outstanding": double,
            "reconciled": boolean
        }
    }
    """
    paired_balances = pair_balances(balances, account_id)
    checked_balances = check_balances(paired_balances, transactions)

    return checked_balances
