# Multiples of 3 and 5
multiples = []
for n in range(0,1001):
    if n%3 == 0 or n%5 == 0:
        multiples.append(n)
sumofmultiples = sum(multiples)
print(sumofmultiples)

# Even Fibonacci numbers
list = [1,2]
list.append(sum(list))
sum_list = []
while list[-1] <= 4000000:
    next_sum = sum(list[-2:])
    list.append(next_sum)
for n in list:
    total_sum = ''
    if n%2 == 0:
        sum_list.append(n)
    total_sum = sum(sum_list)
print(total_sum)
