from sqlalchemy import select
from lib.models import db, ledger_transactions

def get_ledger_transactions(account_id, txn_ref):
    """
    get a list of ledger transactions, in the format

    [
        {
            "amount": double,
            "date": DateTime,
            "credit_debit": string,
            "count": 1
        }
    ]
    """
    # select matching transactions
    select_transactions = select(ledger_transactions).where(
        ledger_transactions.c.account == account_id
        and ledger_transactions.c.transaction_reference == txn_ref
    )

    # parse result to list
    transaction_list = []
    with db.begin() as conn:
        for row in conn.execute(select_transactions):
            transaction_list.append({
            "amount": dict(row)["amount"],
            "date": dict(row)["value_date"],
            "credit_debit": dict(row)["credit_debit"],
            "count": 1
        })

    return transaction_list

def set_transaction_recon(account_id, txn_ref, amount, count):
    """set a given number of transactions as reconciled, given account id, transaction reference, and amount"""
    stmt = f'''
            UPDATE ledger_transactions SET "reconciled"=true
            WHERE "account"='{account_id}'
            AND "transaction_reference"='{txn_ref}'
            AND "amount"={amount} AND "reconciled"=false
            AND "index" in (
                SELECT "index" FROM ledger_transactions
                WHERE "account"='{account_id}'
                AND "transaction_reference"='{txn_ref}'
                AND "amount"={amount} AND "reconciled"=false
                ORDER BY "index" ASC LIMIT {count}
            );
            '''
    with db.begin() as conn:
        res = conn.execute(stmt)