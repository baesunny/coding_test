while True:    
    number = input().split()

    if (int(number[1])==0) or (int(number[0])==0):
        break
    elif int(number[1])%int(number[0]) == 0:
        print("factor")
    elif int(number[0])%int(number[1]) == 0:
        print("multiple")
    else:
        print("neither")