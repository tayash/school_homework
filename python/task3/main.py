def sum_number():
    total = 0
    cnt = 0
    for i in range (0, 8):
        print("Enter the number")
        input_a = input()
        input_a = int(input_a)
        sqr_input = input_a**2
        if sqr_input > 10:
            print(f"Квадрат числа {input_a} більше 10 ({sqr_input})")
            cnt += 1
            total += input_a

    print(f"total: {total} number: {cnt}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sum_number()