#Smallest multiple
list20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
i = 1
e = 1
longlist = list(range(10000000))
while i <= 20 and e <= 10000000:
    if longlist[e] % list20[i] == 0:
        i = i + 1
        print (i)
    else:
        e = e + 1



