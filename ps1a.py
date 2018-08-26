# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 22:21:39 2018

@author: Lenovo
"""

annual_salary=(float)(input("Enter your annual salary:"))
portion_saved=(float)(input("Enter the portion of salary saved per month:"))
total_cost=(float)(input("Enter the cost of your home:"))
down_payment=0.25*total_cost
r=0.05
n=0
savings=0.0
monthly_salary=annual_salary/12
while savings<=down_payment :
    n+=1
    savings=(monthly_salary*portion_saved)+(savings*r/12)+savings
print("The number of months it will take are:",n)
