import random
import math

class Agent:
    '''The following class is an agent run in a Breightenbeg Vehichle'''
    def __init__(self):
        '''Initiization Function for the Agent class'''
        self.x = 0.0  # agent's x position
        self.y = 0.0  # agent's y position
        self.o = 0.0  # agent's orientation
        self.v = 1.0  # agent's velocity
        self.sensor = 0.0  ## current sensor stimuli
        self.memory = 0.0  ## past sensor stimuli

    def think(self):
        ''' Uses Klinokinesis that keeps the velocity constant but
        moves the orientation.'''
        self.v = 10
        if self.sensor < self.memory:
            self.o = random.random() * 2 * math.pi
        self.o + 1.5 * (1 / (1 + self.distance(pizza)))

    def move(self):
        '''moves the agents'''
        self.x += self.v * math.cos(self.o)
        self.y += self.v * math.sin(self.o)

    def sense(self, pizza):
        '''is the sensor and memory of the sensor'''
        self.memory = self.sensor
        self.sensor = 1 / (self.distance(pizza))

    def distance(self, pizza):
        ''' the following method is the distance that the agent travels'''
        return math.sqrt((self.x - pizza.x) ** 2 + (self.y - pizza.y) ** 2)

class Food:
    '''is the food that the agents are going to'''
    def __init__(self, dist):
        angle = random.random() * 2 * math.pi
        self.x = dist * math.cos(angle)
        self.y = dist * math.sin(angle)

pizza = Food(100)