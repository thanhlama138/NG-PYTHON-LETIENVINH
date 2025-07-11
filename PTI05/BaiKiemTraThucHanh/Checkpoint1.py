class Homework:
    def __init__(self, name, priority, compeleted=False):
        self.name = name
        self.priority = priority
        self.compeleted = compeleted
    def show(self):
        print("name:",self.name)
        print("priority:",self.priority)
        print("compeleted:",self.compeleted)
class ListHomework:
    def __init__(self):
        self.listhomework = []

        

#hs1 = Homework ("lap trinh App Producer", "High", "unfinished")
#hs2 = Homework ("Lam van","normal","finished")
#hs3 = Homework ("lap trinh gameker","Low","unfinished")
#hs1.show()
#hs2.show()
#hs3.show()