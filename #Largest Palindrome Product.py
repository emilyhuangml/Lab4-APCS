#Largest Palindrome Product 
num_list = []
def find_pal():
    for i in range (100, 1000):
        for e in range (100, 1000):
            number = str(i*e)
            if number == number[::-1]:
                num_list.append(number)
                num_list.sort()
    print(num_list[-1])
       
print(find_pal())

       

   
