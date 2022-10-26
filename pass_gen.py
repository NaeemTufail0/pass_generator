#!/usr/bin/python3

import random

import string_utils

lower_alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

upper_alpha=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

digits=['0','1','2','3', '4', '5', '6', '7', '8', '9']

symbols=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']

pass_len=input("Enter the length of your password")

#picking at least one from every list
temp_pass=""
temp_pass=temp_pass+random.choice(lower_alpha)
temp_pass=temp_pass+random.choice(upper_alpha)
temp_pass=temp_pass+random.choice(digits)
temp_pass=temp_pass+random.choice(symbols)


#generating pasword
combined_list=lower_alpha+upper_alpha+digits+symbols
final_pass=""

for x in range(int(pass_len)-4):
	final_pass=final_pass+random.choice(combined_list)

#adding 4 digit pick from all lists to password
final_pass=final_pass+temp_pass

#shuffling our final password
final_pass=string_utils.shuffle(final_pass)

print(final_pass)


print("Hello")












