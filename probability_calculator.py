import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
        self.copy = self.contents[:]

    def draw(self, number):                
        self.contents = self.copy[:]
        if number < len(self.contents)-1:
            self.drawn_balls = []
            for i in range(number):
                index = self.contents.index(random.choice(self.contents))
                self.drawn_balls.append(self.contents[index])
                self.contents.pop(index)            
        else:
            return self.contents
        return self.drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    prob = 0
    for i in range(num_experiments):
        drawn_dictionary = {}
        drew = hat.draw(num_balls_drawn)
        for item in drew:
            if item not in drawn_dictionary:
                drawn_dictionary[item] = 1
            else:
                drawn_dictionary[item] += 1
        same_var = 0
        for key in expected_balls.keys():
            if key in drawn_dictionary.keys():
                if expected_balls[key] <= drawn_dictionary[key]:
                    same_var += 1                            

        if same_var == len(expected_balls):
            prob += 1
    
    return prob / num_experiments

hat = Hat(blue=3,red=2,green=6)
hat.draw(3)
print(len(hat.contents))
# print(experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000))

# lis = [1,76, 32,31,2,3,4,6]

# k = [1,2,3]

# for i,j in zip(lis,k):
#     n = 0
#     if i == j:
#         print("yeah")
#     else:
#         print("no")

# k = "green"
# v = {"blue":2,"green":1}

# if k in v.keys():
#     print("yeah")