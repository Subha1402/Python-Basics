for i in range(5):
    n= input("Enter name of student:")
    s=0
    print("Enter 5 marks of student")
    for j in range(5):
        m=float(input("Enter mark: "))
        s+=m
    print("Total of",n,"is",s)
