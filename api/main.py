from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import select

from lib.models import db, ledger_transactions, swift_balances

app = Flask(__name__)

# enable cors from all sources
CORS(app)

# get all transactions
@app.route('/transaction/all', methods=['GET'])
def get_all_transactions():
    stmt = select(ledger_transactions)
    with db.begin() as conn:
        res = []
        for row in conn.execute(stmt):
            res.append(row)
    return jsonify({'transactions': [dict(row) for row in res]})

# get all balances
@app.route('/balance/all', methods=['GET'])
def get_all_balances():
    stmt = select(swift_balances)
    with db.begin() as conn:
        res = []
        for row in conn.execute(stmt):
            res.append(row)
    return jsonify({'balances': [dict(row) for row in res]})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)