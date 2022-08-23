def div_by_7(x):
    for i in range(0, x):
        if i % 7 == 0:
            yield i


num = int(input("Please Enter the Number: "))
output = div_by_7(num)
for number in output:
    print(number)
