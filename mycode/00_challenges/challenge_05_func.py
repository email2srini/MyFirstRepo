#!/usr/bin/env python3

# Create 3 functions

# A Math function that takes 2 required arguments, multiplies them together and then divides by 100 and returns the result

def math(a,b):
    result =(a*b)/100
    return result

#print(math(5,6))


# A stringy function that takes a required argument string and returns every other letter from the string
def stringy(txt):
    result = (txt[::1])
    return result

#print(stringy("abcdefg"))


# A main function that calls on both of these previous functions, which has 1 required aregument of an integer and has two default arguments (1 int and 1 string)

def main(num1, num2=20, txt1="mnbvcasdf"):
    print(math(num1,num2))
    print(stringy(txt1))
    
main(10)


