print("Welcome to the Downton Abbey Trivia Game!")
playing = input("Would you like to play? ")
if playing.lower() != "yes":
    quit()

print("Okay lets play!")
print("Each correct answer is 2 points while each wrong answer is -3 points!")
score = 0
print("Please answer with either 'a', 'b', 'c', or 'd'")
print("===============================================")
print("===============================================")
print("===============================================")
print("===============================================")
print("===============================================")
print("===============================================")
print("1. Who is the head of the Crawley family? ")
print("a) Matthew Crawley")
print("b) Lady Mary Crawley")
print("c) Robert Crawley")
print("d) Lady Edith Crawley")
answer1 = input("")

if answer1.lower() == "c":
    print("Correct!")
    score += 2
else:
    print("Incorrect!")
    score -= 3

print("2. What is the name of the Crawley family's estate? ")
print("a) Balmoral Castle")
print("b) Buckingham Palace")
print("c) Downton Abbey")
print("d) Highclere Castle")
answer2 = input("")

if answer2.lower() == "c":
    print("Correct!")
    score += 2
else:
    print("Incorrect!")
    score -= 3

print("3. Who is the heir to the Crawley familly's fortune and estate? ")
print("a) Matthew Crawley")
print("b) Lady Mary Crawley")
print("c) Lady Sybl Crawley")
print("d) Lady Edith Crawley")
answer3 = input("")

if answer3.lower() == "b":
    print("Correct!")
    score += 2
else:
    print("Incorrect!")
    score -= 3

print("4. What event triggers the start of the series? ")
print("a) World War I")
print("b) The sinking of the Titanic")
print("c) The Great Depression")
print("d) The assassination of Archduke Franz Ferdinand")
answer4 = input("")

if answer4.lower() == "b":
    print("Correct!")
    score += 2
    # print("The sinking of the Titanic, which results in the death of the Cr")
else:
    print("Incorrect!")
    score -= 3

print("5. Who is the new heir to the Crawley family's fortune and estate? ")
print("a) Matthew Crawley")
print("b) Tom Branson")
print("c) Sir Richard Carlisle")
print("d) Mr. Bates")
answer5 = input("")

if answer5.lower() == "a":
    print("Correct!")
    score += 2
else:
    print("Incorrect!")
    score -= 3

print("3. Who is Lady Sybil Crawley's love interest in season 1? ")
print("a) Mr. Carson")
print("b) Tom Branson")
print("c) William Mason")
print("d) John Bates")
answer6 = input("")

if answer6.lower() == "b":
    print("Correct!")
    score += 2
else:
    print("Incorrect!")
    score -= 3

print("7. Who is the head housemaid at Downton Abbey? ")
print("a) Mrs. Hughes")
print("b) Mrs. Patmore")
print("c) Anna Smith")
print("d) Ethel Parks")
answer7 = input("")

if answer7.lower() == "a":
    print("Correct!")
    score += 2
else:
    print("Incorrect!")
    score -= 3

print("8. Who is Lady Mary's suitor in Season 1? ")
print("a) Matthew Crawley")
print("b) Tom Branson")
print("c) Sir Richard Carlisle")
print("d) Mr. Bates")
answer8 = input("")

if answer8.lower() == "c":
    print("Correct!")
    score += 2
else:
    print("Incorrect!")
    score -= 3

print("9. What is the name of the valet who is fired in Season 1 for stealing? ")
print("a) John Bates")
print("b) Thomas Barrow")
print("c) Alfred Nugent")
print("d) William Mason")
answer9 = input("")

if answer9.lower() == "a":
    print("Correct!")
    score += 2
else:
    print("Incorrect!")
    score -= 3

print("10. Who is the cook at Downton Abbey? ")
print("a) Mrs. Hughes")
print("b) Mrs. Patmore")
print("c) Anna Smith")
print("d) Ethel Parks")
answer10 = input("")

if answer10.lower() == "b":
    print("Correct!")
    score += 2
else:
    print("Incorrect!")
    score -= 3

if score >= 14:
    print("Well done! Your score is: " +str(score)+ " points!")
else:
    print("Your score is: " +str(score)+ " points! Maybe brush up on your Downton Abbey trivia?")