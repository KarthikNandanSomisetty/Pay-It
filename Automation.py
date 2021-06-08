
print("Welcome to Pay it !")

class grocery:
    def __init__(self,cardNo,name):
        self.cardNo=cardNo
        self.name=name
    
    def integers(self):
         print("Choose the bill you want to pay : ")
         print("1)Electricity Bill 2)Telephone Bill 3)Gas Bill")
         activity=int(input("Enter your choice number : "))
         if(activity==1):
            input("Eneter the amount you need to pay : ")
            print("Amount Succesfully Paid ✔")

         elif(activity==2): 
           input("Eneter the amount you need to pay : ")
           print("Amount Succesfully Paid ✔")

         elif(activity==3):
            input("Eneter the amount you need to pay : ")
            print("Amount Succesfully Paid ✔")
    
def main():
    name=input("Enter your name: ")
    card_number=input("Insert your card number: ")
    print("Welcome "+name+"!")
    new_user=grocery(card_number, name)

    if card_number.strip().isdigit():
        new_user.integers()
        

    
if __name__=="__main__":
    main()