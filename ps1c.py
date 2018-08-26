# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 23:42:13 2018

@author: Lenovo
"""
import random
annual_salary=(float)(input("Enter your annual salary:"))
total_cost=(float)(input("Enter the cost of your home:"))
semi_annual_raise=(float)(input("Enter the semi annual raise: "))
a=annual_salary
down_payment=0.25*total_cost
r=0.04
n=0
savings=0.0
bisect=random.random()
#bisect=.5
low=0.0
high=1.0
for i in range(1,13,1):
    savings=((annual_salary/12)*1)+(savings*r/12)+savings
    if i%6==0:
        annual_salary+=(annual_salary*semi_annual_raise)
if savings<down_payment:
    print("there is no possible saving")
    
else:
    n=1
    for i in range(1,13,1):
        if i==1:
            savings=0.0
            annual_salary=a
        savings=((annual_salary/12)*bisect)+(savings*r/12)+savings
        if i%6==0:
            annual_salary+=(annual_salary*semi_annual_raise)
    while abs(savings-down_payment)>1:
        
        if savings>down_payment:
            high=bisect
            bisect=(low+high)/2
            n+=1
        else:
            low=bisect
            bisect=(low+high)/2
            n+=1
        for i in range(1,13,1):
            if i==1:
                savings=0.0
                annual_salary=a
            savings=((annual_salary/12)*bisect)+(savings*r/12)+savings
            if i%6==0:
                annual_salary+=(annual_salary*semi_annual_raise)
        
    print("the best saving rate is",bisect)
    print("the iterations are",n)
