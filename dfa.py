import sys

# La roche-posay

# Main Program
psi = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
pi = ['.']
phi = ['@']

# [x for x in original_list if x not in excluded_elements]

# Trap state (Q10) for non-specified states
# def q10(string):
#    print(f'{string[0]}: Q10')

# State Q9
def q9(string):
    if not len(string):
        print("Success")
    # . -> Q5 
    elif len(string)>1 and string[0] in pi:
        print(f'{string[0]}: Q5')
        string = string[1:]
        q5(string)
    # E -> Q4
    elif len(string)>1 and string[0] in psi:
        print(f'{string[0]}: Q4')
        string = string[1:]
        q4(string)
    else: 
        string = string[1:]
        for i in string:
            print(f'{string[0]}: Q10')
        
        print("Alphabet is in trap state")

# State Q8
def q8(string):
    if not len(string):
        print("Success")
    # . -> Q5 
    elif len(string)>1 and string[0] in pi:
        print(f'{string[0]}: Q5')
        string = string[1:]
        q5(string)
    # E -> Q4
    elif len(string)>1 and string[0] in psi:
        print(f'{string[0]}: Q4')
        string = string[1:]
        q4(string)
    else: 
        string = string[1:]
        for i in string:
            print(f'{string[0]}: Q10')
        
        print("Alphabet is in trap state")

# State Q7
def q7(string):
    # . -> Q5 
    if len(string)>1 and string[0] in pi:
        print(f'{string[0]}: Q5')
        string = string[1:]
        q5(string)
    # E-{v} -> Q4
    elif len(string)>1 and string[0] in [x for x in psi if x not in ['v']]:
        print(f'{string[0]}: Q4')
        string = string[1:]
        q4(string)
    # v -> Q9 
    elif string[0] == 'v':
        print(f'{string[0]}: Q9')
        string = string[1:]
        q9(string)
    else: 
        string = string[1:]
        for i in string:
            print(f'{string[0]}: Q10')
        
        print("Alphabet is in trap state")

# State Q6
def q6(string):
    # o -> Q7 
    if len(string)>1 and string[0] == 'o':
        print(f'{string[0]}: Q7')
        string = string[1:]
        q7(string)
    # r -> Q8, gr - FINALE 
    elif string[0] == 'r':
        print(f'{string[0]}: Q8')
        string = string[1:]
        q8(string)
    # E-{o,r} -> Q4 
    elif len(string)>1 and string[0] in [x for x in psi if x not in ['o', 'r']]:
        print(f'{string[0]}: Q4')
        string = string[1:]
        q4(string)
    # . -> Q5 
    elif len(string)>1 and string[0] in pi:
        print(f'{string[0]}: Q5')
        string = string[1:]
        q5(string)
    else: 
        string = string[1:]
        for i in string:
            print(f'{string[0]}: Q10')
        
        print("Alphabet is in trap state")

# State Q5
def q5(string):
    # g -> Q6 
    if len(string)>1 and string[0] == 'g':
        print(f'{string[0]}: Q6')
        string = string[1:]
        q6(string)
    # E-{g} -> Q4 
    elif len(string)>1 and string[0] in [x for x in psi if x not in ['g']]:
        print(f'{string[0]}: Q4')
        string = string[1:]
        q4(string)
    else: 
        string = string[1:]
        for i in string:
            print(f'{string[0]}: Q10')
        
        print("Alphabet is in trap state")

# State Q4
def q4(string):
    # . -> Q5
    if len(string)>1 and string[0] in pi:
        print(f'{string[0]}: Q5')
        string = string[1:]
        q5(string)
    # E -> Q4
    elif len(string)>1 and string[0] in psi:
        print(f'{string[0]}: Q4')
        string = string[1:]
        q4(string)
    else: 
        string = string[1:]
        for i in string:
            print(f'{string[0]}: Q10')
        
        print("Alphabet is in trap state")

# State Q3
def q3(string):
    # E -> Q3
    if len(string)>1 and string[0] in psi:
        print(f'{string[0]}: Q3')
        string = string[1:]
        q4(string)
    else: 
        string = string[1:]
        for i in string:
            print(f'{string[0]}: Q10')
        
        print("Alphabet is in trap state")

# State Q2
def q2(string):
    # E -> Q2
    if len(string)>1 and string[0] in psi:
        print(f'{string[0]}: Q2')
        string = string[1:]
        q2(string)
    # . -> Q1
    elif len(string)>1 and string[0] in pi:
        print(f'{string[0]}: Q1')
        string = string[1:]
        q1(string)
    # @ -> Q3
    elif len(string)>1 and string[0] in phi:
        print(f'{string[0]}: Q3')
        string = string[1:]
        q3(string)
    else:
        string = string[1:]
        for i in string:
            print(f'{string[0]}: Q10')

        print("Alphabet is in trap state")

# State Q1
def q1(string):
    # E -> Q2
    print(f"'{string[0]}' started on State Q1\n")

    if len(string)>1 and string[0] in psi:
        print(f'{string[0]}: Q2')
        string = string[1:]
        q2(string)
    else:
        string = string[1:]
        for i in string:
            print(f'{string[0]}: Q10')


        print("Alphabet is in trap state")


n = int(input("Please enter number of iterations: "))

# This block of code iterates through every letter in the string and runs them through the state machine
for i in range(n):
    str_ = input(f'\nEnter string {i+1} of {n}: ')
    q1(str_)
