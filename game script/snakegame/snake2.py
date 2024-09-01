from turtle import Turtle

class Snake:
    starting_position = [(0,0),(-20,0),(-40,0)]
    UP =90
    DOWN =270
    RIGHT =0
    LEFT =180

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
        

    def create_snake(self):
        for position in self.starting_position:
            self.add_segment(position)

    def add_segment(self,position):
         self.new_segment=Turtle("square")
         self.new_segment.color("white")
         self.new_segment.penup()
         self.new_segment.goto(position)
         self.segments.append(self.new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(20)

    def go_up(self):
        if self.head.heading() != self.DOWN:
            self.head.setheading(self.UP)
    def go_down(self):
        if self.head.heading() != self.UP:
            self.head.setheading(self.DOWN)
    def go_right(self):
        if self.head.heading() != self.LEFT:
            self.head.setheading(self.RIGHT)
    def go_left(self):
        if self.head.heading() != self.RIGHT:
            self.head.setheading(self.LEFT)
    
    
  
           


