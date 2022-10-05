#Sanna B
#Lab 4, Loops

def question_one(even_sum):
#grabs the sum of all the even numbers from 2-100 inclusive
  
  counter = 0 #counter set up for while loop
  
  while counter <=100: #goes up to 100 inclusive
    
    if counter%2 == 0:#tests if number is even
      even_sum = even_sum + counter #adds even number to sum
      
    counter += 1 #increases counter by one each time to continue loop instead of creating infinite loop
      
  print("question one: %s"%even_sum)#should print 2550

def question_two(squares_sum):
#creates a sum of all the numbers (from 0-100) squared
  
  counter = 0

  while counter <= 100: #keeps range from 0-100
    
    squares_sum += counter**2 #adds number squared
    counter += 1

  print("question two: %s"%squares_sum)#should print 338350

def question_three():
#prints all the powers of 2 up until 20
  
  power = 0 #multiplies 2 by the power of this number

  sum_two = 0 #set to 0 in order to display proper num when printed

  print("**question three below**")
  
  while power <= 20:
    sum_two = 2**power #grabs the product of 2^n
    power += 1 #increases the power by one each time
    print(sum_two)#should print every power of 2

def question_four(begin, end):
#adds the sum of all odd numbers from a range the user defines
  
  counter = begin #in order to start from beginning, set counter to the beginning value
  odd_sum = 0 #sets the sum to 0
  
  while counter <= end: #stops once it reaches the end inclusive
    
    if counter%2 > 0: #if counter is odd, %2 will be above 0
      odd_sum += counter #adds the number to sum
      
    counter += 1 #prevents it from infinitely looping

  print("question four: %s"%odd_sum) #displays the sum of all the odd numbers

def question_five(user_number):
#takes an integer given by user and adds only the odd digits
  
  digit = "" #empty variable that will be filled with digit
  sum = 0 #setting sum to zero
  
  for i in range(len(user_number)): #i goes through all characters in the string user_number
    digit = user_number[i] #digit grabs the digit starting from left to right
    
    if int(digit)%2 > 0: #if digit is odd it will run statement
      sum += int(digit) #adds the odd digit to sum

  print(sum) #should print the value sum of all odd digits in the integer given

def question_six():
#takes 10 numbers from user and then displays the largest num
  
  counter = 1 #displays to user what number to submit
  compare = 0 #compares the number with the former largest num
  largest_odd = 0 #will be filled with the largest int
  
  while counter <=10:
    number = int(input("enter %s number for question six here: " %counter))
    #outputs to user to enter a number
    #collects that number to be compared
    
    if number%2 >0: #if odd statement will run
      
      if number > compare: #if number is larger than large_odd
        largest_odd = number #sets new large sum to current num
        compare = number #sets number to the current num to be used to compare the next numbers

    counter += 1 #stops loop from running infinitely
        
  print(largest_odd) #prints the largest odd number to user

def question_seven(sentence):
#reads sentence user inputted and grabs all the integers to add them up then outputs that sum
  
  sum = 0 #sets sum to zero to be called later

  for i in range(len(sentence)): #Checks every character in range of the entire sentence given by user
    
    if sentence[i].isdigit(): #checks each character for if it is a digit comes out true if character is a digit
      number_character = int(sentence[i]) #assigns the variable's value to the number found in sentence
      sum += int(number_character) #adds digit to sum

  print(sum)#prints all digits added up
  
def question_eight(float_list):
#collects a list of floats and adds them together
  
  sum = 0
  float_list = float_list.split(",") #splits string into list, each element starts/ends at the comma (non inclusive)

  for i in float_list: #i runs for every element in the list
    sum += float(i) #turns the string element into a float and adds

  print(sum) #prints all the floats added up together
  
if __name__ == "__main__":
  question_one(0)
  question_two(0)
  question_three()
  question_four(int(input("Enter the beginning of the range: ")), int(input("Enter the end of the range: ")))
  question_five(input("Enter the number for question five: "))
  question_six()
  question_seven(input("Enter your sentence for question 7 here: "))
  question_eight(input("Enter your float list for question 8 here: "))