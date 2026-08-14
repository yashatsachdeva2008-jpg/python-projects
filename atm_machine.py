print("Welcome to xyz ATM")
Balance=100000
while True:
        print("What you want to do :")
        print("1=check balance")
        print("2=Deposit money")
        print('3=Withdraw money')
        print("4=exit")
        A=int(input("choose ur option: "))
        if(A==1):
                print("Your balance is :",Balance)
        elif(A==2):
                B=int(input("How much money u wanna add: "))
                print("Your balance now is :",(Balance+B))
                Balance=Balance+B
                
        elif(A==3):
                C=int(input("How much money u wannna withdraw: "))
                if C>Balance:
                        print("You dont have enough money to withdraw")
                        continue
                else:
                        print("Your balance is ",(Balance-C))
                        Balance= Balance-C
                
        elif(A==4):
                quit()
        else:
                print("invalid choice!!")
                print("Choose valid option")
                continue

