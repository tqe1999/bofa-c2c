import pandas as pd
import sys

from lib.models import db

# get command line args
input_file = sys.argv[1]
data_type = sys.argv[2]

# read csv to dataframe, add reconciled status
df = pd.read_csv(input_file)
df["reconciled"] = False

df.to_sql(data_type, con=db, index=False, if_exists="append")
