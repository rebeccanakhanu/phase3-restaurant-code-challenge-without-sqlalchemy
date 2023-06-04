#!/usr/bin/env python3



if __name__ == '__main__':
#  WRITE YOUR TEST CODE HERE ###
 class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)
        
class Customer:
    all_customers = []
    
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []
        Customer.all_customers.append(self)
        
    def set_given_name(self, given_name):
        self.given_name = given_name
        
    def set_family_name(self, family_name):
        self.family_name = family_name
        
    def full_name(self):
        return f"{self.given_name} {self.family_name}"
    

customer1 = Customer("mary", "John")






# DO NOT REMOVE THIS                 
ipdb.set_trace()
