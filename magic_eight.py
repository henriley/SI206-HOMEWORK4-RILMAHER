import random
from random import randrange
response_list = ["It is certain","It is decidedly so", "Without a doubt", "Yes definitely","You may rely on it","As I see it, yes","Most likely","Outlook good","Yes","Signs point to yes","Reply hazy try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]
pop = 'riley'

while pop!= "quit":
    pop=input("What is your question? ")
    if "?" not in pop:
        print("Sorry, I can only answer questions.")
    else:
        erin = response_list[randrange(len(response_list))]
        print(erin)



# Ben's comments that Asha said to make for credit
