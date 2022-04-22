# import libraries
import random

# create Agent class
class Agent():
# initialise Agent class take in data variables
    def __init__(self, environment, agents, y, x):
        self.y = y
        self.x = x
        self.environment = environment
        self.store = 0
        self.agents = agents

# define function to move agents
    def move(self):
        if random.random() < 0.5: # if randomly generated number less than 0.5
            self.y = (self.y + 1) % 300     # add 1 from y value
        else:                               # otherwise
            self.y = (self.y - 1) % 300     # subtract 1 from y value

        if random.random() < 0.5: # if randomly generated number less than 0.5
            self.x = (self.x + 1) % 300     # add 1 from x value
        else:                               # otherwise
            self.x = (self.x - 1) % 300     # subtract 1 from x value

# define function to share resources with nearby neighbours
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:               # loop through agents
            dist = self.distance_between(agent) # calculate distance between self and other agent
            if dist <= neighbourhood:           # if distance less than or equal to agent
                sum = self.store + agent.store  # add self store and other agent store
                ave = sum /2                    # take average
                self.store = ave                # assign average value to store value
                agent.store = ave               # assign average value to store value
                #print("sharing " + str(dist) + " " + str(ave))

# define function to eat environment
    def eat(self):
        if self.environment[self.y][self.x] > 10:  # if environment xy greater than 10
            self.environment[self.y][self.x] -= 10 # take 10 from environment xy
            self.store += 10                       # add 10 to store

# define function to calculate distance between self and another agent
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 # calculate distance