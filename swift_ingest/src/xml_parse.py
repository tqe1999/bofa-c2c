from datetime import datetime
import xml.etree.ElementTree as ET

from numpy import double

# set swift xml namespace
ns = {"": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.08"}

def get_xml_root(file_name):
    """read xml file and get its root"""
    tree = ET.parse(file_name)
    root = tree.getroot()
    return root

def get_stmt_el(root):
    """get statement element from swift xml root"""
    stmt = root.find("BkToCstmrStmt/Stmt", namespaces=ns)
    return stmt

def get_txn_details(stmt):
    """get account id and transaction reference for a statement"""
    acct_id = stmt.find("Acct/Id/Othr/Id", namespaces=ns).text
    tx_ref = stmt.find("Ntry/NtryDtls/TxDtls/Refs/EndToEndId", namespaces=ns).text
    return acct_id, tx_ref

def get_swift_transactions(stmt):
    """
    get a list of swift transactions, in the format

    [
        {
            "amount": double,
            "date": DateTime,
            "credit_debit": string,
            "count": int
        }
    ]
    """
    transaction_list = []

    # find and iterate through all transaction entries
    transaction_entries = stmt.findall("Ntry", namespaces=ns)
    for entry in transaction_entries:
        # get transaction values
        amount_element = entry.find("Amt", namespaces=ns)
        amount = float(amount_element.text)
        date_element = entry.find("ValDt/Dt", namespaces=ns)
        date =  datetime.strptime(date_element.text, "%Y-%m-%d")
        credit_debit_element = entry.find("CdtDbtInd", namespaces=ns)
        credit_debit = credit_debit_element.text
        
        # check if batch transaction and set count accordingly
        if entry.find("NtryDtls/Btch", namespaces=ns) is not None:
            count_element = entry.find("NtryDtls/Btch/NbOfTxs", namespaces=ns)
            count = int(count_element.text)
        else:
            count = 1

        transaction_list.append({
            "amount": amount,
            "date": date,
            "credit_debit": credit_debit,
            "count": count
        })

    return transaction_list

def get_balance_list(stmt):
    """
    get a list of swift balances, in the format

    [
        {
            "amount": double,
            "date": DateTime,
            "code": string,
            "currency": string
        }
    ]
    """
    balance_list = []

    # find and iterate through all balances
    balances = stmt.findall("Bal", namespaces=ns)
    for balance in balances:
        # get balance values
        amount_element = balance.find("Amt", namespaces=ns)
        amount = float(amount_element.text)
        currency = amount_element.get('Ccy')
        date_element = balance.find("Dt/Dt", namespaces=ns)
        date = datetime.strptime(date_element.text, "%Y-%m-%d")
        code_element = balance.find("Tp/CdOrPrtry/Cd", namespaces=ns)
        code = code_element.text
        balance_list.append({
            "amount": amount,
            "date": date,
            "code": code,
            "currency": currency
        })
        
    return balance_list