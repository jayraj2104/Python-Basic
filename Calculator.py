# Program : Calculator
OP=1
while(OP!="5"):
    N1,N2=float(input("ENTER THE VALUE 1 : ")),float(input("ENTER THE VALUE 2 : "))

    OP=input("" \
    "1 : +\n" \
    "2 : -\n" \
    "3 : *\n" \
    "4 : /\n" \
    "5 : Exit\n" \
    "Enter Your Choice : ")

    def calculator(OP):
        match OP:
            case "1": print(N1+N2)
            case "2": print(N1-N2)
            case "3": print(N1*N2)
            case "4": print(N1/N2)
            case "5": print("THANk yoU");  
            case _: print("You Entered Something Else Please Restart ")
    
    calculator(OP)

    

