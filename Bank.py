class Bank:
    def __init__(self,accno,accname,username,passwod,balance=0):
        self.accNo=accno
        self.accHolder=accname
        self.uname=username
        self.pwd=passwod
        self.balance=balance
    def Login(self,un,pw):
        if((self.uname==un)and(self.pwd==pw)):
            return True

    def Deposit(self,depAmount):
        if(depAmount<0):
            print("Invalid Deposit Amount")
        else:
            self.balance=self.balance+depAmount
            print(depAmount,"deposited successfully")
            print("New balance=",self.balance)
    def Withdraw(self,wdrawAmt):
        if(wdrawAmt>self.balance):
            print("Insufficient balance to withdraw the entered amount")
        else:
            self.balance=self.balance-wdrawAmt
            print(wdrawAmt, "withdrawn successfully")
            print("New balance=", self.balance)
    def AccountDetails(self):
        print("Account Number:",self.accNo)
        print("Account Holder:", self.accHolder)
        print("Account Balance:", self.balance)
        return

def sign_in(accounts):
    login=False
    username = input("Enter the username:")
    password = input("Enter the password:")
    for b1 in accounts:
        if (b1.Login(username, password)):
            print("Login successful")
            login=True
            while (True):
                option = int(input("********************\n1.Deposit\n2.Withdraw\n3.Account Details\n4.Exit\nEnter an option: "))
                if option == 1:
                    depositAmt = int(input("Enter the amount to deposit : "))
                    b1.Deposit(depositAmt)
                elif option == 2:
                    withdrawAmt = int(input("Enter the amount to withdraw : "))
                    b1.Withdraw(withdrawAmt)
                elif option == 3:
                    b1.AccountDetails()
                elif option == 4:
                    print("Thank You for banking with us...")
                    exit()
                else:
                    print("Invalid option.Enter a valid option")
    if login==False:
            print("Invalid credentials.Login unsuccessful")
def account_list():
    # considering some existing account holders
    accounts = [
        Bank('123456789', 'Holder1', 'user1', 'password123', balance=1000),
        Bank('987654321', 'Holder2', 'user2', 'password456', balance=1500),
    ]
    return accounts
def sign_up(accounts):
    acc_no = input("Enter your account number: ")
    acc_name = input("Enter your account holder name: ")
    uname = input("Enter the username:")
    pwd = input("Enter the password:")

    new_account = Bank(acc_no, acc_name, uname, pwd)
    accounts.append(new_account)

    print("Account created successfully")

print("Welcome to Net Banking")
account_list = account_list()
while (True):
    signin_up=int(input("****************************\n1.Sign In\n2.Sign Up\n3.Exit\nEnter an option:"))
    if signin_up==1:
        sign_in(account_list)
    elif signin_up==2:
        sign_up(account_list)
    elif signin_up==3:
        exit()
    else:
        print("Invalid option.Enter a valid option")
