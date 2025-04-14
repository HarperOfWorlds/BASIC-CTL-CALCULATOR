Code = input("Addition(A) Subtraction(S) Multiplication(M) Or Division(D): ")
Input1 = input("First Number: ")
Input2 = input("Second Number: ")

if Code.upper() == 'A':
    sum = float(Input1) + float(Input2)
    print(sum)
elif Code.upper() =='S':
    sub = float(Input1) - float(Input2)
    print(sub)
elif Code.upper() =='M':
    mult = float(Input1) * float(Input2)
    print(mult)
else:
    div = float(Input1) / float(Input2)
    print(div)
