size = int(input("Enter the size of the pattern: "))

raw =0
while raw < size:
    for i in range(1,size +1):
        print("*", end="")
    print()
    raw +=1
