#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:18:19 2018

@author: patrick
"""
import time
operators = ['^','*','/','+','-']

class Stack:
     def __init__(self, items = []):
         self.items = items

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self, index = None):
         if index != None and is_number(index):
             return self.items.pop(index)
         else:
             return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
     

class OperandPairs:
    position = None
    operand1 = None
    operand2 = None
    operator = None
    
    def __init__(self, operand1, operand2, operator):
        self.operand1 = operand1
        self.operand2 = operand2
        self.operator = operator
        

    def to_postfix(self):
        return (self.operand1 if self.operand1 != None else '') \
            + (' ' + self.operand2 if self.operand2 != None else '') \
            + ' ' + self.operator

    def __str__(self):
       return self.to_postfix()
    
def to_postfix(in_flux):
   
    #clean up infix
    infix = in_flux.replace('\s','').replace('(', ' ( ').replace(')', ' ) ')
    for o in operators:
        infix = infix.replace(o,' ' + o + ' ')
    
    infix_list = eval_infix(infix.split(' '), operators)
    infix_list = [str(y).strip() for y in infix_list if y not in ['(',')']]
    infix_list = eval_infix(infix_list, operators)
    
    return " ".join([str(i).strip() for i in infix_list])

def eval_infix(infix_list, operators):
    for oi, o in enumerate(operators):
        for vi, v in enumerate(infix_list):
            if v == o:
                print(infix_list[vi],infix_list[vi-1])
                infix_list[vi-1] = OperandPairs(
                    str(infix_list[vi-1]) if infix_list[vi-1] != None else None,
                    str(infix_list[vi+1]) if infix_list[vi+1] != None else None,
                    o
                )
                infix_list[vi] = None
                infix_list[vi+1] = None
        infix_list = [str(y).strip() for y in infix_list if y not in (None,'', ')', '(') ] 
    return infix_list
     
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

def calculat_postfix(postfix):
    
    values = [y.strip() for y in postfix.split(' ')]

    results = []
    for i, p in enumerate(values):
        if p in operators:
            results[-2] = float(do_math(results[-2], results[-1], p))
            del results[-1]
        elif is_number(p):
            results.append(float(p))
    return results[0]
def do_math(v1, v2, p):
    if p == "*":
        return float(v1) * float(v2)
    if p == "/":
        return float(v1) / float(v2)
    if p == "+":
        return float(v1) + float(v2)
    if p == "-":
        return float(v1) - float(v2)
    if p == "^":
        return int(v1) ** int(v2)
    return 0

infix = input("infix:")

start_time = time.time()
print("PostFix: %s" % to_postfix(infix))
print("Result: %s" % calculat_postfix(to_postfix(infix)))

print("Execution Time: %s seconds" % (time.time() - start_time))
#print(to_postfix(input("influx:")))