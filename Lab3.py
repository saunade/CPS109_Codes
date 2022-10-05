#Sanna B
#501154179
#Lab 3 Homework, Oct 2

def question_one(num): 
#checks if an integer is pos, neg, or 0
  
    if num > 0: #case 1: if number is positive, output will be positive
        print("number is positive!")
    elif num == 0: #case 2: if number = 0, output will be 0
        print("number is 0")
    else: #case 3: if number negative, output will be negative
        print("number is negative")

def question_two(num): 
#checks float if pos, neg, or 0, 
#also checks if absolute value is >1000 (large) or <1 (small)
  
    if num > 0:
        if num >= 1000:
            print("Value is a large positive number")
        elif num < 1:
            print("Value is a small positive number")
        else:
            print("Value is a positive number")
    elif num < 0:
        if num <= -1000:
            print("Value is a large negative number")
        elif num >= -1:
            print("Value is a small negative number")
        else:
            print("Value is a negative number")
    elif num == 0:
        print("value is 0")

def question_three(num): 
#checks int for the number of digits it has
  
  digits = len(str(num)) #grabs number of digits
  
  if num < 0: #turns negative number positive
    num *= -1
    
  if num <= 1000000: #case 1: num is any number below/equal to 1 mil
    print("num is ", digits,  "digit(s)") #outputs number of digits
  else:
    print("num is lots") #case 2: num is higher than 1 mil, prints lots

def question_four(num1, num2, num3): 
#checks 3 ints if the are the same or all diff
  
  if num1 == num2 == num3: #Case 1: all numbers are the same
    print("All numbers are the same")
    
  elif num1==num2 or num2==num3 or num3 == num1: #numbers neither all diff or all same
    print("neither")
    
  else: #numbers are all different
    print("All numbers are different")

def question_five(num1, num2, num3): 
#checks numbers if they are in ascending/descending or neither order
#does not include same numbers (ex: 3 3 4 counts as neither)
  
  if num1 < num2 < num3: #checks numbers are in ascending order
    print("List is in ascending order")
    
  elif num1 > num2 > num3: #checks if numbers are in descending order
    print("List is in descending order")
    
  else: #number is neither ascending or descending
    print("List is neither in ascending or descending order")

def question_six(user_input, num1, num2, num3): 
#asks user for lenient or strict mode
#lenient: checks if numbers are in ascending/descending order
  #includes same numbers (example: 3 3 4 counts as ascending)
#strict: checks if in ascending/descending order but does not include same numbers (example: 3 3 4 counts as neither)
  
  if user_input == "lenient": #if user inputs lenient, programs include similar numbers
    lenient = True
    strict = False
  elif user_input == "strict": #strict mode enabled
    strict = True
    lenient = False
    
  if lenient==True: #lenient mode includes equals
    if num1 <= num2 <= num3: #case one: ascending mode
      print("list is in ascending order")
      
    elif num1 >= num2 >= num3: #case 2: descending mode
      print("list is in descending order")
      
    else: #case 3: neither
      print("neither")
      
  elif strict==True: #strict mode, not including equals
    if num1 < num2 < num3: #case 1: ascending
      print("list is in ascending order")
      
    elif num1 > num2 > num3: #descending
      print("list is in descending order")
      
    else: #neither
      print("neither")

def question_seven(num1, num2, num3):
#checks if list is in order
  #in order if it is ascending or descending
  
  if num1 <= num2 <= num3 or num1 >= num2 >= num3: #if in ascending/descending it is in order
    print("list is in order")
    
  else: #else it isnt in order
    print("list is not in order")


def question_eight(num1, num2, num3, num4): 
#checks if there are 2 pairs of numbers (example: 3 3 4 4) 
  # does not count if 3 numbers are the same (3 3 3 4 only one pair)
  
  if num1==num2==num3==num4: #all numbers are the same = 2 pairs
    print("there are 2 pairs")
    
  elif num1 == num2 or num1== num3 or num1 ==num4: #finds if there is one pair
    
    if (num2 == num3 or num3==num4 or num4==num2) and (num2!=num1 and num3 != num1 and num4 != num1): #finds the second pair, but excludes the same number as 1
      print("there are two pairs")
      
    else:
      print("there are no two pairs")
  
  else:
    print("there are no two pairs")
    
def question_nine(unit, temperature): 
#takes temperature in F or C
#then outputs if water will be solid, liquid or gaseous in that temp
  
  unit = unit.upper() #makes unit upper case for to fit code
  
  if unit == "C": #temperature will be in celsius
    if temperature <= 0: #water is solid below/equal 0
      print("Water will be solid")
    elif temperature >= 100: #water is gaseous above 100
      print("Water will be gaseous")
    else: #liquid between 0 - 100
      print("Water will be liquid")
  elif unit == "F": #temperature will be in farenheit
    if temperature <= 32: #solid below 32
      print("water will be solid")
    elif temperature >= 212: #gaseous above 212
      print("water will be gaseous")
    else: #liquid between 32 - 212
      print("water will be liquid")

def question_ten(letter_grade): 
#converts letter grade A, B, C, D to numeric value
#A=4, B=3, C=2, D=1, F=0,  - = -0.3  + = +0.3
  
  numeric_value = 0 #sets variable value at 0
  letter_grade = letter_grade.upper() #in case user submits lower case, it will upper case the character
  
  if len(letter_grade) > 1: #if there is + or - following the letter it will run this condition and add/subtract 0.3
    if letter_grade[1] == "+":
      numeric_value += 0.3
    elif letter_grade[1] == "-":
      numeric_value -= 0.3
    
  if letter_grade[0] == "A": #if letter grade = A, + 4
    numeric_value += 4
  elif letter_grade[0] == "B": #if letter grade = B, +3
    numeric_value += 3
  elif letter_grade[0] == "C": #if letter grade = C, +2
    numeric_value += 2
  elif letter_grade[0] == "D": #if letter grade = D, +1
    numeric_value += 1
  elif letter_grade[0] == "F": #if letter grade = F, +0
    numeric_value = 0

  print("your letter grade in numeric value is ", numeric_value)
  #prints numeric value to user
  
if __name__ == "__main__":
  
  question_one(int(input("Enter your number for question 1 here: ")))
  
  question_two(float(input("Enter your floating number for question two here: ")))
  
  question_three(int(input("enter your number for question 3 here: ")))
  
  question_four(int(input("number 1: ")), int(input("number 2: ")), int(input("number 3: ")))
  
  question_five(int(input("number 1: ")), int(input("number 2: ")), int(input("number 3: ")))

  question_six(input("Enter lenient or strict: "), int(input("number 1: ")), int(input("number 2: ")), int(input("number 3: ")))

  question_seven(int(input("number 1: ")), int(input("number 2: ")), int(input("number 3: ")))

  question_eight(int(input("number 1: ")), int(input("number 2: ")), int(input("number 3: ")), int(input("number 4: ")))
  
  question_nine(input("is the temperature you are about to input in C or F? "), float(input("what is the temperature: ")))

  question_ten(input("Enter the letter grade: "))