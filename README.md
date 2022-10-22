README

# Robot-guide
robot guide through a 2d map with convx polygon obstacles using searching algorithms. Each vertex of the polygons represents a point where the robot can move.

# Libraries installation
This program use  https://github.com/scikit-geometry/scikit-geometry available using this command:

`conda install scikit-geometry -c conda-forge`

# Test demo
The tests can be used by running main.py. After running it, a prompt message is shown asking for the map to be used for testing(I implemented only two maps):

0. to access the first map, 
1. (or any other value) to choose the second map. 

After choosing it, the program will plot it(e. g.):

![Figure_1.png](Figure_1.png)

Here we can see the start state (blue dot), the goal state (yeollow dot) and all obstacles to navigate through (convex polygons). The program will then ask for the searching algorithm to use in the graph form*:
1. A* algorithm
2. Uniform cost search algorithm
3. (or any other value) Breadth first search algorithm

 Once algorithm is chosen, it will be executed and a plot of the map will be shown with the path found by the algorithm. The list of segments making up the path from start to goal and its length will then be written into the terminal. 
The plot using A* is shown below:
![Figure_2.png](Figure_2.png)

# Code from other repositories
The code for the utils.py file, like the code for A* and Best First Search was taken from the repository https://github.com/aimacode.

_* indicates the version of the algorithm used. This uses a closed list to store already explored nodes so that they are not explored again._
