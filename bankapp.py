import random
import datetime
usersbase:dict = {}

class UserAccount():
    def __init__(self, name, surname, username, password):
        self.user_firstname = name
        self.user_surname = surname
        self.username = username
        self.accounts = {}
        self.password = password

    def create_new_account(self):
        account = BankAccount(self.user_firstname, self.user_surname, self.username, self.password)
        if not self.accounts.get(account.account_type) is None:
            print(f"{account.account_type} Account Already Exists")
            return
        self.accounts[account.account_type] = account
        print(f"{account.account_type} Account Successfully Created")

    @property
    def account_holder(self):
        return self.user_firstname+" "+self.user_surname
    
    def __repr__(self) -> str:
        return self.account_holder
    
class BankAccount(UserAccount):

    def __init__(self, name, surname, username, password, acctype = None):
        super().__init__(name, surname, username, password)
        acctype = get_acctype_from_user()

        self.account_number = get_n_digits(10)
        self.balance = 0 #BALANCE IN CENTS
        self.phone_number = generatepnumber()
        self.account_type = acctype
        self.password = password
        self.debitcard = Card([self])
        self.statement = []

    
    @property
    def info(self):
        return {
            "Account Holder": self.account_holder,
            "Username": self.username,
            "Account Number": self.account_number,
            "Account Type": self.account_type,
            "Balance": self.balance,
            "Phone Number": self.phone_number,
        }
    
    def valid_transfer(self, amt:int, out):

        if not amt >= 1:
            print("amount must be atleast be R0.01")
            return False
        elif amt > self.balance and out:
            print("Declined insufficient funds")
            return False
        return True
    
    def transfer(self, other, amt:int):
        if self.valid_transfer(amt, True):
            self.balance -= amt
            other.balance += amt

    def deposit(self, amt:int):
        if self.valid_transfer(amt, False):
            self.balance += amt

    def withdraw(self,amt: int):
        if self.valid_transfer(amt, True):
            self.balance -= amt
                   
class Card:
    
    def __init__(self, accounts:list) -> None:
        self.type = type
        self.card_balance = {}
        self.pin = 000000
        for ac in accounts: 
            self.card_balance[ac.account_type] = ac.balance
        self.info = {
            "Card Number": get_n_digits(16),
            "cvc": get_n_digits(3),
            "Valid Thru": "06/26"
        }

    def __init__(self, accounts:list) -> None:
        self.type = type
        self.card_balance = {}
        for ac in accounts: 
            self.card_balance[ac.account_type] = ac.balance
        self.info = {
            "Card Number": get_n_digits(16),
            "cvc": get_n_digits(3),
            "Valid Thru": "06/26"
        }


def generatepnumber()-> str:
    pnumber = "+27"
    snum = ["6","7","8"][random.randint(0,2)]
    pnumber += snum
    tnum  = str(random.randint(1,9))
    pnumber += tnum
    pnumber += get_n_digits(7)
    return pnumber

def get_n_digits(n=10) -> str:
    hereyougo = ""
    for digits in range(n):
        hereyougo += str(random.randint(0,9))
    return hereyougo

def get_acctype_from_user() -> str:
    while True:
        acctype = input("""enter number for account type: 
1. Current/Checking Account
2. Savings Account
""")
        
        if acctype in ["1","2"]: 
            if acctype == "1": return "Current"
            elif acctype == "2": return "Savings"
            confirmation = input("Are you sure you want to set account type to "+acctype+" Account? (Y/N) ").lower()
            if confirmation == "n": continue
            elif confirmation != "y": 
                print("please follow instructions")
                continue
        else: 
            print("please follow instructions")
            continue
        break

def create_new_passward() -> str:
    while True:
        password = input("create password: ")
        if password == input("confirm password: "): 
            return password
        print("Passwords do not match try again")

def getikey(a:dict, n:int):
    i = 0
    for key in a:
        if n == i: return key
        i += 1
    return None


