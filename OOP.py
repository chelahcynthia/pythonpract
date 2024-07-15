# Types of variables
class Car:
    
    wheels = 4
    
    # defining variable inside init is instance variable 
    # defining variable outside init is class variable
    # namespace - where you create and store objects/variables
    
    def __init__(self):
        # Instance variables : as the object changes the value also change
        self.mil = 10
        self.com = "BMW"
    
    # Types of methods:
    #   instance methods
    # class methods
    # static methods
        

class Student:
    # static variable
    school = 'Chelah'
    
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
       
        #instance method 
        # self - belong to a particular object.
    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3
    
    
# Inheritance
class A:
    def feature1(self):
        print("Feature 1 is working")
    def feature2(self):
        print("Feature 2 is working")
        

class B(A):
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")
        
        
# Polymorphism
# how to achieve polymorphism:
#   duck typing
#   operator overloaading
#   method overloaading
#   method overriding

# Valid Palindrome
class Solution:
    def is_palindrome(self, s: str) -> bool:
        # remove non-alphanumeric characters using extra memory
        newStr = ""
        
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[:: -1]
    
# Not using extra space. Constant extra memory(not creating a new version of the string)
# instead of reversing, we can use pointers to check the left and right side until they eventually meet in the middle 







              


        




           
             