import copy 

original_list = [5 , 1 , [6,9] ]
shallowCopy_list = copy.copy(original_list)
deepCopy_list = copy.deepcopy(original_list)

original_list[2][0] = 4

print(original_list)   # [5 , 1 , [4,9] ]
print(shallowCopy_list)     # [5 , 1 , [4,9] ]
print(deepCopy_list)   # [5 , 1 , [6,9] ]



class Student:
    def __init__(self, firstName , lastName , major):
        self.firstName = firstName
        self.lastName = lastName
        self.major = major

    def fullName(self):
        return f'{self.firstName} {self.lastName} is {self.major}'
    
student1 = Student('Pratush','Mishra','Mathematics')
student2 = Student('Ganesh','Mishra','Physics')
print (student1.fullName())
print (student2.fullName())