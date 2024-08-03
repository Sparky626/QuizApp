import requests
import random
import html
def main():
    active = True
    score = 0
    category = ""
    type = ""
    api_token = requests.get("https://opentdb.com/api_token.php?command=request")
    api_categories = requests.get("https://opentdb.com/api_category.php")
    api_categories = api_categories.json()['trivia_categories']
    print("Welcome to Inquizzitive!")
    print(" ")
    print("Choose your game type!")
    print("Infinity - answer an infinite stream of trivia questions!")
    print("Survival - see how many correct questions you can get without getting any wrong!")
    print(" ")
    type = input("")
    print(" ")
    print("Current Categories:")
    for cats in api_categories:
        print(cats['name'] + " - ID: " + str(cats['id']))
    print(" ")
    category = input("Enter a category id or enter none: ")
    if (type == "Infinity" or type == "infinity" or type == "INFINITY"):
        print("Enter END as answer to end the game.")
        while (active == True):
            if category == 'none' or category == "NONE" or category == "None":
                api_pull = requests.get("https://opentdb.com/api.php?amount=5&token=" + api_token.json()['token'])
            else:
                api_pull = requests.get("https://opentdb.com/api.php?amount=5&token=" + api_token.json()['token'] + "&category=" + category)
            #print(api_token.json())
            #print(api_pull.json())
            results = api_pull.json()['results']
            for qs in results:
                question = qs['question']
                correct_answer = qs['correct_answer']
                incorrect_answers = qs['incorrect_answers']
                answer_list = []
                answer_list.append(correct_answer)
                for answers in incorrect_answers:
                    answer_list.append(answers)
                print("Current Score: " + str(score))
                print(html.unescape(question))
                random.shuffle(answer_list)
                for answers in answer_list:
                    print(html.unescape(answers))
                print(" ")
                user_answer = html.escape(input("Enter your answer: "))
                if user_answer == correct_answer:
                    print("Correct!")
                    score += 1
                    print(" ")
                else:
                    print("Incorrect!")
                    print(" ")
        print("Your high score is " + str(score) + "!")
    else:
        while (active == True):
            if category == 'none' or category == "NONE" or category == "None":
                api_pull = requests.get("https://opentdb.com/api.php?amount=5&token=" + api_token.json()['token'])
            else:
                api_pull = requests.get("https://opentdb.com/api.php?amount=5&token=" + api_token.json()['token'] + "&category=" + category)
            #print(api_token.json())
            #print(api_pull.json())
            results = api_pull.json()['results']
            for qs in results:
                question = qs['question']
                correct_answer = qs['correct_answer']
                incorrect_answers = qs['incorrect_answers']
                answer_list = []
                answer_list.append(correct_answer)
                for answers in incorrect_answers:
                    answer_list.append(answers)
                print("Current Score: " + str(score))
                print(html.unescape(question))
                random.shuffle(answer_list)
                for answers in answer_list:
                    print(html.unescape(answers))
                print(" ")
                user_answer = html.escape(input("Enter your answer: "))
                if user_answer == correct_answer:
                    print("Correct!")
                    score += 1
                    print(" ")
                else:
                    print("Incorrect!")
                    print(" ")
                    active = False
                    break
        print("Your high score is " + str(score) + "!")


if __name__ == '__main__':
    main()