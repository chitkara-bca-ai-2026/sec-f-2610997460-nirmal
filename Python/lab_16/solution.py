print("===================================================================")
print("                ENTERPRISE MODULAR UTILITY CALCULATOR              ")
print("===================================================================")
history=[]
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return None
    else:
        return a/b
def modulus(a,b):
    if b==0:
        return None
    else:
        return a%b
def power(a,b=2):
    return a**b
    
while True:
    print("Select an operation:")
    print("1. Addition(+)")
    print("2. Subtraction(-)")
    print("3. Multiplication(*)")
    print("4. Division(/)")
    print("5. Modulus/ Remainder(%)")
    print("6. Power/ Exponential (Default: Square)")
    print("7. View Calculation History")
    print("8. Exit")



    choice=int(input("Enter your choice:"))
    if choice==1:
        a=int(input("Enter the value of a:"))
        b=int(input("Enter the value of b:"))
        #def ask_input():
         #   return (a,b)
        #a,b=ask_input()
        res=add(a,b)
        print("a+b=",res)
        history.append(f"{a}+{b}={res}")
    elif choice==2:   
        a=int(input("Enter the value of a:"))
        b=int(input("Enter the value of b:"))
        #def ask_input():
         #   return(a,b)
        #a,b=ask_input()
        res=subtract(a,b)
        print("a-b=",res)
        history.append(f"{a}-{b}={res}")
    elif choice==3:
        a=int(input("Enter the value of a:"))
        b=int(input("Enter the value of b:"))
        #def ask_input():
        #    return(a,b)
        #a,b=ask_input()
        res=multiply(a,b)
        print("a*b=",res)
        history.append(f"{a}*{b}={res}")
    elif choice==4:
        a=int(input("Enter the value of a:"))
        b=int(input("Enter the value of b:"))
        #def ask_input():
        #    return(a,b)
        #a,b=ask_input()
        res=divide(a,b)
        if res is None:
            print("CANNOT BE DIVIDED BY ZERO")
        else:    
            print("a/b=",res)
            history.append(f"{a}/{b}={res}")  
    elif choice==5:
        a=int(input("Enter the value of a:"))
        b=int(input("Enter the value of b:"))
        #def ask_input():
        #    return(a,b)
        #a,b=ask_input()
        res=modulus(a,b)
        if res is None:
            print("CANNOT PERFORM MODULUS BY ZERO.")
        else:
            print("a%b=",res)
            history.append(f"{a}%{b}={res}")
    elif choice==6:
        a=int(input("Enter the value of a:"))
        b=int(input("Enter the value of b:"))
        #def ask_input():
        #    return(a,b)
        #a,b=ask_input()  
        res=power(a,b)  
        print("a**b=",res)
        history.append(f"{a}**{b}={res}")
        
        print(history)

    elif choice==7:
        if len(history)==0:
            print("NO CALCULATION HISTORY!")
        else:
            print("CALCULATION HISTORY DISPLAY!")
            for items in history:
                print(items)    
    elif choice==8:
        print("THANKS FOR USING THE CULCULATOR!!!<'_'>")
        break            
    else:
        print("INVALID CHOICE")






           

        