n = int(input(" Введите число : "))   
numbers = list(range(2, n + 1))
for num in numbers:
    if num != 0:
        for x in range(2 * num, n+1, num):
            numbers[x-2] = 0
print(list(filter(lambda x: x != 0, numbers)))
