class ATM(object):
    def __init__(self, cardNum, cardPin):
        self.cardNum = cardNum
        self.cardPin = cardPin

    def withdraw(self,amount):
        nw = 5000 - amount
        print("You have withdrawn "+str(amount)+". Your remaining balance is "+str(nw)+".")

    def balance(self):
        nw = 5000 - amount
        print("You're current balance is $5000.")


def main():
    card_number= input("Insert Your Card Number: ")
    pin_number= input("Enter Your Card's Pin: ")

    new_user= ATM(card_number,pin_number)
    print("Choose Any Activity:")
    print("1). Balance enquiry     2). Withdrawl " )
    activity=int(input("Enter Activity Number : "))
    
    if(activity ==1):
        new_user.balance()

    elif (activity==2):
        amount=int(input("Enter the Amount You Want to Withdraw: "))
        new_user.withdraw(amount)

    else:
        print("Enter a Valid Number")      


main()          
    

