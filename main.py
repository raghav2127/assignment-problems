# FILTER ALL THE LANGUAGE THAT STARTS WITH "P"

# l = ['Python', 'Java', 'Perl', 'PHP', 'Python', 'JS', 'C++', 'JS', 'Python', 'Ruby']
# l1 = []
# for i in range(len(l)):
#     if (l[i][0]) == "P":
#         l1.append(l[i])
# print(l1)

# RAISE TO THE POWER OF LIST INDEX

# a = [1,2,3,4,5]
# b = []
# for i in a:
#     i = i**i
#     b.append(i)
# print(b)



# count the vowels in the given string

# s = str(input("Enter the string:"))
# l = ["a","e","i","o","u","A","E","I","O","U"]
# for i in s:
#     for v,x in enumerate(l):
#         if i==x:
#             print(i,i.count(i))
#



#REVERSE THE STRING USING FOR LOOP

# s = "hello"
# s1 = ""
# for i in s:
#     s1=i+s1
# print(s1)

#REVERSE THE STRING USING WHILE LOOP

# s = "raghav"
# s1 = ""
# n = 0
# while n<len(s):
#     s1 = s[::-1]
#     n+=1
# print(s1)

#FUNCTION CALLING EXAMPLE

# def add(x,y):
#     print(x+y)
#
# add(5,6)

#A function takes variable number of positional arguments as input. How to check if the arguments that are passed are more than 5


# def chckvar(x):
#     if x>5:
#         print("argument passed are more than 5")
#     else:
#         print("argument is less than 5")
# chckvar(9)

#Build a list of tuples with string and its length pair

# l = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
# l1 = []
# for i in l:
#     t = (i,len(i))
#     l1.append(t)
#     print(l1)

#List comprehension to sum the factorial of numbers from 1-5

# l = []
# f = 1
# for i in range(1,5+1):
#     f=f*i
#     print(f)

#WAP TO PRINT LIST OF EVEN NO WITH IN 10 USING LIST COMPREHENSION:

# l1 = [i for i in range(11) if i%2==0]
# print(l1)


#Reverse the string if the string is of odd length, otherwise keep it as is.
# l = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
# odd= []
# even=[]
# for i in l:
#     if len(i)%2!=0:
#         s=i[::-1]
#         odd.append(s)
#     else:
#         even.append(i)
# print(odd)
# print(even)


#Write a program to search for a character in a given string and return the corresponding index.

# s = "hello"
# l = []
# n = input(str("enter the char:"))
# for i in s:
#     if i == n:
#         j = (i,s.index(i))
#         l.append(j)
# print(l)


#A function takes variable number of positional arguments as input. How to check if the arguments that are passed are more than 5

# def chck_(x):
#     if x>5:
#         print("argument passed is more than 5")
#     else:
#         print("argument passed is less than 5")
#
#
# chck_(2)
# chck_(6)
# chck_(1230)
