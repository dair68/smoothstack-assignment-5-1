# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 14:55:59 2022
Smoothstack assignment 5-1
@author: Grant Huang
"""

#calculates person's bmi based on weight and height
#@param weight - person's weight in km
#@param height - person's height in m
#spits out bmi as float based on weight and height
def bmi(weight, height):
    return weight/height**2

#determines person's bmi grade based on bmi
#@param bmi - bmi as positive float
#spits out under, normal, over, or obese weight based on bmi
def bmiGrade(bmi):
    #spitting out grade based on bmi
    if bmi <= 0:
        return "invalid"
    elif bmi < 18.5:
        return "under"
    elif bmi < 25.0:
        return "normal"
    elif bmi < 30.0:
        return "over"
    else:
        return "obese"

numPeople = int(input("input data: "))
#print(numPeople)

people = []

#storing inputed weight (km) and height (m) of each person
for n in range(numPeople):
    stats = input().split(" ")
    people.append((float(stats[0]), float(stats[1])))
    
#print(people)
    
bmis = [bmiGrade(bmi(p[0], p[1])) for p in people]
print("\nanswer: ")
print(" ".join(bmis))  