if __name__=="__main__":
    logged_in = False
    #logging/signing in user
    while True:
        while not logged_in:
            print(usersbase)
            iput = input("""1. Sign Up
2. Log In\n""")
            if iput == "1":
                while True:
                    print("to go back type 'back()' ")
                    fname = input("Enter first name:\n")
                    if fname.lower() == "back()": break
                    lname = input("Enter last name:\n")
                    print("first name: "+fname)
                    print("last name: "+lname)
                    confirmation = input("Confirm (Y/N)\n").lower()
                    if confirmation == "n": continue
                    elif confirmation != "y": 
                        print("please follow intructions")
                        continue
                    password = create_new_passward()
                    username = get_n_digits(10)
                    while usersbase.get(username) != None:
                        username = get_n_digits(10)
                    print(f"Your username is {username}")
                    user = UserAccount(fname, lname, username, password)
                    usersbase[user.username] = user 
                    break
            elif iput == "2":
                # logging_user_in
                while not logged_in:
                    print("enter your username:")
                    iput = input()
                    #Take this nonsense away
                    if usersbase.get(iput) is None:
                        iput = username 
                    try: 
                        usersbase[iput]
                    except:
                        print("enter valid username")
                        continue
                    trying = usersbase[iput]
                    while True:
                        password = input("Enter password: \n")
                        if password != trying.password:
                            print("password incorrect")
                            continue
                        break
                    
                    logged_user:UserAccount = usersbase[iput]
                    if logged_user is None:
                        #MASSIVE NOT DONE 
                        option = ""
                        while not option in ["1","2"]:
                            print("username does not exist")
                            print("1. retry")
                            option = input("2. Go to sign screen\n")
                            if not option in ["1","2"]:
                                print("please follow instruction")
                        if option == "1": continue
                        elif option == "2": break
                    else:
                        logged_in = True
                        break

            else: print("please follow intructions")
        #run the fucking app
        
        action = None
        option = ""

        while logged_in:

            if logged_user.accounts == {}:

                print(f"""
Welcome, {logged_user.account_holder}
====================================
no accounts

1. Create Account
2. Log Out
====================================
""")        
                option = input()
                if not option in ["1","2"]: 
                    print("please follow instructions")
                    continue
                if option == "2":
                    logged_in = False
                    continue
                while True:
                    confirmation = input("Create New Account? (Y/N)\n").lower()
                    if not confirmation in ["y", "n"]: 
                        print("please follow instructions")
                        continue
                    break
                if confirmation == "y": 
                    logged_user.create_new_account()
                    break
                continue
            else:
                while True:
                    print(usersbase)
                    print(f"""Welcome, {logged_user.account_holder}
====================================""")  

                    for type in logged_user.accounts:
                        print(f"""{type} Account
{f"R{format(logged_user.accounts[type].balance/100,'.2f')}"}
------------------------------------""")
                    option = ""
                    option = input("""
1. Deposit
2. Withdraw
3. Transfer
4. View Statement
5. Create New Account
6. Delete Account
7. Settings
8. Log Out
====================================\n""")
                    if not option in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                        print("please follow instructions")
                        continue
                    break
                if option in ["1","2","3"]:
                    while True:
                        while "Entering Amount":
                            print("to go back type: back()")
                            amount = input("Enter Amount \nR")
                            if amount == "back()": break
                            try:
                                int(amount)*100
                            except:
                                print("input valid amount")
                                continue
                            break
                        while "Selecting Account":
                            print("Select Account your account")
                            i = 0
                            accs = []
                            types = []
                            for type in logged_user.accounts:
                                i += 1
                                print(f"{i}. {type} Account")
                                accs += [str(i)]
                                types += [type]
                            accn = input()
                            if accn in accs:
                                print("Yesssssssssssss")
                                break
                            print("please follow instructions")
                        account: BankAccount = logged_user.accounts[types[int(accn)-1]]
                        if option == "2":
                            if not account.valid_transfer(int(amount)*100, True): continue
                            action = f"Withdraw R{amount} from {account.account_type} Account?"
                        elif option == "1":
                            if not account.valid_transfer(int(amount)*100, False): continue
                            action = f"Deposit R{amount} into {account.account_type} Account?"
                        else: 
                            if not account.valid_transfer(int(amount)*100, True): continue
                            action = "Transfers not done yet"
                        while "confirming":
                            print(action)
                            confirmation = input("Confirm (Y/N)\n").lower()
                            if confirmation in ["y","n"]:
                                break
                            print("please follow instructions")
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
                            else: continue
                        else:
                            amount = int(amount)*100
                            while True:
                                reference = input("Enter your reference:\n")
                                reference[:10]
                                confirmation = input(f"Your reference: '{reference}'\nConfirm(Y/N)").lower()
                                if confirmation == "y": break
                                elif confirmation == "n": continue
                                print("please follow instructions")
                            scredit = "R0.00"
                            sdebit = "R0.00"
                            if option == "1":
                                account.deposit(amount)
                                scredit = f"R{format(amount/100,'.2f')}"
                                print(f"R{amount/100} deposited from account")
                            elif option == "2":
                                account.withdraw(amount)
                                sdebit = f"R{format(amount/100,'.2f')}"
                                print(f"R{amount/100} withdrawn from account")
                            else:
                                print("Transfers not done yet and nothing happened")
                            logged_user.accounts[account.account_type] = account
                            slip = {
                                "date": str(datetime.date.today()),
                                "reference": reference,
                                "credit": scredit,
                                "debit": sdebit,
                                "balance": f"R{account.balance/100}"
                            }
                            account.statement += [slip]
                            break


                elif option == "5":
                    while True:
                        confirmation = input("Create New Account? (Y/N)\n").lower()
                        if not confirmation in ["y", "n"]: 
                            print("please follow instructions")
                            continue
                        break
                    if confirmation == "y": 
                        logged_user.create_new_account()
                
                elif option in ["4", "5", "6", "7"]:
                    print("STILL IN PROGRESS")
                elif option == "8": 
                    usersbase[logged_user.username] = logged_user
                    logged_in =  False
                    print("logged off successfully")
                    break