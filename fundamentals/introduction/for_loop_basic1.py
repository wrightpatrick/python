num = 0
# while num <= 150:
#     if num % 5 == 0:
#         print(num)
#     num += 1


# while num <= 1000:
#     if num % 5 == 0:
#         print(num)
#     num += 1

# while num < 100:
#     if num % 10 == 0:
#         print("Coding")
#     elif num % 5 == 0:
#         print("Coding Dojo")
#     else: print(num)
#     num += 1

# num2 = 0
# while num < 500000:
#     if num % 2 != 0:
#         num2 = num2 + num
#     num += 1

# print(num2)

# num1 = 4
# num2 = 2018
# while num2 > 0:
#     print(num2)
#     num2 = num2 - num1

# multiple_checker = {
#     "low_num" : 2, "high_num" : 100, "mult" : 4
# }

# mult_checker = { "low_num" : 2, "high_num" : 100, "mult" : 4}

# for i in range(low_num, high_num, mult):
#     if i % mult == 0:
#         print(i)
    
low_num = 1
high_num = 100
mult = 4

for i in range(low_num, high_num + 1):
    if i % mult == 0: #the step still needed to be 1, why plus and no comma??
        print(i)
    
        
    