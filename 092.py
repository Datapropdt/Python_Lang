#program to creatte an iterator to print squares of numbers 

class Square:
    def __init__(self):
        self.val = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.val += 1
        return self.val ** 3
    
Sq = Square()
count = 0
for num in Sq:
    print(num, end=" ")
    if count == 10:
        break
    count += 1
    
