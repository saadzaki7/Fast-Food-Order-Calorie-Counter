#Name: Saad Zaki
#Date: Oct,2
#File Name: P0201.Zaki.Saad
#Description: A program that displays a menu and then asks the user to press
#Enter. Then it asks them to pick one of the options by pressing 1-4. Afterwards
#it determins their orders calories.

#input - Prints menu and asks which food they want
print("Welcome to Saad's Fast Fooderia!")
print("\nBurgers:\t\t\t\t Drinks:")
print("********\t\t\t\t *******")
print("1 - Cheeseburger(470 Calories)\t\t 1 - Coke(100 Calories)")
print("2 - Beyond Meat Burger(200 Calories)\t 2 - Orange Juice(20 Calories)")
print("3 - Veggie Burger(250 Calories)\t\t 3 - Smoothie(150 Calories)")
print("\nSide Orders:\t\t\t\t Desserts:")
print("************\t\t\t\t *********")
print("1 - Fries(250 Calories)\t\t\t 1 - Cake(300 Calories)")
print("2 - Poutine(400 Calories)\t\t 2 - Swiss Rolls(400 Calories)")
print("3 - Onion Rings(280 Calories)\t\t 3 - Sundae(410 Calories)")

#Pauses the program to have them press enter & guides the user
enter = input("\nPlease take a moment to read our menu. Press Enter to\
 continue ...")
print("\nNow enter your choice of food")
print("Enter 4 if you do not want any one of the options")

#Asks the user what items they want from the menu and forces them to write a
#number between 1 and 4 by using while loops.

burger= int(input("\nBurger choice:"))
while burger>4 or burger<0:
    burger= int(input("Please choose a number between 1-4:"))
    
drink=int(input("Drink choice:"))
while drink>4 or drink<0:
    drink= int(input("Please choose a number between 1-4:"))

sideOrder=int(input("Side Order choice:"))
while sideOrder>4 or sideOrder<0:
    sideOrder= int(input("Please choose a number between 1-4:"))
    
dessert=int(input("Dessert choice:"))
while dessert>4 or dessert<0:
    dessert= int(input("Please choose a number between 1-4:"))
    
#Process
#burger choice calories - depending on the users choice adds on the appropriate
#amount of calories, to the variable "calories"

calories=0

if burger == 1:
    calories+= 470

elif burger ==2:
    calories+= 200

elif burger ==3:
    calories+= 250

elif burger ==4:
    calories +=0

else:
    print ("Your number was not between 1-4 please restart the program")

#drink choice calories
if drink == 1:
    calories+= 100

elif drink ==2:
    calories+= 20

elif drink ==3:
    calories+= 150

elif drink ==4:
    calories +=0

else:
    print ("Your number was not between 1-4 please restart the program")

#side order choice calories
if sideOrder == 1:
    calories+= 250

elif sideOrder ==2:
    calories+= 400

elif sideOrder ==3:
    calories+= 280

elif sideOrder ==4:
    calories +=0

else:
    print ("Your number was not between 1-4 please restart the program")

#Dessert order choice calories
if dessert == 1:
    calories+= 300

elif dessert ==2:
    calories+= 400

elif dessert==3:
    calories+= 410

elif dessert ==4:
    calories +=0

else:
    print ("Your number was not between 1-4 please restart the program")
    
#assigning 4 variables 0 to later assign them to the chosen items
itemOne=0
itemTwo=0
itemThree=0
itemFour=0

#Assigning itemOne to the choice of burger
if burger== 1:
    itemOne= "Cheeseburger"
elif burger ==2:
    itemOne="Beyond Meat Burger"
elif burger ==3:
    itemOne="Veggie Burger"
elif burger ==4:
    itemOne="No burger"
else:
    print("error")

#Assigning itemTwo to the choice of Drink
if drink== 1:
    itemTwo= "Coke"
elif drink ==2:
    itemTwo="Orange Juice"
elif drink ==3:
    itemTwo="Smoothie"
elif drink ==4:
    itemTwo="No drink"
else:
    print("error")

#Assigning itemThree to the choice of side order
if sideOrder== 1:
    itemThree= "Fries"
elif sideOrder ==2:
    itemThree="Poutine"
elif sideOrder ==3:
    itemThree="Onion Rings"
elif sideOrder ==4:
    itemThree="No side order"
else:
    print("error")

#Assigning itemFour to the choice of dessert
if dessert== 1:
    itemFour= "Cake"
elif dessert ==2:
    itemFour="Swiss Rolls"
elif dessert ==3:
    itemFour="Sundae"
elif dessert ==4:
    itemFour="No dessert order"
else:
    print("error")

#output
    
print("\nYou ordered", itemOne, itemTwo, itemThree,itemFour, sep=",")
print("Your total calorie count is:", calories, "Calories")
