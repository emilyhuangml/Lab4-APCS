#Largest Prime Factor


# factorList = []
# list = []
# for i in range (1, 320):
#     if 320 % i == 0:
#         factorList.append(i)
#     for factor in factorList:
#         for e in range (1, factor):
#             if factor % e != 0:
#                 list.append(e)
#                 print(len(list))
# for factor in factorList:
#     primeList = []
#     for e in range (1, factor+1):
#         if factor % e == 0:
#             primeList.append(factor)
#             if len(primeList) == 2:
#                 print(factor)
        
# ^^^failed attempt bc I read the question wrong ^^^
# I looked at other people's solution and had to analyze it for a long time to finally understand what it meant:
n = 600851475143
i = 2 #starting prime factor

while i * i < n: #bc i can't be greater than the square root of n (ex. prime factors of 25 is 5 and 5, can't be greater than that)
    while n%i == 0: #divides n so it is not divisible by multiples of the current prime factor
        n = n / i
    i = i + 1
print (n)


