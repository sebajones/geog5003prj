# import libraries
#import random
import operator
import matplotlib
import matplotlib.pyplot
import matplotlib.animation
import agentframework
import csv
import tkinter
import requests
import bs4

# scrape y and x data

# get url and parse data
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text    # create content variable
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})    # find y tags
td_xs = soup.find_all(attrs={"class" : "x"})    # find y tags

# create empty list for the environment data
environment = []

# read in environment data and append to the environment list
with open("in.txt", newline='') as f: # open environment data file
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:              # loop through rows
        rowlist = []                # create empty rowlist list
        for value in row:           # loop through values
            rowlist.append(value)   # append to rowlist list
        environment.append(rowlist) # append to environment list

# set model variable values
num_of_agents = 100
num_of_iterations = 10
neighbourhood = 20

# create empty list for agents
agents = []

# set pyplot figure settings and apply set variable names
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# use loop to create agents using scraped data values and append to agents list
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(environment, agents, y, x))

# set animation control 'carry_on' to True
carry_on = True

# define update function
# updates
def update(frame_number):
    fig.clear()
    global carry_on

    # move agents
    for j in range(num_of_iterations):      # loop through num_of_iterations
        for i in range(num_of_agents):      # loop through agents
            agents[i].move()                # call move function
            agents[i].eat()                 # call eat function
            agents[i].share_with_neighbours(neighbourhood)  # call share with neighbours function

    # animation stopping condition
    #while random.random < 0.1:
    #    carry_on = False
    #    print("stopping condition")

    # pre-environment pyplot axis limits
    #matplotlib.pyplot.xlim(0, 99)
    #matplotlib.pyplot.ylim(0, 99)

    # show environment surface
    matplotlib.pyplot.imshow(environment, cmap='terrain') # colour surface
    for i in range(num_of_agents):      # loop through agents xy values
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y,      #plot xy
        color='whitesmoke', edgecolors='slategray')     # set colours

# define generator function, stops supplying when the condition is met
def gen_function(b = [0]):
    a = 0
    global carry_on
    while (a < 10) & (carry_on) : # loop while a is less than 10
        yield a			# returns control and waits for next call
        a = a + 1       # add 1 to a

# define run function
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update,
    frames=gen_function, repeat=True) # set animation parameters
    canvas.draw()   # draw canvas

# create Graphical User Interface
root = tkinter.Tk()         # main window
root.wm_title("Model")      # set title
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)  # backend and connect with figure
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)            # layout
menu_bar = tkinter.Menu(root)   # create menu
root.config(menu=menu_bar)      # configure menu
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu) # create cascade menu
model_menu.add_command(label="Run model", command=run) # label menu and connect command 'run' function


root.mainloop()     # wait for interactions