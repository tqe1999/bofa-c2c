import inflection
import pandas as pd
import sys

from lib.models import db

# get command line args
try:
    input_file = sys.argv[1]
    data_type = sys.argv[2]
except:
    print("please specify an input file and data type (ledger_transactions or ledger_balance)")

# read csv to dataframe, add reconciled status
df = pd.read_csv(input_file)

# set data type for date columns
if data_type == "ledger_transactions":
    # tag all transactions with the same transaction reference
    df["TransactionReference"] = df["TransactionReference"][0]
    df["ValueDate"] = pd.to_datetime(df["ValueDate"])
elif data_type == "ledger_balance":
    df["AsOfDateTS"] = pd.to_datetime(df["AsOfDateTS"])

# set all values unreconciled by default
df["reconciled"] = False

# convert from CamelCase to snake_case for SQL column names
df.columns = [inflection.underscore(x) for x in df.columns]

# load dataframe to SQL
df.to_sql(data_type, con=db, index=True, if_exists="append")
