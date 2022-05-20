# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def product(n_from, n_to):
    total = 1
    for i in range(n_from, n_to + 1, 1):
        remainder = i % 2
        if remainder == 0:
            total = total * i
        print(f"число {i} залишок {remainder} результат: {total}")
    print(f"Добуток: {total} ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    product(2, 10)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
