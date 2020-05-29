## Hello Eighth Grader, This project is to test your knowledge and to see your ability to make smart and safe decisions if you were ever to be stuck on a stranded island!
#You will be asked several two option questions, one answer is correct and if you choose it you will move on to the next question, if you choose the incorrect answer you will get to move on, but you wont have a perfect score

# One day you decided to hop on a plane and go on a short vacation. While you were in the air the plane started having a bunch of turbulance. You thought it was nothing so you decided to take a nap. The moment you wake up everyonen around you is screaming and you can tell the plane is going down. You start freaking out. You are so scared that you completely black out. 
# The next thing you know, your beached on an island. Youre alone, scared, confused, and the only thing you have is the pocket knife you keep in your back pocket at all times. 
# What do you do now?

name=input("State your name: ")

def rightanswer():
    print("You Got this right "+ name)

def wronganswer():
    print("You got this wrong "+ name)

questionone = input("What is the #1 thing that you should never lose?- a.)Your clothes. b.) Your pocket knife")
questionones = ("b")
if questionone == questionones:
    rightanswer()
else:
    wronganswer()
# I set question 1 as the question and i put question1s as the answer to the question. 
# I then have my if statement to print the right answer and else statement to print the incorrect answer
#all of the questions will be set up like this, two options and one answer.
questiontwo = input("What is the first thing you should look for?- a.)water. b.) food")
questiontwos = ("a")
if questiontwo == questiontwos:
    rightanswer()
else:
    wronganswer()
#a lot of questions will just be testing knowledge on facts 
questionthree = input("Where should you make your camp?- a.)near many trees. b.) near the shore")
questionthrees = ("b")
if questionthree == questionthrees:
    rightanswer()
else:
    wronganswer()

questionfour = input("You see random berries sitting on a bush, what do you do?- a.) Eat them! b.) Leave them be")
questionfours = ("b")
if questionfour == questionfours:
    rightanswer()
else:
    wronganswer()

questionfive = input("What is the most dangerous sea life animal you could encounter?- a.) sharks and eels. b.) Sea Wasp Jellyfish ")
questionfives = ("b")
if questionfive == questionfives:
    rightanswer()
else:
    wronganswer()

questionsix = input("What is the most deadly land animal you could encounter?- a.)Snakes. b.) Spiders")
questionsixs = ("a")
if questionsix == questionsixs:
    rightanswer()
else:
    wronganswer()

questionseven = input(" What is one insect that you need to always be looking out for?- a.)Mosquitos. b.) Stink bugs")
questionsevens = ("a")
if questionseven == questionsevens:
    rightanswer()
else:
    wronganswer()

questioneight = input("How long can you survive without food?- a.)5 days. b.) three weeks")
questioneights = ("b")
if questioneight == questioneights:
    rightanswer()
else:
    wronganswer()

questionnine = input("What plants can you use for a soap replacement?- a.)Sunflowers. b.) Yucca Roots")
questionnines = ("b")
if questionnine == questionnines:
    rightanswer()
else:
    wronganswer()

questionten = input("How long can you survive without water?- a.) 6 days. b.) 3 days")
questiontens = ("b")
if questionten == questiontens:
    rightanswer()
else:
    wronganswer()

print("Good job you finished!! You survived ten questions about being stranded on an island!!")