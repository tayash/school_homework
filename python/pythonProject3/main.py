# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def task():
    print("Enter the number")
    x = input()
    x = int(x)
    if x < 0:
        sqr = x ** 2
        x = abs(x)
        rdc = x ** (1. / 3.)
        rdc *= (-1)
        print (f"квадрат: {sqr} корінь: {rdc}")
    else:
        print (f"число більше за нуль")
   # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    task()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
