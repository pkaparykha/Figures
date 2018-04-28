import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import random
import math
import numpy as np

# number of images we are going to create in each of the two classes
nfigs = 4000

# Specify the size of the image.
# E.g. size=32 will create images with 32x32 pixels.
size = 32


def plot_figure(path_data, figure_class, type):
    # get the path data in the right format for plotting
    codes, verts = zip(*path_data)
    path = mpath.Path(verts, codes)
    # add shade the interior of the shape
    patch = mpatches.PathPatch(path, facecolor='gray', alpha=0.5)

    # initialise a new figure
    fig, ax = plt.subplots()
    ax.add_patch(patch)
    # set the scale of the overlall plot
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    # swith off plotting of the axis (only draw the shapes)
    plt.axis('off')
    # set the number of inches in each dimension to one
    # - we will control the number of pixels in the next command
    fig.set_size_inches(1, 1)
    # save the figure to file in te directory corresponding to its class
    # the dpi=size (dots per inch) part sets the overall number of pixels to the
    # desired value
    fig.savefig('e:\\Projects\\MachineLearning2\\data\\train\\' + figure_class + '\\data' + str(i)+ type + '.png', dpi=size)
    # close the figure
    plt.close(fig)


def constrict_figure(square, figure_class, type):


    negatives = sum((value[0] < 0 or value[0] > 1) for value in square)
    if(negatives >= 2):
        print ("   === Negatives =====")
        print(square)
        return

    overflows = sum((value[1] < 0 or value[1] > 1 ) for value in square)
    if (overflows >= 2):
        print("   === Overflow =====")
        print(square)
        return

    if clss == "squares":
        path_data1 = [
            (Path.MOVETO, (square[0][0], square[0][1])),  # move to base position of this image
            (Path.LINETO, (square[1][0], square[1][1])),
            (Path.LINETO, (square[2][0], square[2][1])),
            (Path.LINETO, (square[3][0], square[3][1])),
            (Path.LINETO, (square[0][0], square[0][1])),
        ]
    else:
        path_data1 = [
            (Path.MOVETO, (square[0][0], square[0][1])),
            (Path.LINETO, (square[1][0], square[1][1])),
            (Path.LINETO, (square[2][0], square[2][1])),
            (Path.LINETO, (square[0][0], square[0][1])),
        ]
    plot_figure(path_data1, figure_class, type)


def init_square():
    # set position and scale of each shape using random numbers
    # the coefficients are used to just try and prevent too many shapes from
    # spilling off the edge of the image
    basex = 0.7 * random.random()
    basey = 0.7 * random.random()
    length = max([0.2, 0.7 * random.random()])

    x1 = basex
    y1 = basey
    x2 = basex + length
    y2 = basey
    x3 = basex + length
    y3 = basey + length
    x4 = basex
    y4 = basey + length
    square = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
    return square

def init_triangle():
    basex = 0.7 * random.random()
    basey = 0.7 * random.random()
    length1 = max([0.2, 0.7 * random.random()])
    length2 = max([0.2, 0.7 * random.random()])
    length3 = max([0.2, 0.7 * random.random()])
    sign_operation = random.choice([1, -1])

    x1 = basex
    y1 = basey
    x2 = basex + length1
    y2 = basey
    x3 = basex + length2 * sign_operation
    y3 = basey + length3

    triangle = [[x1, y1], [x2, y2], [x3, y3]]
    return triangle



# loop over classes
for clss in ["squares", "triangles"]:
    print( "generating images of " + clss + ":")
    # loop over number of images to generate
    for i in range(nfigs):
        print(str(i))

        # initialise a new path to be used to draw on the figure
        Path = mpath.Path


        teta = 0.5 * random.random()

        rotate_matrix = [[math.cos(teta), -math.sin(teta)], [math.sin(teta), math.cos(teta)]]

        if clss == "squares":
            square1 = init_square()
            rotated = np.dot(rotate_matrix, np.transpose(square1))

            transposed = np.transpose(rotated)
            constrict_figure(transposed, clss, '')

        else:  # triangles
            triangle1 = init_triangle()
            rotated = np.dot(rotate_matrix, np.transpose(triangle1))
            transposed = np.transpose(rotated)
            constrict_figure(transposed, clss, '')

