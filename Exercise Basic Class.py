#!/usr/bin/env python
# coding: utf-8

#  Write a Python class,
# 
#  MedPlus, that has three instance variables of type str, int, and float, that respectively represent the name of the medicine, batch number, and its price.
#  
#  Your class must include a constructor method that initializes each variable to an appropriate value, and your class should include methods for setting the value of each type, and retrieving the value of each type
#  
#  If the user passes invalid parameters to the constructor method in that case raise an appropriate error to the user of your class
# 
#  
# 

# In[5]:


class MedPlus:
    def __init__(self, name: str, batch_num: int, price: float):
        if not isinstance(name, str):
            raise TypeError("name should be a string")
        if not isinstance(batch_num, int):
            raise TypeError("batch_num should be an integer")
        if not isinstance(price, float):
            raise TypeError("price should be a float")
        
        self.name = name
        self.batch_num = batch_num
        self.price = price

    def set_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("name should be a string")
        self.name = name

    def set_batch_num(self, batch_num: int):
        if not isinstance(batch_num, int):
            raise TypeError("batch_num should be an integer")
        self.batch_num = batch_num

    def set_price(self, price: float):
        if not isinstance(price, float):
            raise TypeError("price should be a float")
        self.price = price

    def  get_name(self): 
        return self.name

    def get_batch_num(self):
        return self.batch_num

    def get_price(self): 
        return self.price


# In[6]:


med = MedPlus("Aspirin", 12345, 2.99)

print(med.get_name())   
print(med.get_batch_num())   
print(med.get_price())   

med.set_name("Ibuprofen")
med.set_batch_num(54321)
med.set_price(4.99)

print(med.get_name())   
print(med.get_batch_num())   
print(med.get_price())   

