import os
from sqlalchemy import create_engine, MetaData, Table, Column, Boolean, Float, String, DateTime

# get environment variables
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")

# database connection
conn_str = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/postgres"
)
db = create_engine(conn_str)
metadata = MetaData()

# define tables
ledger_balance = Table(
    'ledger_balance',
    metadata,
    Column('account', String(48), primary_key=True),
    Column('currency', String(10)),
    Column('balance', Float),
    Column('as_of_date_ts', DateTime),
    Column('reconciled', Boolean)
)

ledger_transactions = Table(
    'ledger_transactions',
    metadata,
    Column('account', String(48), primary_key=True),
    Column('value_date', DateTime),
    Column('currency', String(3)),
    Column('credit_debit', String(6)),
    Column('amount', Float),
    Column('transaction_reference', String(48)),
    Column('reconciled', Boolean)
)

swift_balances = Table(
    'swift_balances',
    metadata,
    Column('account', String(48), primary_key=True),
    Column('currency', String(3)),
    Column('open', Float),
    Column('close', Float),
    Column('difference', Float),
    Column('outstanding', Float),
    Column('date', DateTime),
    Column('reconciled', Boolean)
)
    