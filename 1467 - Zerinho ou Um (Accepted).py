while True:
    try:
        num1,num2,num3 = list(map(int,input().split()))
        if num1 == num2 == num3:
            print("*")
        else:
            if (num1 == num2):
                print("C")
            else:
                if(num1 == num3):
                    print("B")
                else:
                    print("A")
    except EOFError:
        break