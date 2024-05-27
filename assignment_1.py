#Sanna Balouchi
#Assignment 1

#this program solves the repetitive calculations involving vectors in physics. gives the magnitude, unit vector, and sum/difference if needed

import math #imported to allow me to use the square root function

def welcome_user():
#prints an introduction to user so it does not constantly display when user chooses to use calculator again
  
  #prints how user should format the value to be inputted
  print("Before entering values, remove expressions and enter every digit.\nDo not enter in significant digit form.\n")

def run_again():
#asks user if it wants to use the calculator again instead of making them reset the program

  #asks user if they want to run the program again or not
  user_decision = input("Do you want to calculate again?\nType 'YES' for yes\nType 'NO' for no\n")

  #if user says "yes" or "YES" it will run the program again
  if user_decision.upper() == "YES":
    vector_calculator() #runs the calculator all over again

  #if user says "no" or "NO" it will not run the program again
  elif user_decision.upper() == "NO":
    print("\nBye Bye!") #says good bye to user and program then ends

  #if they put an incorrect input, the prompt is asked again
  else:
    run_again() 
  
def unit_vector(magnitude, vector_x, vector_y, vector_z):
#function calculates the unit vector by using equation vector/magnitude

  unit_vector_x = vector_x / magnitude #calculates the unit vector x
  unit_vector_y = vector_y / magnitude #calculates the unit vector x
  unit_vector_z = vector_z / magnitude #calculates the unit vector x

  #creates the unit vectors xyz into a list form
  unit_vector = [unit_vector_x, unit_vector_y, unit_vector_z]

  return unit_vector #returns value to be used

def vector_magnitude(vector_x, vector_y, vector_z):
#calculates the magnitude of the vector

  #calculates the magnitude by adding each vector component squared, then finding the square root of the sum
  magnitude = math.sqrt(vector_x**2 + vector_y**2 + vector_z**2)
  
  return magnitude #returns magnitude to be used later in program

def vector_addition(vector_one_x, vector_one_y, vector_one_z, vector_two_x, vector_two_y, vector_two_z):
#calculates the sum of two vectors
  
  #adds x1 and x2 to create resultant x
  resultant_x = vector_one_x + vector_two_x 
  #adds y1 and y2 to create resultant y
  resultant_y = vector_one_y + vector_two_y 
  #adds z1 and z2 to create resultant z
  resultant_z = vector_one_z + vector_two_z 

  #creates a list holding resultant vectors xyz coordinates
  resultant = [resultant_x, resultant_y, resultant_z]

  return resultant #returns resultant vector coordinates

def vector_subtraction(vector_one_x, vector_one_y, vector_one_z, vector_two_x, vector_two_y, vector_two_z):
#calculates the difference of two vectors

  #subtracts x2 from x1
  resultant_x = vector_one_x - vector_two_x
  #subtracts y2 from y1
  resultant_y = vector_one_y - vector_two_y
  #subtracts z2 from z1
  resultant_z = vector_one_z - vector_two_z

  #creates a list holding resultant vectors xyz coordinates
  resultant = [resultant_x, resultant_y, resultant_z]

  return resultant #returns resultant vectors coordinates

def vector_calculator():
#displays and takes values for user

  #collects value for vector one's x-coordinate
  vector_one_x = float(input("Enter values for the first vector\nEnter the x-value: "))
  #collects value for vector one's y-coordinate
  vector_one_y = float(input("Enter the y-value: "))
  #collects value for vector one's z-coordinate
  vector_one_z = float(input("Enter the z-value: "))

  #collects value for vector two's x-coordinate
  vector_two_x = float(input("\nEnter values for the second vector\nEnter the x-value: "))
  #collects value for vector two's y-coordinate
  vector_two_y = float(input("Enter the y-value: "))
  #collects value for vector two's z-coordinate
  vector_two_z = float(input("Enter the z-value: "))

  #caclulates vector ONE magnitude by using magnitude function
  vector_one_magnitude = vector_magnitude(vector_one_x, vector_one_y, vector_one_z)
  #calculates vector TWO magnitude by using magnitude function
  vector_two_magnitude = vector_magnitude(vector_two_x, vector_two_y, vector_two_z)

  #calculates vector ONE's unit vector using unit vector function
  unit_vector_one = unit_vector(vector_one_magnitude, vector_one_x, vector_one_y, vector_one_z)
  #calculates vector TWO's unit vector using unit vector function
  unit_vector_two = unit_vector(vector_two_magnitude, vector_two_x, vector_two_y, vector_two_z)

  #displays to user the vectors magnitude of both vectors
  print("\nVector one's magnitude: %s\nVector two's magnitude: %s" %(vector_one_magnitude, vector_two_magnitude))
  #displays to user the unit vector value of both vectors
  print("Unit vector one: %s\nUnit vector two: %s" %(unit_vector_one, unit_vector_two))

  #asks the user if they want to add or subtract the vectors
  operation = input("\nWhat operation do you want to do? input the corresponding number\n1. Vector addition\n2. Vector subtraction - r1-r2\n3. Difference - r2-r1\n4. None. Quit the program\n")

  #runs if user wants vector addition
  if operation ==  "1":
    #resultant runs addition function with values given earlier
    resultant = vector_addition(vector_one_x, vector_one_y, vector_one_z, vector_two_x, vector_two_y, vector_two_z)
    #prints the resultant vectors value
    print("Here is the addition resultant vector: %s"%resultant)

    #asks the user if it wants to run the program again for more calculations
    run_again()

  #runs if user wants to do vector subtraction (r1-r2)
  elif operation == "2":
    #resultant is given by the subtraction function with values given
    resultant = vector_subtraction(vector_one_x, vector_one_y, vector_one_z, vector_two_x, vector_two_y, vector_two_z)
    #prints the resultant vectors value
    print("Here is the subtraction resultant vector: %s"%resultant)

    #asks the user if it wants to run the program again for more calculations
    run_again()

  #runs if user wants to find the difference between the two vectors
  elif operation == "3":
    #resultant is given by the subtraction functions with values given
    resultant = vector_subtraction(vector_two_x, vector_two_y, vector_two_z, vector_one_x, vector_one_y, vector_one_z)
    #prints the resultant vectors value
    print("Here is the difference resultant vector: %s"%resultant)

    #asks the user if it wants to run the program again for more calculations
    run_again()

  #ends the program if user does not want to do vector addition/subtraction
  elif operation == "4":
    print("Hope you got what you wanted!")

  #ends the program because user did not input 1/2/3/4
  else:
    print("invalid input")
  
if __name__ == "__main__":
  welcome_user()
  vector_calculator() #runs the main program, the calculator
