# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

def task():
    print("Enter the number:")
    x = input()
    x = int(x)
    if x < -6:
        print(f"число {x} менше -6")
        y = x**2
    elif x > 6:
        print(f"число {x} більше +6")
        y = math.tan((3*x)+(x/2))
    else:
        print(f"число {x} більше -6 та менше 6")
        y = abs(3*(x**3))
    print (f"число {x} результат {y}")



# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    task()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
