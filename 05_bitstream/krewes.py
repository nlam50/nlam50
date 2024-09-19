# Nia Lam
# peaches & mangoes
# SoftDev
# K05
# 2024-09-17
# time spent: 0.8

# warning: will not work if "$$$" or "@@@" are substrings of names


import random
k = open('krewes.txt')


k_str = k.read()
# k.read() is a string
# print(k_str[0])


# list of dictionaries representing each devo
# each dictionary is of the form {<name>: [<period>, <ducky>]}


k_list = k_str.split("@@@")
# k_list is a list of devos, with $$$ still included
# print(k_list)


k_list2 = []
for i in k_list:
    info = i.split('$$$')
    k_list2.append({info[1]:[info[0], info[2]]})
# k_list2 is a list of dictionaries, each one corresponding to a devo
# print(k_list2)
random_devo = random.choice(k_list2)
# randomly selected a devo
print("Devo: " + list(random_devo.keys())[0])
print("Period: " + list(random_devo.values())[0][0])
print("Ducky name: " + list(random_devo.values())[0][1])
# prints random devo's name, period, and ducky name
