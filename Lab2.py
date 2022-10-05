#program slices a string by creating a list that has the desired amount of characters the user wants

def slice_string(word, slice): #function that slices string
  counter = 0
  list1=[] #creates an empty list to fill
  
  if slice < 0: #first case, user inputs negative number
    print("invalid input")
  elif word == "-1": #second case, user inputs end key
    print("Good bye!")
  else: #third case, user inputs string and slice correctly
    for i in range(len(0, word), slice):
      str_add = word[counter:(counter+slice)] #creates a string that will be soon added to a list
      list1.append(str_add) #adds new string created to a list
      counter+=slice #counter then adds by the users wished amnt of slices
    print(list1) #prints the list user wished for
  
if __name__ == "__main__": 
  slice_string(input("Enter your word here or -1 to end program: "), int(input("Enter how many characters per slice you want: "))) #grabs users word and number of characters per slice
