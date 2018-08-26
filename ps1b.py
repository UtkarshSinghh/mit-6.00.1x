# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 23:39:30 2018

@author: Lenovo
"""

annual_salary=(float)(input("Enter your annual salary:"))
portion_saved=(float)(input("Enter the portion of salary saved per month:"))
total_cost=(float)(input("Enter the cost of your home:"))
semi_annual_raise=(float)(input("Enter the semi annual raise: "))
down_payment=0.25*total_cost
r=0.04
n=0
savings=0.0
while savings<=down_payment :
    n+=1
    savings=((annual_salary/12)*portion_saved)+(savings*r/12)+savings
    if n%6==0:
        annual_salary+=(annual_salary*semi_annual_raise)
print("The number of months it will take are:",n)
