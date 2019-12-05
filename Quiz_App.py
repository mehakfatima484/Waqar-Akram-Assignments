#Student: Waqar Akram
#email: raobscs@gmail.com
#This is a small quiz app for pyhton students using dictionaries in pyhton
#You can add 100 of questions in this dictionary
quiz=[
    {
        "sr_no":1,
        "question":"Which of the following are true of Python dictionaries:",
        "options":["All the keys in a dictionary must be of the same type.","Dictionaries can be nested to any depth.","A dictionary can contain any object type except another dictionary.","Items are accessed by their position in a dictionary."],
        "answer":"2"
    },
     {
        "sr_no":2,
        "question":"d = {'foo': 100, 'bar': 200, 'baz': 300}\nWhat is the result of this statement:\nd['bar':'baz']",
        "options":["It raises an exception","[200, 300].","200 300.","(200, 300)"],
        "answer":"1"
    },
    {
        "sr_no":3,
        "question":"In a Python program, a control structure:",
        "options":["Directs the order of execution of the statements in the program","Dictates what happens before the program starts and after it terminates","Defines program-specific data structures","Manages the input and output of control characters"],
        "answer":"1"
    },
     {
        "sr_no":4,
        "question":"What signifies the end of a statement block or suite in Python?",
        "options":["A comment","A line that is indented less than the previous line","}","end"],
        "answer":"2"
    },
     {
        "sr_no":5,
        "question":"What does a threading.Lock do?",
        "options":["Allow only one thread at a time to access a resource","Pass messages between threads","SHIFT TO ALL CAPS","Wait until a thread is finished"],
        "answer":"1"
    },

]
score=0
for question in quiz:
    i=1
    print(str(question["sr_no"])+" "+question["question"])
    for item in question["options"]:

        print(i,item)
        i+=1

    its_answer=input("Write Correct Option No Here like 1,2,3: ")

    #i was try to make correct this app for multiple right options....:( but i was failed
    #if can do it correct please inform me
    # a=len(question["answer"])
    # if a>1:
    #     for ans in range(a):
    #         its_answer==question["answer"][ans] and question["answer"][ans] and question["answer"][ans]
    #         score+=1
    # else:

    #To check both are same or not you can print it to show the right option after answer
    # print(its_answer)
    # print(question["answer"])
    if (its_answer==question["answer"]):
        score+=1
        # to check if statement isworking or not
        # print(score)
pcntg=(score/len(quiz))*100
print("Your Result Score is ",score)
print("Your Percentage is "+str(pcntg)+"%")
