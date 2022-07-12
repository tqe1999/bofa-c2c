import os
from sqlalchemy import create_engine, MetaData, Table, Column, Boolean, Float, Integer, String

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
    Column('Account', String(48), primary_key=True),
    Column('Currency', String(10)),
    Column('Balance', Float),
    Column('AsOfDateTS', String(48)),
    Column('reconciled', Boolean)
)

ledger_transactions = Table(
    'ledger_transactions',
    metadata,
    Column('Account', String(48), primary_key=True),
    Column('ValueDate', String(10)),
    Column('Currency', String(3)),
    Column('CreditDebit', String(6)),
    Column('Amount', Integer),
    Column('TransactionReference', String(48)),
    Column('reconciled', Boolean)
)
    