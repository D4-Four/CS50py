#13 march '24
#Talking Hat is a code that inputs "name" from user and generates a randomized output based on Harry Potter's Housing
def main(): 
    name = input("Hey kid, What is your Name? ").title().strip()
    #random 1-4
    #if 1: etc
    if House(name) == "Gryffindor":
        print("You belong in Gryffindor, where courage and bravery shine like the sun, and valor is celebrated above all else.")
    elif House(name) == "Slytherin":
        print("You belong in Slytherin, where ambition and cunning are your greatest allies, and success is your destiny.")
    elif House(name) == "Ravenclaw":
        print("You belong in Ravenclaw, where wisdom and wit are your guiding stars, and knowledge is the key to unlocking your true potential.")
    else:
        print("You belong in Hufflepuff, where loyalty and hard work pave the path to greatness, and fairness and kindness are your greatest strengths.")

def House(name):
    HogwartsStudents = {
    "Harry": "Gryffindor",
    "Hermione": "Gryffindor",
    "Ron": "Gryffindor",
    "Neville": "Gryffindor",
    "Ginny": "Gryffindor",
    "Fred": "Gryffindor",
    "George": "Gryffindor",
    "Percy": "Gryffindor",
    "Bill": "Gryffindor",
    "Charlie": "Gryffindor",
    "Seamus": "Gryffindor",
    "Oliver": "Gryffindor",
    "Angelina": "Gryffindor",
    "Katie": "Gryffindor",
    "Parvati": "Gryffindor",
    "Draco": "Slytherin",
    "Vincent": "Slytherin",
    "Gregory": "Slytherin",
    "Millicent": "Slytherin",
    "Pansy": "Slytherin",
    "Blaise": "Slytherin",
    "Theodore": "Slytherin",
    "Marcus": "Slytherin",
    "Morag": "Slytherin",
    "Daphne": "Slytherin",
    "Tracey": "Slytherin",
    "Luna": "Ravenclaw",
    "Cho": "Ravenclaw",
    "Padma": "Ravenclaw",
    "Terry": "Ravenclaw",
    "Susan": "Ravenclaw",
    "Megan": "Ravenclaw",
    "Eloise": "Ravenclaw",
    "Marietta": "Ravenclaw",
    "Michael": "Ravenclaw",
    "Lisa": "Ravenclaw",
    "Penelope": "Ravenclaw",
    "Stephen": "Ravenclaw",
    "Kevin": "Ravenclaw",
    "Cedric": "Hufflepuff",
    "Ernie": "Hufflepuff",
    "Justin": "Hufflepuff",
    "Hannah": "Hufflepuff",
    "Susan": "Hufflepuff",
    "Zacharias": "Hufflepuff",
    "Anthony": "Hufflepuff",
    "Stewart": "Hufflepuff",
    }
    #if name == dictionary then return housing name
    if name in HogwartsStudents:
        return HogwartsStudents[name]
    else:
        total_sum = 0
        for char in name.lower():
            convertedchar = ord(char)-96
            total_sum += convertedchar
        # Check conditions to determine house
        if total_sum % 2 == 0:
            return "Gryffindor"
        elif total_sum % 3 == 0:
            return "Slytherin"
        elif total_sum % 5 == 0:
            return "Ravenclaw"
        else:
            return "Hufflepuff"

main()