questions = [ [" which phone is best:" , "redmi" , "apple" , "iqoo" , "samsung" , 4],
             
             [ " who is real OG" , "spider man" , "bat man" , "iron man"  , "thor" , 4],

             [ " who is the best PM" , " nehru" , "modi" , "indra" , "abdul kalam" , 4]
]

levels = [10000 , 100000 , 700000]
money = 0

for i in range( 0 , len(questions)):
    question = questions[i]
    print(f" question for rs: {levels[i]}" )
    print(f" a. {question [1]}           b. {question [2]}")
    print(f" c. {question [3]}           d. {question [4]}")
    reply = int(input("enter your answer (1-4)"))

    if reply == question[-1]:
        print(f"correct answer , you have won Rs: {levels[i]}")
        if (i == 0):
            money = 10000
        elif(i == 1):
            money = 100000
        elif(i == 2):
            money = 700000

    else:
        print("wrong answeer")
        break

print(f"your total winning price money is rs: {money}")