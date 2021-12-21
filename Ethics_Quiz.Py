'''
1. Ask the user for their name.
2. User provides name as an input.
3. Ask for confirmation that their name was entered correctly.
4. If entered correctly, return "awesome!".
5. If incorrect, return to asking for the user's name.
6. Randomly pull a question from an array of questions.
7. Ask the user a question.
8. Store the answer.
9. 
10. 

'''
import random

questions = ['Do you believe in the greater good?' , 'Do you believe that an action is moral if it makes you happy but, does not harm another?' , 'Do you believe that the ten commandments are considered laws?' , 'Is Taylor Swift real?' , 'Are you a robot?']
masterlist = []

#print(questions[(random.randint(0,4))]);


'''
while True:
            # Asks and confirms the user's name continueing the loop.
            print("what is your name?")
            Name = input()

            print("Is" , Name, "correct?")
            print("y or n?")
            name_auth = input()

            if name_auth == 'y':
                print("awesome!")
                break
            
            if name_auth == 'n':
                print("Try again!")

            else:
                print("Idiot sandwich!!!")
               
print("Welcome",Name,"It's time for the first question!")
'''

for x in range(len(questions)):
            for x in range(len(questions)):
                    # Randomly shuffles the questions and assigns the shuffled list to a variable.
                    random.shuffle(questions)
                    Q1 = questions
                    #print(Q1) #Print the list of questions.#
                    
                    for x in range(len(Q1)):                        
                        Y1 = list.pop(Q1)
                        break
                    print(Y1) #Print the last question of the list.
                        
                    # Asks the user for their answer to the question.
                    A1 = input('Yes or No: ')
                    
                    # Stores both the question and the answer to a new list.
                    masterlist.append(Y1)
                    masterlist.append(A1)
                                     
                    for x in range(len(Y1)):
                        # Confirms the user's answer and completes the loop.
                        print("Is" , A1 , "correct?")
                        print("y or n?")
                        answerinput = input()

                        if answerinput == 'y':
                            print("awesome!")
                            #print(masterlist)                       
                            break        
                        
                        if answerinput == 'n':
                            print("Try again!")
                            pass

                        elif answerinput != ('y' or 'n'):
                            print("Idiot_sandwich!!!")
                            pass
                    
