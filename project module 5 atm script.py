import sys

#account balance 
account_balance = float(500.25)


#<--------functions go here-------------------->
#printbalance function
def balance ():
  print("Your current balance:\n %.2f" % account_balance)
#deposit function
def deposit():
  deposit_amount = float(input("How much would you like to deposit today?\n"))
  balance = account_balance + deposit_amount
  print(("Deposit was $%.2f, current balance is $%.2f") % (deposit_amount, balance))

#withdraw function
def withdraw():
  withdraw_amount = float (input("How much would you like to withdraw today?\n"))
  if withdraw_amount > account_balance:
    print("$%.2f is greater than your account balance of $%.2f" % (withdraw_amount, account_balance))
  else:
    balance = account_balance - withdraw_amount
    print("Withdrawal amount was $%.2f, current balance is $%.2f" % (withdraw_amount, balance))

#User Input goes here, use if/else conditional statement to call function based on user input
userchoice = input ("What would you like to do?\n")

if (userchoice == "D"):
  deposit()
elif (userchoice == "W"):
  withdraw()
elif (userchoice == "B"):
  balance()
elif (userchoice == 'Q'):
  print('Thank you for banking with us.')
