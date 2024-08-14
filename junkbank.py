class Card:
    def __init__(self, accounts:list=[]) -> None:
        cvc = ""   
        for digits in range(3):
            cvc += str(random.randint(0,9))
        valid_thru = "06/26"
        cardnum = ""
        for digit in range(16): cardnum += str(random.randint(0,9))
        self.cvc = cvc
        self.card_number = cardnum
        self.valid_thru = valid_thru

        while logged_in:
            print(logged_acc.info)
            option = ""
            while not option in ["1","2","3"]:
                balance = int(logged_acc.balance)/100
                print(f"""==========================
Balance:
R{format(balance,".2f")}
1. Deposit
2. Withdraw
3. Transfer
4. View Statement
5. Log Out
==========================
""")        
                option = input()
                if not option in ["1","2","3","4","5"]:
                    print("please follow intructions")
                    continue
                break
            #Check deposit
            if option == "5":
                BankAccount.accounts[logged_acc.username] = logged_acc
                logged_in = False
                break
            elif option in ["1","2","3"]:
                while True:
                    print("to go back type: back()")
                    amount = input("Enter Amount \nR")
                    if amount == "back()": break
                    try:
                        int(amount)*100
                    except:
                        print("input valid amount")
                        continue
                    if option == "2":
                        if not logged_acc.valid_transfer(int(amount)*100, True): continue
                        action = f"Withdraw R{amount} from Account?"
                    elif option == "1":
                        if not logged_acc.valid_transfer(int(amount)*100, False): continue
                        action = f"Deposit R{amount} into Account?"
                    else: 
                        if not logged_acc.valid_transfer(int(amount)*100, True): continue
                        while True:
                            recipuser = input("enter recipient username: \n")
                            try:
                                BankAccount.accounts[recipuser]
                            except:
                                print("username doesnt exist\ntry again")
                                continue
                            recip = BankAccount.accounts[recipuser]
                            break
                        action = f"Transfer R{amount} to {recip.username}"

                    print(action)
                    confirmation = input("Confirm (Y/N)\n").lower()
                    if confirmation == "n": 
                        while True:
                            sumn = input("""1. retry
    2. go back to home screen""")
                            if not sumn in ["1","2"]:
                                print("please follow instructions")
                                continue
                            break
                        if sumn == "2":
                            break

                    elif confirmation == "y":
                        amount = int(amount)*100
                        while True:
                            reference = input("Enter your reference:\n")
                            reference[:10]
                            while True:
                                confirmation = input(f"Your reference: '{reference}'\nConfirm(Y/N)")
                                if confirmation in ["y","n"]:
                                    break
                                print("please follow instructions")

                            if confirmation == "y": break
                            else:
                                continue

                        scredit = "R0.00"
                        sdebit = "R0.00"
                        if option == "1": 
                            logged_acc.deposit(amount)
                            scredit = f"R{format(amount/100,'.2f')}"
                            print(f"R{amount/100} deposited into account")

                        elif option == "2": 
                            logged_acc.withdraw(amount)
                            sdebit = f"R{format(amount/100,'.2f')}"
                            print(f"R{amount/100} withdrawn from account")
                        else:
                            logged_acc.transfer(recip, amount)
                            BankAccount.accounts[recip.username] = recip
                            sdebit = f"R{format(amount/100,'.2f')}"
                            print(f"R{format(amount/100,'.2f')} transferd to Account {recip}")
                        BankAccount.accounts[logged_acc.username] = logged_acc
                        slip = {
                            "date": str(datetime.date.today()),
                            "reference": reference,
                            "credit": scredit,
                            "debit": sdebit,
                            "balance": f"R{logged_acc.balance/100}"
                        }
                        logged_acc.statement += [slip]
                        break
            
            elif option == "4":
                print(f"""
======================================================================================
Account No: {logged_acc.username}                              Type: {logged_acc.account_type}
Account Holder: {logged_acc.account_holder}
R{logged_acc.balance/100}
======================================================================================""")
                if logged_acc.statement == []:
                    print("no transactions")
                else:
                    print("date----reference----credit----debit----balance")
                    for slips in logged_acc.statement:
                        print(slips.get("date")+"----"+slips.get("reference")+"----"+slips.get("credit")+"----"+slips.get("debit")+"----"+slips.get("balance"))                 
        