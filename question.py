# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME  is the input of the function.  The first line of the code has been defined as below

def hello_name(User_Name):
    print(f"hello_{User_Name}")
#pass

hello_name("Marvin")

# Question 2:
#Write a python function, first_odds that prints the odd numbers form 1-100 and returns nothing
def first_odds():
    odds = [] 
    for number in range(1,100):
        if number % 2 == 1:
            # print(number)
            odds.append(number)
    print(f"{odds}")

first_odds()

# question
#Please write a Python function, max_num_in_list to return the max number of a given list.  the first 
#line of the code has been defined as below.

def max_num_in_list(a_list):
    a_list.sort()
    return(a_list[-1])
a_list=[10,25,14,39]
print(max_num_in_list(a_list))

#question 4
#Write a function to return if the given year is a leap year.  A leap year is divisible by 4
#but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type 
#(true/false)

def is_leap_year(a_year):
    if (a_year%4)==0:
        if (a_year%100)==0:
            if(a_year%400)==0:
                return True
            else:
                return False
        else:
            return True
    else:
            return False

print(is_leap_year(2000))