'''
Zaden Swain
caseStudy.py
Takes student's names and determines if they are in dean's list or honor roll
'''
#gets first and last name and gpa from user and stores them in variables
last_name = input('Enter Last Name: ')

#ends program if ZZZ is entered in last name
if last_name == 'ZZZ':
    quit()

first_name = input("Enter First Name: ")

GPA = float(input("Enter GPA: "))

#checks to see where the inputed information qualifies.
if GPA >= 3.5:
    print("Congratulation, you've made the Dean's list!")
    
elif GPA >= 3.25:
    print("Congrats, you've made honor roll!")
    
else: print("Sorry you did not qualify for either.")