# # snake water gun game
#
# import random
# name=input("Enter your name :")
# clist = ["s","g","w"]
# chance = 10
# human_point = 0
# computer_point = 0
# chance_left=0
# print(" \t \t \t \t Snake,Water,Gun Game\n \t\t\t\t\t\t\t\t\t~Devloped by Tonmay\n ")
# print("press s for snake\npress w for water\npress g for gun\n\n")
# while chance_left<chance:
#     computer_choise = random.choice(clist)
#     human_choice = input('Snake,Water,Gun:')
#
#     if human_choice == computer_choise:
#         print("Both tie !")
#     elif computer_choise=="s" and human_choice=="g":
#         print(f"your guess {human_choice} and computer guess is {computer_choise} \n")
#         human_point=human_point+1
#         print(f"compute point = {computer_point} and human point = {human_point}")
#     elif computer_choise == "s" and human_choice == "w":
#         computer_point = computer_point + 1
#         print(f"your guess {human_choice} and computer guess is {computer_choise} \n")
#         print(f"compute point = {computer_point} and human point = {human_point}")
#
#
#     elif computer_choise =="g" and human_choice =="s":
#         computer_point = computer_point + 1
#         print(f"your guess {human_choice} and computer guess is {computer_choise} \n")
#         print(f"compute point = {computer_point} and human point = {human_point}")
#     elif computer_choise == "g" and human_choice == "w":
#         human_point=human_point+1
#         print(f"your guess {human_choice} and computer guess is {computer_choise} \n")
#         print(f"compute point = {computer_point} and human point = {human_point}")
#
#
#     elif computer_choise == "w" and human_choice == "s":
#         human_point=human_point+1
#         print(f"your guess {human_choice} and computer guess is {computer_choise} \n")
#         print(f"compute point = {computer_point} and human point = {human_point}")
#     elif computer_choise == "w" and human_choice == "g":
#         computer_point = computer_point + 1
#         print(f"your guess {human_choice} and computer guess is {computer_choise} \n")
#         print(f"compute point = {computer_point} and human point = {human_point}")
#     else:
#         print("Invalid choice")
#     chance_left = chance_left+1
#
# if human_point>computer_point:
#     print(f"{name} won the match by {human_point} point")
# elif human_point<computer_point:
#     print(f"Computer won the match by {computer_point} point")
# else:
#     print("Match tie !")



f = open("README.txt", "a")
f.write("19 years old\n")
