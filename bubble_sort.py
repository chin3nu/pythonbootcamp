""" 
BUBBLE SORT A LIST OF NUMBERS
"""


def bs(a):   
    b=len(a)-1

    for x in range(b):
        for y in range(b-x):
            if a[y]>a[y+1]:
                a[y],a[y+1]=a[y+1],a[y]
    return a
