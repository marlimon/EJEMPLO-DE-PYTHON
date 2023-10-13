class User:

    name = None
    email = None
    def __init__(self,name,email):
        self.name = name
        self.email = email
    def send_email(self):
        if self.email is not None:
            print("sending email: "+self.email)
        else:
            print("Error")
    def __str__(self):
        return "User: "+self.name+", "+self.email

 

class Student(User):

    score = None
    def __init__(self, name=None, email=None,score=None):
        super().__init__(name, email)
        self.score=score
    def __str__(self):
        return "Student: "+self.name+", "+self.email+", Score: "+str(self.score)
    def __repr__(self):
        name = self.name
        email = self.email
        score = self.score
        return f"Student({name=},{email=},{score=})"
    def is_approved(self):
        return self.score>=8
