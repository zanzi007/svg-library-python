import svg
import random

def main():

    """
    Try out the SVG class by calling function to
    create and save a few drawings.
    """

    print("-----------------")
    print("| codedrome.com |")
    print("| SVG Library   |")
    print("-----------------")
    print("Bezier exstention by Zanzi")

    draw_all_shapes()

    #i_want_to_believe()

    #mondrian()


def draw_all_shapes():

    """
    Quick demo of creating SVG object, using all methods,
    and saving the finished file.
    """

    s = svg.SVG()

    s.create(256, 192)

    s.fill("#A0A0FF")
    s.circle("#000080", 4, "#0000FF", 32, 64, 96)
    s.line("#000000", 2, 8, 8, 248, 184)
    s.rectangle(64, 64, 112, 32, "#00FF00", "#008000", 4, 4, 4)
    s.text(32, 16, "sans-serif", 16, "#000000", "#000000", "Merry Christmas codedrome.com from Alex Pedersen")
    s.ellipse(64, 160, 32, 16, "#FF0000", "#800000", 4)
    d = ('M' +' ' + str(120) + ' ' + str( 150) + ',' +' ' + 'C' + ' ' + str( 110) + ' ' +str( 80) + ' ' + str( 110) +
         ' ' + str(80) +',' + ' ' + str( 220) + ' ' + str(190))
    
    s.path("white", "white",  2, d )

    s.finalize()

    try:
        s.save("allshapes.svg")
    except IOError as ioe:
        print(ioe)

    print(s)

main()
