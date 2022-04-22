# import libraries
import random
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
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
# find x and y tags
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

# create empty list for the environment data
environment = []

# read in environment data and append to the environment list
with open("in.txt", newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)

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

# set animation 'carry_on' control to True
carry_on = True

def update(frame_number):
    fig.clear()
    global carry_on

    # move agents
    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)

    #while random.random < 0.1:
    #    carry_on = False
    #    print("stopping condition")

    #matplotlib.pyplot.xlim(0, 99)
    #matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.imshow(environment, cmap='terrain')
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y,
        color='whitesmoke', edgecolors='slategray')

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

def run():
    animation = matplotlib.animation.FuncAnimation(fig, update,
    frames=gen_function, repeat=True)
    canvas.draw()

root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)


root.mainloop()