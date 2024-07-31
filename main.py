import requests
import random
import html
def main():
    active = True
    score = 0
    api_token = requests.get("https://opentdb.com/api_token.php?command=request")
    while (active == True):
        api_pull = requests.get("https://opentdb.com/api.php?amount=1&token=" + api_token.json()['token'])
        #print(api_token.json())
        #print(api_pull.json())
        results = api_pull.json()['results']
        question = results[0]['question']
        correct_answer = results[0]['correct_answer']
        incorrect_answers = results[0]['incorrect_answers']
        answer_list = []
        answer_list.append(correct_answer)
        for answers in incorrect_answers:
            answer_list.append(answers)
        print("Current Score: " + str(score))
        print(html.unescape(question))
        random.shuffle(answer_list)
        for answers in answer_list:
            print(answers)
        print(" ")
        user_answer = input("Enter your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
            print(" ")
        else:
            print("Incorrect!")
            print(" ")



if __name__ == '__main__':
    main()