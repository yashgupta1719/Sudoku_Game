# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 15:49:42 2020

@author: yash1719
"""
def print_board(bo):
    for i in range(9):
        if i%3==0 and i!=0:
            print("---------------------------")
        for j in range(9):
            if j%3 ==0 and j!=0:
                print("|",end=" ")
            if j==8:
                print(bo[i][j])
            else:
                print(bo[i][j],end=" ")
def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if(bo[i][j]==0):
                return (i,j)
    return None
def valid(bo,num,pos):
    #check row
    for j in range(9):
        if(bo[pos[0]][j]==num and pos[1]!=j):#As the empty can be found at any location so and we need to starting searching only the row in which the empty was not found and not from the start of the table
            return False
    #check column
    for i in range(9):
        if(bo[i][pos[1]]==num and pos[0]!=i):
            return False
    bx=pos[1]//3
    by=pos[0]//3
    for i in range(by*3,by*3+3):
        for j in range(bx*3,bx*3+3):
            if bo[i][j]==num and (i,j)!=pos:
                return False
    return True
def solve(bo):
    find=find_empty(bo)
    if(find==None):
        return True
    else:
        row,col = find
    for i in range(1,10):
        if(valid(bo,i,(row,col))==True):
            bo[row][col]=i
            if(solve(bo)==True):
                return True
            bo[row][col]=0
    return False

                
            
    
