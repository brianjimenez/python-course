import sys

start = 42
finish = 1200

numbers = []
for i in xrange(start, finish + 1):
    if i % 7 == 0 and i % 5 != 0 or i % 13 == 0:
        numbers.append(i)

total = len(numbers)
# What about reversed function?
reversed_numbers = [str(numbers[total-i-1]) for i in xrange(total)]

print ','.join(reversed_numbers)
