import skgeom as sg
from skgeom.draw import draw
import matplotlib.pyplot as plt
import pickle
import math

x = input("inserisci numero mappa:")
plot = list()
if x == "2":
    plot.append(sg.Polygon([sg.Point2(2, 1), sg.Point2(7, 1), sg.Point2(2, 7)]))
    plot.append(sg.Polygon([sg.Point2(5, 7), sg.Point2(10, 7), sg.Point2(10, 11), sg.Point2(5, 11)]))
    plot.append(sg.Polygon([sg.Point2(9, 1), sg.Point2(13, 1), sg.Point2(14, 4), sg.Point2(11, 6), sg.Point2(8, 4)]))
    plot.append(sg.Polygon([sg.Point2(12, 8), sg.Point2(15, 8), sg.Point2(13, 15), sg.Point2(11, 16), sg.Point2(10, 14)]))
    plot.append(sg.Polygon([sg.Point2(19, 6), sg.Point2(22, 8), sg.Point2(22, 12), sg.Point2(20, 14), sg.Point2(17, 12), sg.Point2(17, 8)]))
    plot.append(sg.Polygon([sg.Point2(28, 1), sg.Point2(31, 2), sg.Point2(31, 6), sg.Point2(29, 8), sg.Point2(25, 6), sg.Point2(25, 2)]))
    plot.append(sg.Polygon([sg.Point2(15, 2), sg.Point2(22, 2), sg.Point2(20, 5), sg.Point2(15, 5)]))
    end = sg.Point2(30, 14)
else:
    plot.append(sg.Polygon([sg.Point2(0, 14), sg.Point2(1, 9), sg.Point2(7, 8), sg.Point2(9, 15), sg.Point2(6, 19)]))
    plot.append(sg.Polygon([sg.Point2(2, 6), sg.Point2(2, 1), sg.Point2(17, 1), sg.Point2(17, 6)]))
    plot.append(sg.Polygon([sg.Point2(10, 8), sg.Point2(14, 8), sg.Point2(12, 15)]))
    plot.append(sg.Polygon([sg.Point2(19, 3), sg.Point2(23, 6), sg.Point2(18, 10)]))
    plot.append(sg.Polygon([sg.Point2(14, 13), sg.Point2(20, 17), sg.Point2(18, 20), sg.Point2(14, 19)]))
    plot.append(sg.Polygon([sg.Point2(22, 9), sg.Point2(28, 9), sg.Point2(28, 19), sg.Point2(22, 19)]))
    plot.append(sg.Polygon(
        [sg.Point2(28, 1), sg.Point2(31, 2), sg.Point2(31, 6), sg.Point2(29, 8), sg.Point2(25, 6), sg.Point2(25, 2)]))
    plot.append(sg.Polygon([sg.Point2(32, 8), sg.Point2(34, 16), sg.Point2(31, 19), sg.Point2(29, 17)]))
    end = sg.Point2(34, 19)


start = sg.Point2(1, 3)
draw(start)
draw(end)
for x in plot:
    draw(x)

plt.show()

"""
def segment_of_pol(start, poly):

    seg_vector = list()  # lista di ritorno con tutti i possibili vettori
    vertices = list(poly.vertices)
    if start in vertices:
        print("true")
        for i in range(0, len(vertices)):
            if start == vertices[i]:
                seg_vector.append(sg.Segment2(vertices[i], vertices[(i+1)%len(vertices)]))    
                seg_vector.append(sg.Segment2(vertices[i], vertices[(i-1)]))
        return seg_vector

    for coord in poly.vertices:
        ps = sg.Segment2(start, coord)
        i = 0
        for i in range(-1, len(vertices) - 1):
            
            if vertices[i + 1] != coord and vertices[i] != coord:
                if sg.intersection(ps, sg.Segment2(vertices[i], vertices[i + 1])) != None:
                    break

        if i == (len(vertices) - 2):
            seg_vector.append(ps)

    return seg_vector


def intersection_pol(seg, poly):
    vertices = list(poly.vertices)
    

    for i in range(-1, len(vertices) - 1):
        p_int =  sg.intersection(seg, sg.Segment2(vertices[i], vertices[i + 1]))      

        if p_int != None:
            print(p_int) 
            if p_int != seg[0]:
                return True

    return False


def return_possible_segment(start, plot):
    final_list = list()
    for i in range(0, len(plot)):
        segments = segment_of_pol(start, plot[i])
        print(segments)
        if segments != None:
            for j in range(0, len(plot)):
                if j != i:
                    length = len(segments)
                    idx = 0
                    while idx < length:
                        if intersection_pol(segments[idx], plot[j]):
                            segments.remove(segments[idx])
                            idx -= 1
                            length -= 1
                        idx += 1
        for x in segments:
            final_list.append(x)

    for i in range (0, len(plot)):
        if intersection_pol(sg.Segment2(start, sg.Point2(34, 19)), plot[i]):
            break

    if i == (len(plot)-1):
        final_list.append(sg.Segment2(start, sg.Point2(34, 19)))

    return final_list
"""

