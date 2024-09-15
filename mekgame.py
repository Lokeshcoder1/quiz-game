questions =["1.In which year python was invented ?","2.How many years in b.tech ?","3.How many sem years in 4 years of b.tech ?","4.Year of birth of 'Lokesh' ?"]
options = ["1.1990\n2.1987\n3.1996\n4.2000","1.3 years \n2.5 years \n3.4 years \n4.2 years ","1. 3 sems \n2. 8 sems \n3. 4 sems \n4.10 sems","1.1990\n2.1987\n3.1996\n4.2006"]
answers = ["1","3","2","4"]
prizes=["25,00,000","50,00,000","75,00,000","100,00,000",]
print("Welcome to  the MEK GAME : ")
print("The prizes of the game is :")
for i,j in zip(range(1,5),prizes):
    print(f"{i}st question ",end=f"{j} rupees \n")
print()
print("Ok, Let's start the game : \n")

for  i,que,opt,ans,prize in zip(range(5),questions,options,answers,prizes):
    print(f"\n{que}\n{opt}\n")
    answer = input(f"Enter the correct option for the {1+i}st question : \n")
    if answer == ans:
        print(f"Congratulations!,correct answer\nYou won {prize} rupees ")
        continue
    elif answer!=ans and i+1==1:
        print("Sorry,Wrong answer\n You are eliminated from the game \n You won nothing ")
        break
    elif answer!=ans :
        print(f"Sorry,wrong answer \n You are eliminated from the game \n but Congratulations! \n You won {prizes[i-1]}")
        break
    else:
        print(f"Sorry,Wrong answer \n you are eliminated from the game \n but Congratulations!\n You won {prize} rupees ")
        break

