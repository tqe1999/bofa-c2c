import pandas as pd
import sys

from lib.models import db
import src.sql_interface as sql
import src.xml_parse as swift_xml
import src.balance_recon as balance_recon
import src.transaction_recon as transaction_recon

# get command line args
try:
    input_file = sys.argv[1]
except:
    print("please specify an input file")

# parse xml and get report data
root = swift_xml.get_xml_root(input_file)
stmt = swift_xml.get_stmt_el(root)
account_id, txn_ref = swift_xml.get_txn_details(stmt)

# get transaction and balance data
swift_transactions = swift_xml.get_swift_transactions(stmt)
swift_balances = swift_xml.get_balance_list(stmt)
ledger_transactions = sql.get_ledger_transactions(account_id, txn_ref)

# reconcile balance
checked_balances = balance_recon.swift_recon(swift_balances, swift_transactions, account_id)
# parse dictionary into dataframe, set column header, load to sql
df = pd.DataFrame.from_dict(checked_balances, orient="index")
df["date"] = df.index
df.reset_index()
df.to_sql("swift_balances", con=db, index=False, if_exists="append")

# invalidate transactions within the time period of unreconciled balances
failed_dates = []
for date in checked_balances.keys():
    if checked_balances[date]["reconciled"] == False:
        failed_dates.append(date)

swift_transactions = [x for x in swift_transactions if not x["date"] in failed_dates]

# reconcile transactions
reconciled, ledger_count, swift_count = transaction_recon.one_to_one(ledger_transactions, swift_transactions)
reconciled.extend(transaction_recon.many_to_many(ledger_count, swift_count))

for transaction in reconciled:
    sql.set_transaction_recon(account_id, txn_ref, transaction["amount"], transaction["count"])