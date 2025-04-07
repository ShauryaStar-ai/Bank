# Global variables 
user_counter = 0
clientInfo = {} 
def give_Account_Number():
    global user_counter  # Access the global user_counter
    user_counter += 1  # Increment the user counter
    accountNumber = user_counter  # Assign the incremented value as the user ID
    return accountNumber
# get the new users information 
def getInfomration(accountNumber):
    userInfomation = {}
    name  =input("Please entre your name ")
    phoneNUmber = (input("Please entre your Phone number "))
    pin = input("Please entre your pin ")
    accountType = input("What type of account do you want to make 'ck' for checking or 's' or saving ")
    accountMoney = int(input("What will be your deposit "))
    userInfomation["name"] = name
    userInfomation["Number"] = phoneNUmber
    userInfomation["pin"] = pin
    userInfomation["account Type"] = accountType
    userInfomation["Money"] = accountMoney
    clientInfo[accountNumber] = userInfomation
    return clientInfo
# the interface the user will use to add themselves to the bannk's records and make a account
def adding_Users():
    permission = input("Do you want to add yourself to you records or someone else 'y' / 'n' ")
    while permission == "y":
        accountNumber = give_Account_Number()
        getInfomration(accountNumber)
        permission = input("Do you want to add yourself to you records 'y' / 'n' ")

# prints the banks records 
def printRecords():
    print(clientInfo)
# Now that we have the user set up their information with us they can now add money reomve money and tranfer money
def addMoney():
    accNumber = int(input("Entre your account number to which you want to add money "))
    if accNumber in clientInfo:
        amountTobeAdded = int(input("Entre the amount of money to be added to your account "))
        clientInfo[accNumber]["Money"] += amountTobeAdded

def removeMoney():
    accNumber = int(input("Entre your account number to which you want to withdraw money from "))
    if accNumber in clientInfo:
        amountTobeRemoved = int(input("Entre the amount of money to be added to your account "))
        clientInfo[accNumber]["Money"] -= amountTobeRemoved 

def transfer():
    accTo = int(input("Entre the accpunt to which tranfer money to"))
    accFrom = int(input("Entre the accpunt to which tranfer money from"))
    amountToTansfer = int(input("What is the amount of moeny needed to be tranfered"))
    if amountToTansfer <= clientInfo[accFrom]["Money"]:
        clientInfo[accFrom]["Money"] -= amountToTansfer
        clientInfo[accTo]["Money"] +=amountToTansfer
    else:
        print("You dont have enough money to execute this transction")

def main():
    adding_Users()
    printRecords()
    action = input("'add money'   'remove money'  'transfer' 'exit' ")
    while action != "exit":
        if action == "add money":
            addMoney()
            printRecords()
        if action == "remove money":
            removeMoney()
            printRecords()
        if action == "transfer":
            transfer()
            printRecords()
        action = input("'add money'   'remove money'  'transfer'     'exit' ")
main()