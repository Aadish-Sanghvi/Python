quesAns = [["Who is the current PM of India", "Arvind Kejriwal", "Narendra Modi", "Rahul Gandhi", "Laalu yadav", 2],
           ["Who is Indian captain", "Rohit", "Kohli", "MSD", "gill",1],
           ["National bird of india ?","peacock","crow","eagle","falcon",1],
           ["Who is the current PM of India", "Arvind Kejriwal", "Narendra Modi", "Rahul Gandhi", "Laalu yadav", 2],
           ["Who is Indian captain", "Rohit", "Kohli", "MSD", "gill",1],
           ["National bird of india ?","peacock","crow","eagle","falcon",1],
           ["Who is the current PM of India", "Arvind Kejriwal", "Narendra Modi", "Rahul Gandhi", "Laalu yadav", 2],
           ["Who is Indian captain", "Rohit", "Kohli", "MSD", "gill",1],
           ["National bird of india ?","peacock","crow","eagle","falcon",1],
           ["Who is the current PM of India", "Arvind Kejriwal", "Narendra Modi", "Rahul Gandhi", "Laalu yadav", 2],
           ["Who is Indian captain", "Rohit", "Kohli", "MSD", "gill",1],
           ["National bird of india ?","peacock","crow","eagle","falcon",1],
           ["Who is the current PM of India", "Arvind Kejriwal", "Narendra Modi", "Rahul Gandhi", "Laalu yadav", 2],
           ["Who is Indian captain", "Rohit", "Kohli", "MSD", "gill",1],
           ["National bird of india ?","peacock","crow","eagle","falcon",1],
           ["Who is the current PM of India", "Arvind Kejriwal", "Narendra Modi", "Rahul Gandhi", "Laalu yadav", 2],
           ["Who is Indian captain", "Rohit", "Kohli", "MSD", "gill",1],
           ["National bird of india ?","peacock","crow","eagle","falcon",1],
           ]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]

winAmount = 0

for i in range(0, len(quesAns)):
    question = quesAns[i]
    print(question[0])
    print(f"1.{question[1]}     2.{question[2]}")
    print(f"3.{question[3]}     4.{question[4]}")
    reply = int(input("Enter your answer: "))
    if(reply == question[-1]):
        print(f"correct answer,you have won {levels[i]}")
    else:
        print("Wrong answer! try again...")
        break