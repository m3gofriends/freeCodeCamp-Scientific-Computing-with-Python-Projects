import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self, red = None, green = None, blue = None, yellow = None, orange = None, pink = None, black = None, striped = None, test = None):
        self.contents = []
        
        self.red = red
        if(red != None):
            for i in range(red):
                self.contents.append("red")
                
        self.green = green
        if(green != None):
            for i in range(green):
                self.contents.append("green")
                
        self.blue = blue
        if(blue != None):
            for i in range(blue):
                self.contents.append("blue")
                
        self.yellow = yellow
        if(yellow != None):
            for i in range(yellow):
                self.contents.append("yellow")
                
        self.orange = orange
        if(orange != None):
            for i in range(orange):
                self.contents.append("orange")
                
        self.pink = pink
        if(pink != None):
            for i in range(pink):
                self.contents.append("pink")
                
        self.black = black
        if(black != None):
            for i in range(black):
                self.contents.append("black")
                
        self.striped = striped
        if(striped != None):
            for i in range(striped):
                self.contents.append("striped")

        self.test = test
        if(test != None):
            for i in range(test):
                self.contents.append("test")

    def draw(self, draw_number):
        if(draw_number > len(self.contents)):
            return self.contents
        draw_list = []
        for i in range(draw_number):
            draw_ball = random.choice(self.contents)
            draw_list.append(draw_ball)
            self.contents.remove(draw_ball)
        return draw_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_counter = 0
    expected_balls_list = []

    for key, value in expected_balls.items():
        temp_list = []
        temp_list.append(key)
        expected_balls_list.extend(temp_list * value)

    for times in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draw_list = hat_copy.draw(num_balls_drawn)
        expected_bool = True
        for expected_color in expected_balls_list:
            try:
                draw_list.remove(expected_color)
            except:
                expected_bool = False
                break
        if(expected_bool):
            expected_counter += 1
            
    return expected_counter / num_experiments