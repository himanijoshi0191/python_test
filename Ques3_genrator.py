def div_generator(x):
    for i in range(0, x):
        if i % 7 == 0 and i % 5 == 0:
            yield str(i)


num = int(input("Please Enter the Number: "))
output = list(div_generator(num))
res = ','.join(output)
print(res)
