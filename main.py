import search
import classes
import skgeom as sg
from skgeom.draw import draw
import matplotlib.pyplot as plt

x = input("inserisci numero mappa:")
plot = list()
if x == "1":
    plot.append(sg.Polygon([sg.Point2(2, 1), sg.Point2(7, 1), sg.Point2(2, 7)]))
    plot.append(sg.Polygon([sg.Point2(5, 7), sg.Point2(10, 7), sg.Point2(10, 11), sg.Point2(5, 11)]))
    plot.append(sg.Polygon([sg.Point2(9, 1), sg.Point2(13, 1), sg.Point2(14, 4), sg.Point2(11, 6), sg.Point2(8, 4)]))
    plot.append(sg.Polygon([sg.Point2(12, 8), sg.Point2(15, 8), sg.Point2(13, 15), sg.Point2(11, 16), sg.Point2(10, 14)]))
    plot.append(sg.Polygon([sg.Point2(15, 2), sg.Point2(22, 2), sg.Point2(20, 5), sg.Point2(15, 5)]))
    plot.append(sg.Polygon([sg.Point2(19, 6), sg.Point2(22, 8), sg.Point2(22, 12), sg.Point2(20, 14), sg.Point2(17, 12), sg.Point2(17, 8)]))
    plot.append(sg.Polygon([sg.Point2(28, 1), sg.Point2(31, 2), sg.Point2(31, 6), sg.Point2(29, 8), sg.Point2(25, 6), sg.Point2(25, 2)]))
    end = sg.Point2(30, 14)
else:
    plot.append(sg.Polygon([sg.Point2(0, 14), sg.Point2(1, 9), sg.Point2(7, 8), sg.Point2(9, 15), sg.Point2(6, 19)]))
    plot.append(sg.Polygon([sg.Point2(2, 6), sg.Point2(2, 1), sg.Point2(17, 1), sg.Point2(17, 6)]))
    plot.append(sg.Polygon([sg.Point2(10, 8), sg.Point2(14, 8), sg.Point2(12, 15)]))
    plot.append(sg.Polygon([sg.Point2(19, 3), sg.Point2(23, 6), sg.Point2(18, 10)]))
    plot.append(sg.Polygon([sg.Point2(14, 13), sg.Point2(20, 17), sg.Point2(18, 20), sg.Point2(14, 19)]))
    plot.append(sg.Polygon([sg.Point2(22, 9), sg.Point2(28, 9), sg.Point2(28, 19), sg.Point2(22, 19)]))
    plot.append(sg.Polygon([sg.Point2(28, 1), sg.Point2(31, 2), sg.Point2(31, 6), sg.Point2(29, 8), sg.Point2(25, 6), sg.Point2(25, 2)]))
    plot.append(sg.Polygon([sg.Point2(32, 8), sg.Point2(34, 16), sg.Point2(31, 19), sg.Point2(29, 17)]))
    end = sg.Point2(34, 19)


start = sg.Point2(1, 3)
draw(start)
draw(end)
for x in plot:
        draw(x)
plt.show()
robot_route = classes.RobotRoute(start, end, plot)
node = search.best_first_graph_search(robot_route, lambda n: n.path_cost)

print(node.solution())
print(node.path_cost)
for nod in node.solution():
    draw(nod)
draw(start)
draw(end)
for x in plot:
    draw(x)
plt.show()