my_list = list(range(10))

print(my_list)

even = list(range(0,10,2))
odd = list(range(1,10,2))

print(even)
print(odd)

my_str = "abcdefghijklmnopqrstuvwxyz"

print(my_str.index('e'))
print(my_str[4])

small_dec = range(0, 10)

print(small_dec)

print(small_dec.index(3))

odd = range(1, 1000, 2)

print(odd)

sevens = range(7, 1000000, 7)

x = int(input("Enter a positive integer: "))

if x in sevens:
    print("{} is divisible by seven".format(x))

decimals = range(0, 100)

print(decimals)

my_range = decimals[3:40:3]

print (my_range)

print('=' * 40)

for i in range(3, 40, 3):
    print(i)

print(decimals[3:40:3])
