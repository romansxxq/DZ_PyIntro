#Ex.1
# fruits = ['apple', 'banana', 'apple', 'strawberry']
# print(fruits[:])

#Ex.2

# fruits = ['apple', 'banana', 'apple', 'strawberry']
# enter = input("Enter a fruit: ")
# print(f'{fruits[fruits.index(enter)]} count: {fruits.count(enter)}')

#Ex.3

# auto = ['Volvo', 'BMW', 'Toyota', 'Audi','Toyota']
# AutoName = input("Enter car name: ")
# ReplaceName = input("Enter new name: ")
# auto[auto.index(AutoName)] = ReplaceName
# print(auto)

#Ex.4

# numbers = (5,12,123,4,56,789,1,23,456,789)
# statistics = {}
#
# for i in numbers:
#     num = len(str(abs(i)))
#
#     if num in statistics:
#         statistics[num] += 1
#     else:
#         statistics[num] = 1
#
# for num, count in statistics.items():
#     print(f'{num} цифра - {count} елементи')

