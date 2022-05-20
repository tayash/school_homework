# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def sum_number(a, b):
    total = 0
    cnt = 0
    for i in range (0, 7):
        print("Enter the number")
        input_a = input()
        input_a = int(input_a)
        if input_a > b or input_a < a:
            cnt += 1
            total += input_a

    print(f"total: {total} number: {cnt}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sum_number(5, 10)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
