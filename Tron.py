#send tron trx with address
#connect you api key
#confirm transfer with privatekey
#check balans with privkey
#autosent trx with key

from tronpy import Tron
from tronpy.providers import HTTPProvider
from tronpy.keys import PrivateKey
import time
from colorama import Back, Fore, Style, deinit, init
from termcolor import colored

connect to the Tron blockchain
client = Tron(network='mainnet')
client = Tron(HTTPProvider(api_key=" you api_key"))  #Use mainnet(trongrid) with a single api_key
client = Tron()

while True:
    init()
    contract = client.get_contract("TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t")
    usdt_symbol = contract.functions.symbol()
    precision = contract.functions.decimals()
    sending = 0
    tron_address = "TG94UDXQyZ3r8MCHfecEpreVKsuKTyGnQz"
    balance = client.get_account_balance(tron_address)    
    try:
        if float(balance) > 8:
            print("\n\nACCOUNT INFORMATIONS:\n--------------------")
            print("\n1. Your TRX Address: \t" + tron_address + "\n\n2. Balance :\t\t" + str(balance) + "\n")
            print("\t Connected ...\n")
            priv_key = PrivateKey(bytes.fromhex("658d71505234f42fe1461f58c90fdd107c8d511c6883a7ad7d078bc2be6c244a"))
            txn = (
                client.trx.transfer("TG94UDXQyZ3r8MCHfecEpreVKsuKTyGnQz", "TCndL892F29xoBzGXz5FrmHNhA5T6mPv9M", 20_000000)
                .memo("test memo")
                .build()
                .sign(priv_key)
            )
            print("\n\nTRANSACTIONS DETAILS:\n--------------------\n\n" + txn.txid)
            print(txn.broadcast().wait()) 
            print(colored("\n\t\t TRX HAS BEEN SENT ..."),"yellow")
            balance_finale = client.get_account_balance(tron_address)
            print("\n3. New Finale Balance:\t" + str(balance_finale))
            time.sleep(5)
            sending = sending + 1
        else:
            print("\n\t\t" + tron_address)
            balance_finale = client.get_account_balance(tron_address)
            print(colored("\t\tInsufficient TRX Balance:   " + str(balance_finale),'yellow'))
            print("\t\t" + usdt_symbol + " Balance: \t\t ", contract.functions.balanceOf('TG94UDXQyZ3r8MCHfecEpreVKsuKTyGnQz') / 10 ** precision)
            time.sleep(5) 
            deinit()
            sending = sending + 1
    except:
        print("\n\t An error occurred, please wait...\n")
        time.sleep(1)
        sending = sending + 1
