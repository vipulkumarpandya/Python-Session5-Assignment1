def testfunction(a=0):
    try :
        b = a/0

    except ZeroDivisionError:
        print("Cannot divide a number by Zero")



a = input("Enter a number ")
testfunction(int(a))
