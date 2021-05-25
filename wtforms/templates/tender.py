from web3 import Web3 as wb
import json

f=open('abi.json','r')
url='http://127.0.0.1:8545'
w3=wb(wb.HTTPProvider(url))

t_add='0x1C0D9E5B28C2Aa369114A4dE7fa6d8Ee27C611F4'

add=w3.toChecksumAddress(t_add)
abi=json.loads(f.read())

contract =w3.eth.contract(address=add,abi=abi)

def showaccounts():
    li=w3.eth.get_accounts()
    return li

def hasbidbefore(address):
    data=contract.functions.hasBidBefore(address).call()
    print(data)

def placeBid(address,quote,quoteclause):
    tx={
        'to':add,
        'from':address,
    }
    data=contract.functions.placeBid(quote,quoteclause).transact(tx)
    recipt=w3.eth.getTransactionReceipt(data)
    # log=contract.events.myEvent().processReceipt(recipt)
    return recipt
    # print(log)

def bidders():
    data=contract.functions.returnbidders().call()
    print(data)

def gettender():
    data=contract.functions.get_tender().call()
    return data

def showing_bids(address):
    data=contract.functions.showingbids(address).call()
    print(data)
def Bidapproval(address,status):
    tx={
        'from':address,
        'to':add
    }

    data=contract.functions.Bidapproval(address,status).transact(tx)
    recipt=w3.eth.getTransactionReceipt(data)
    
    print(recipt)

def winner(address):
    tx={
        'from':address,
        'to':add
    }
    data=contract.functions.winner(address).transact(tx)
    recipt=w3.eth.getTransactionReceipt(data)
    print(recipt)
# hasbidbefore('0x69896e134062200Db545cEb7d0DC26513804B99E')
# /gettender()
# print(placeBid('0xe34F17F666193395c409d5d90E9dC054D3A7c72E',10,'sample'))
# Bidapproval('0xE54a67D8267d98eC77e07D57f7466ccCC6f4E7d9','approve')
# bidders()
# showing_bids('0x69896e134062200Db545cEb7d0DC26513804B99E')