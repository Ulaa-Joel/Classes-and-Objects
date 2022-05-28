class Student:
    name = 'Tom'
    age = int(24)
    tracks = ['FE', 'BE']
    score = float(12.5)
    # [assignment] Skeleton class. Add your code here
    def __init__(self):
        print("name=",self.name, "age=",self.age, "tracks=",self.tracks, "score=",self.score)

Student()
setattr(Student, 'name', 'Tim')
print getattr(Student, 'name')

setattr(Student, 'age', 29)
print getattr(Student, 'age')

setattr(Student, 'tracks', 'UI/UX')
print getattr(Student, 'tracks')

setattr(Student, 'score', float(15.3))
print getattr(Student, 'score')

