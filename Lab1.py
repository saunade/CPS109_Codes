#grabbing user input to assign values to h,w,l
#basic program

height = int(input("Enter the height of the rectangular prism: "))
width = int(input("Enter the width of the rectangular prism: "))
length = int(input("Enter the length of the rectangular prism: "))

#using h,w,l to solve rectangular prism surface area and volume equations
volume = width*length*height #v=whl
surfaceArea = 2*(width*length+height*length+height*width) #v=2(wl+hl+hw)

print("The volume of your prism is", volume, "and your surface area is", surfaceArea) #outputs answ
