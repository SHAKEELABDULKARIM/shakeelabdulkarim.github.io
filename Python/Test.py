
import math

# name  = input("what is your name ? ")
# print ("kaisy ho "+name)


# birth_year = input("Birth Year ")
# age  = 2024-int(birth_year)
# print (age)

# name = 'jennifer'
# print(name[1:-1])

first_name = 'shakeel'
last_name = 'abdulkarim'

# print(first_name[1:])
# message = first_name+' ' +last_name +' is a programmer'
# msg = f'{first_name} {last_name} is a programmer'
# print(msg)

# length = len(first_name)
# print(length)
# print (first_name.title())
# in order to check existance of a letter or a character in a sring use in

# is_exit = 'malik' in first_name
# print(is_exit)

# x =2.9
# print (math.floor(x))


# secret_number = 9
# guess_counter  = 0
# total_guess = 3

# while guess_counter<total_guess:
#     number = int(input("Guess "))
#     guess_counter+=1
#     if(number==secret_number):
#         print('you won')
#         break
# print('you lose') 


# numbers = [3,6,9,10,30,2,4,1,0]
# max = numbers[0]
# for number in numbers:
#     if(number>max):
#         max = number
# print('Max Number is '+str(max) )


# number1 = int(input("Enter First Number" ))
# number2 = int (input("Enter Second Number"))
# result =number1*number2
# if(result>100):
#     print("Sum is "+str(result))
# else:
#     print("Product is "+ str(result))



["""]
# Exercise 1: Calculate the multiplication and sum of two numbers
    
def product_or_sum_Fuction(num1,num2):
  
    product = num1*num2
  
    if(product<=1000):
                print("Product of numbers are "+str(product))

        
    else:
                print("Sum of 2 Numbers are "+str(num1+num2))

        
        
product_or_sum_Fuction(int(input("Enter First Number ")),int(input("Enter Second Number ")))     
["""]
["""]
# Exercise 2: Print the sum of the current number and the previous number

def Sum_of_concrete_numbers():
    print("Printing current and previous number sum in a rang(10)")
    previous_num = 0
    for i in range(0,10):
        sum = previous_num+i
        print("Current Number is ",i,"Previos Number",previous_num," Sum: ",sum)
        previous_num = i
    
    
Sum_of_concrete_numbers()
["""]     
["""]   
    # Exercise 3: Print characters from a string that are present at an even index number
    
def Print_characters_from_string_on_Even_Index():
        print ("Ref String is ")
        strinname = str(input())
        print("Printing only even index chars")
        sizeofstring = len(strinname)
        for i in range(0,sizeofstring,2):
                print(strinname[i])    
        # x = list(strinname)
        # for i in x[0::2]:
        #     print(i)
                
Print_characters_from_string_on_Even_Index()
["""]

["""]
# Exercise 4: Remove first n characters from a string

def Remove_first_N_Characters(_name,numb):
    
    print(_name[numb:])
    
Remove_first_N_Characters(str(input("ENter Name ")),int(input("Enter Number to remove ")))
["""]

# # Exercise 5: Check if the first and last number of a list is the same
# def Check_if_first_and_last_num_is_same():
#     numbers_x = [10, 20, 30, 40, 10]
#     numbers_y = [75, 65, 35, 75, 30]
#     print("given list: ",numbers_x)
#     if(numbers_x[0]==numbers_x[-1]):
#         print("Result is true")
#     else:
#         print("Result is False")
#     print("given list: ",numbers_y)
#     if(numbers_y[0]==numbers_y[-1]):
#         print("Result is true")
#     else:
#         print("Result is False")
# Check_if_first_and_last_num_is_same()


# Exercise 6: Display numbers divisible by 5 from a list

# def Display_numbers_divisible_by_5_from_list(_list):
#     size   = len(_list)
#     print(range(0,size))
#     for i in _list:
#         if(i%5==0):
#              print(i)
# numbrlist = [5,12,13,15,30,25,20,55,60]
# Display_numbers_divisible_by_5_from_list(numbrlist)

# Exercise 7: Return the count of a given substring from a string

# def Return_the_count_of_given_substring_from_a_string():
#     givenstring  = "shakeel abdulkarim lives in lahore. shakeel abdulkarim belongs to lahore"
#     stringtofind = "shakeel"
#     count = givenstring.count(stringtofind)
#     print (count)
# Return_the_count_of_given_substring_from_a_string()

# Exercise 8: Print the following pattern

def print_pattern():
    for num in range(5):
        for i in range(num+1):
            print(num+1,end=" ")
        print("\n")        
print_pattern()
