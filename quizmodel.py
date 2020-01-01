class Exammodel():
    clist=dict()

    def __init__(self):
        
        pass
    
    def getSelection(self, qid):
        if qid=="":
            return -1
        else:
            choice=input("Enter options:?")
            id=str(qid)
            
            self.clist.update({id:choice})
            return self.clist
