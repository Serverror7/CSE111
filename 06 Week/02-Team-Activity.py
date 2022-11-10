def main():
    introprt1 = "\nThis program is an implementation of the Rosenberg \nSelf-Esteem Scale. This program will show you ten \nstatements that you could possibly apply to yourself."
    introprt2 = "Please rate how much you agree with each of the \nstatements by responding with one of these four letters: \n"
    introprt3 = "D means you strongly disagree with the statement. \nd means you disagree with the statement. \na means you agree with the statement. \nA means you strongly agree with the statement."
    print(introprt1)
    print(introprt2)
    print(introprt3)
    
    answers = [input("I feel that I am a person of worth, at least on an equal plane with others. ")] 
    answers.append(input("I feel that I have a number of good qualities. ")) 
    answers.append(input("All in all, I am inclined to feel that I am a failure. ")) 
    answers.append(input("I am able to do things as well as most other people. ")) 
    answers.append(input("I feel I do not have much to be proud of. ")) 
    answers.append(input("I take a positive attitude toward myself. ")) 
    answers.append(input("On the whole, I am satisfied with myself. ")) 
    answers.append(input("I wish I could have more respect for myself. ")) 
    answers.append(input("I certainly feel useless at times. ")) 
    answers.append(input("At times I think I am no good at all. ")) 
    positives = [0,0,1,0,1,0,0,1,1,1]
    values = evalutate(answers, positives)
    scores = score(values)
    print(f"Your score is: {scores}.")

def evalutate(answers, positives):
    values = []
    iteration = 0
    for x in answers:
        positive = positives[iteration]
        values.append(letter_to_value(x, positive))
        iteration = iteration + 1
    return values

def score(values):
    iteration = 0
    score = 0
    for x in values:
        score = score + x
        iteration = iteration + 1
    return score

def letter_to_value(letter, positive):
    """
    The letter value is either A, a, d, or D.
    """
    if positive == 0:
        letterislower = letter.islower()
        if letterislower == True:
            if letter == "a":
                score = 2
            elif letter == "d":
                score = 1
            else:
                score = 0
        else:
            if letter == "A":
                score = 3
            elif letter == "D":
                score = 0
            else:
                score = 0
    if positive == 1:
        letterislower = letter.islower()
        if letterislower == True:
            if letter == "a":
                score = 1
            elif letter == "d":
                score = 2
            else:
                score = 0
        else:
            if letter == "A":
                score = 0
            elif letter == "D":
                score = 3
            else:
                score = 0
    return score



main()