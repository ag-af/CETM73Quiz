# CETM73 Geography Quiz

## **Overview**

This Python program is a console-based quiz game that allows multiple users to take a geography quiz. Players can answer a set number of questions, presented in a random order. Their scores are displayed at the end of the game along with the highest scorer and average score. 

The quiz followed specific instructions of an assignment from the Software Engineering module part of the Computer Science with Data Science course. 

### **How to Use**

**Requirements**

Python 3 installed

**Setup**
1. Clone the CETM73Quiz repository `https://github.com/ag-af/CETM73Quiz.git`
2. Save in a directory of your choice
2. Open a terminal and navigate to the directory containing quiz_game.py
3. Alternatively, you can open the project in PyCharm and run it from there

**Instructions**
1. To start the game, run the script by entering: `python quiz_game.py`
2. When prompted, specify how many questions the players would like to answer between 1 and 10
3. Each player will be prompted to enter their name, it cannot be left blank
4. For each question, type your answer and press `Enter`
5. The program will provide feedback if your answer is correct or incorrect. Answer cannot be blank
6. After completing the quiz, you will be asked if another player would like to take the quiz
7. If so, the next player can enter their name and answer the same number of questions as chosen initially
8. Once all players have finished, the program with display player's score along with their percentage score, the highest scorer and the average score and average percentage of all players

## Example

        python quiz_game.py

        How many questions would you like to answer? (Max:10):

        2
        
        Enter your name: Mary
        
        Q1: What is the oldest recorded town in the UK? London
        
        Incorrect! The correct answer was: Colchester
        
        Q2: Which country has the largest population? China

        Correct!

        Mary, you scored 1 out of 2 (50.00%)
        
        Does anyone else want to play the quiz? (yes/no): yes

        Enter your name: John
        
        Q1: What is the oldest recorded town in the UK? Colchester
        
        Correct
        
        Q2: Which country has the largest population? China

        Correct

        John, you scored 2 out of 2 (100.00%)
        
        Does anyone else want to play the quiz? (yes/no): no

            Quiz Results
        Mary: 1 point (50.00%)
        John: 2 points (100.00%)

        Highest scorer: John with 2 points (100.00%)
        Average score of all users: 1.50 (75.00%)

### Features
- Player's name
- Multiplayers
- Score of users
- Highest and average score
- Questions in random order
- User can specify the number of questions to answer
- Feedback for correct and incorrect answer
- Error handling(e.g. empty answer)


**Enjoy the quiz!**


