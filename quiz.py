#Python Quiz Game

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is thee hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Elephant", "C. Mammath", "D. Ostrich"),
           ("A. Oxygen", "B. Nitrogen", "C. Methane", "D. Carbon-dioxide"),
           ("A. 204", "B. 205", "C. 206", "D. 207"),
           ("A. Mercury", "B. Venus", "C. Mars", "D. Jupiter"))

answers = ("C", "D", "B", "C", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------")
    print(question)
for option in options[question_num]:
    print(option)

guess = input("Enter (A, B, C, D): ").upper()
guesses.append(guess)
if guess == answers[question_num]:
    score += 1
    print("CORRECT!")
else:
    print("INCORRECT")
    print(f"{answers[question_num]} is the correct answer")

question_num += 1

print("---------------")
print("     RESULT    ")
print("---------------")

print("answers:", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
