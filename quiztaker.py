from quizmodel import Exammodel
    

def run():
    id=0
    qbank = {"0":"Who is lord", "1":"Do u love God"}
    opt={"0":{"1":"Jesus","2":"Zion"}, "1":{"1":"yes","2":"maybe"}}
    ans={"0":opt["0"]["1"],"1":opt["1"]["1"]}

    while id < len(qbank):
        
        try:    
            displayQue(qbank,opt,id)
            choice=Exammodel().getSelection(id)          
            id=id+1
            if id==len(qbank):
                print("Choice list are: ",choice)
                displayResult(choice,ans)

        except Exception as ex:
            print("oh ops- smth broke",str(ex))

def getInput():
    que=input("Enter questions:?")
    opt=input("Enter options:?")
    ans=input("Enter anwers")
    return que,opt,ans
    
def displayQue(qbank,opt,qid):
    id=str(qid)
    print(qbank[id],"\n",opt[id])

def displayExamRules():
    print(''' 
     Here is a Quiz Taker app
     Updates would continually be added
    ''')

def displayResult(choice,ans):
    score=0
    k=0
    while k < len(ans):
        i=""
        i=str(k)
        if choice[i] in ans:
            score += 1
        k+=1
    
    print("Total score is " + str(score))




def setQue():
    que,opt,ans=getInput()
    return que , opt, ans

