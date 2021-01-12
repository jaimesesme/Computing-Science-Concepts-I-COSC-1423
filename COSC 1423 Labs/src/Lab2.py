
def main() :
    do_math_one()
    do_math_two()
    do_math_three()
    do_math_four()
    do_math_five()
    do_math_and_string()   # for extra credit, 3 points
    
# ***********************************************************************
# do_math_one()
# Write a function that stores the value 5 in the variable 'num' and prints 
# the contents of 'num'
# then stores 7 in 'num' and prints the contents of 'num'.
#
# Help: To print the contents of a variabe x: print(x)
# ***********************************************************************
def do_math_one() :
    print("Now in the do_math_one() function")
    num = 5
    print(num)
    num = 7
    print(num)


# ***********************************************************************
# do_math_two()
# Write a function that adds 5 + 7 and stores the result in the variable 'mySum'
# then prints the contents of the variable 'mySum'
# ***********************************************************************
def do_math_two() :
    print("Now in the do_math_two() function")
    mySum = 5 + 7
    print(mySum)

# ***********************************************************************
# do_math_three()
# Write a function that stores 5 in the variable 'num' and prints 'num'
# then stores num + 7 in the variable 'mySum' and prints the contents of 'mySum'
# 
# Help: To add a number to what is already in variable a: a = a + (Number)
# ***********************************************************************
def do_math_three() :
    print("Now in the do_math_three() function")
    num = 5 
    print(num)
    mySum = num + 7
    print(mySum)

# *********************************************************************** 
# do_math_four()
# Write a function that prints "13" + "16"
# and then prints 13 + 16 (without quotes)
# Now add 13 + 16 and store the result in a variable named "sum"
# The program should then print "13 + 16 = 29", in a way that uses
# the contents of sum.
#
# Help: To print a string that includes double quotes, you can surround
# the string with single quotes.
# ***********************************************************************
def do_math_four() :
    print("Now in the do_math_four() function")
    print('"13"+"16"')
    print("13+16")
    sumnum = 13 + 16
    print("13 + 16 = ", sumnum)


# *********************************************************************** 
# do_math_five()
# Write a function that prints 20 + 17 then divide the sum by 3
# The program should then print "20 + 17 then divided 3 = 12.3333", in a way that accounts
# for precidence of operator.
#
# Help: whatever is in parenthesis will occur first. There is 2 extra points if you use formatting to
# control the number of digits after the decimal point.
# the string with single quotes.
# ***********************************************************************
def do_math_five() :
    print("Now in the do_math_five() function")
    sumnum = 20 + 17
    average = sumnum/3
    print("20 + 17 then divided by 3 = ",(format(average, ".4f")))

#------------------------------------------------------------

# Extra Credit

#------------------------------------------------------------

# ***********************************************************************
# Ask for the users name, age, and 3 grades
# calculate the average of the grades
# print to the screen "My name is <name goes here>, I am <age> years old and my average grade is <average goes here>
# ***********************************************************************
def do_math_and_string():
    print("Now in the do_math_and_string() function")
    name = input("Enter name: ")
    age = input("Enter age: ")
    test1 = int(input("Enter Exam 1: "))
    test2 = int(input("Enter Exam 2: "))
    test3 = int(input("Enter Exam 3: "))
    average = test1 + test2 + test3
    print("My name is ", name,", I am", age, "years old, and my average grade is", average)

# ***********************************************************************
# This is where execution starts.
# ***********************************************************************

if __name__ == "__main__":
    main()    
