#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 17:20:38 2019

@author: kartik
"""

pswd_lst = list(map(str, input().strip().split(',')))

pwd_lst = [i.strip() for i in pswd_lst ]

lst_not_allowed = ["[", "%", "!", "(", ")", "[" ] 
lst_must_have = ["*", "$", "_", "#", "=", "@" ]

for S in pwd_lst: # itereating over the different passwords
   
    NA_flg = False
    must_have_flg = False
    digit_flg = False
    lower_flg = False
    upper_flg = False
    
    for i in range(0,len(S)): # iterating over a single password
        
        #setting flags
        if S[i] in lst_not_allowed:
            NA_flg = True
        elif S[i] in lst_must_have:
            must_have_flg = True
        elif S[i].isdigit():
            digit_flg = True
        elif S[i].islower():
            lower_flg = True
        elif S[i].isupper():
            upper_flg = True                    
    
    #checking flags according to the conditions 
    if NA_flg == True:
       print(S,"Failure Password cannot contain [%!)(]")    
    elif (len(S)<6):
       print(S,"Failure Password must be 6 characters long")
    elif (len(S)>12):
       print(S,"Failure Password must be at max 12 characters long")
    elif lower_flg == False:
       print(S,"Failure Password must contain atleast one from a-z")
    elif upper_flg == False:
       print(S,"Failure Password must contain atleast one from A-Z")
    elif must_have_flg == False:
       print(S,"Failure Password must contain atleast one from *$_#=@")
    elif digit_flg == False:
       print(S,"Failure Password must contain atleast one from 0-9")         
    else:
       print(S,"Sucess")
       
         