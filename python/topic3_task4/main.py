
def task():
    print("Введіть строку символів:")
    x = input()
    # x = "This is a Test String 12356"
    x_lower = []
    n_lower = 0
    print (f"Ви ввели: {x}")
    str_len = len(x)
    # print (f"length : {str_len}")
    for i in range(0, str_len):
        s = x[i]
        # print (f"s : {s}")
        if s.islower():
            n_lower += 1
            x_lower.append(s)
    print (f"The number of lower case letters: {n_lower}")
    print ("Lower case letters from your string:")
    for i in range(0, len(x_lower)):
        s = x_lower[i]
        if i == 0:
            print(f"{s}", end='')
        else:
            print(f";{s}", end = '')


if __name__ == '__main__':
    task()