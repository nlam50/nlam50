# Nia Lam
# peaches & mangoes
# SoftDev
# K<nn> -- <RandomDevo/Lists, Dictionaries, and Random Selection/Function to randomly select a devo... (Aim for concision, brevity, CLARITY. Write to your future self...)>
# <yyyy>-<mm>-<dd>
# time spent: <elapsed time in hours, rounded to nearest tenth>
# #DISCO:
# QCC:
# OPS SUMMARY:
import random

# krewes = {
#            4: [ 
# 		'DUA','TAWAB','EVA','JACK','VICTOR','EVAN','JASON','COLYI','IVAN','TANZEEM',
# 		'TAHMIM','STANLEY','LEON','NAOMI','NIA','ANASTASIA','JADY','BRIAN','JACOB',
# 		'ALEX','CHONGTIAN','DANNY','MARCO','ABIDUR','ANKITA','ANDY','ETHAN','AMANDA',
# 		'AIDAN','LINDA','QIANJUN','JIAYING','KISHI'
#         ],
#            5: [ 
#                 'ADITYA','MARGIE','RACHEL','ALEXANDER','ZIYAD','DANNY','ENDRIT','CADEN',
#                 'VEDANT','SUHANA','KYLE','KEVIN','RAYMOND','CHRISTOPHER','JONATHAN','SASHA',
#                 'NAFIYU','TIM','WILL','DANIEL','BENJAMIN','CLAIRE','CHLOE','STELLA','TRACY',
#                 'JESSICA','JACKIE','WEN YUAN','YINWEI','TIFFANY','JAYDEN DANIEL','PRINCEDEN'
#                 ]
#          }

krewes = {
           4: [ 
		'DUA','TAWAB','EVA'
        ],
           5: [ 
                'ADITYA','MARGIE','RACHEL'
                ]
         }

def random_devo(krewes):
    # rand_key -> random key index
    # keys_list -> list of keys
    # keys -> random key
    # values -> value of random key (list in our case)
#     rand_key = random.randrange(0, len(krewes))
#     keys_list = krewes.keys()
#     keys = keys_list[rand_key]
#     # keys() -> returns keys of dictionary (as list)
#     values = (keys)
#     print(values)

    
    
random_devo(krewes)
    