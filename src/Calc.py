def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    return a / b


def square(a):
    return a * a


def squareroot(a):
    return a ** 0.5

class Calc:
    def my_function(self):
        return 0

    if __name__ == "__main__":
        a = float(input("Enter first number:"))
        b = float(input("Enter second number:"))
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Square")
        print("6.Sqroot")
        choice = int(input("Enter your choice:1/2/3/4/5/6"))

    if choice == 1:
     print(addition(a, b))

     #result = addition(a, b)
        #return result

    elif choice == 2:
     print(subtraction(a, b))
     #result = subtraction(a, b)
      #  return result

    elif choice == 3:
     print(multiply(a, b))
     #result = multiply(a, b)
      #  return result

    elif choice == 4:
     print(division(a, b))
     #result = division(a, b)
      #  return result

    elif choice ==5:
     print(square(a))
      #  result = square(a)
       # return result

    elif choice == 6:
     print(squareroot(a))
      #  result = squareroot(a)
       # return result

    else:
     print("invalid choice")