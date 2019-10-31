import pyglet
import math

window = pyglet.window.Window()

class Point:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z
        self.draw()

    def draw(self):
        pyglet.graphics.draw(1, pyglet.gl.GL_POINTS, ('v2i', (self._x, self._y)))

class Bezier:
    def __init__(self, point0, point1, point2, point3):
        self._point0 = point0
        self._point1 = point1
        self._point2 = point2
        self._point3 = point3

    def calculatePoint(self, t):
        Px = self._point0._x * (1 - t) ** 3 + 3 * self._point1._x * t * (1 - t) ** 2 + 3 * self._point2._x * (t ** 2) * (1 - t) + self._point3._x * (t ** 3)
        Py = self._point0._y * (1 - t) ** 3 + 3 * self._point1._y * t * (1 - t) ** 2 + 3 * self._point2._y * (t ** 2) * (1 - t) + self._point3._y * (t ** 3)
        point = Point(math.ceil(Px), math.ceil(Py), 0)

    def draw(self):
        n = 1000
        for i in range(0, n + 1):
            self.calculatePoint(i / n)

def calulateTangent(point0, point1, point2, t0, t1, t2):

    u = (t2 - t1) / (t2 - t0)

    x = point1._x - point0._x
    y = point1._y - point0._y
    z = point1._z - point0._z
    firstPoint = Point(x, y, z)

    x = point2._x - point1._x
    y = point2._y - point1._y
    z = point2._z - point1._z
    secondPoint = Point(x, y, z)

    firstFraction = (1 - u) / (t1 - t0)
    secondFraction = u / (t2 - t1)

    x1 = firstFraction * firstPoint._x
    y1 = firstFraction * firstPoint._y
    z1 = firstFraction * firstPoint._z

    x2 = secondFraction * secondPoint._x
    y2 = secondFraction * secondPoint._y
    z2 = secondFraction * secondPoint._z
    print(x1, y1, z1, x2,y2, z2)
    s = Point(math.ceil(x1 + x2), math.ceil(y1 + y2), math.ceil(z1 + z2))

    print(s._x, s._y, s._z)

@window.event
def on_draw():
    window.clear()
    p0 = Point(100, 20, 2)
    p1 = Point(20, 200, 4)
    p2 = Point(180, 40, 4)
    p3 = Point(260, 20, 4)
    bezier = Bezier(p0, p1, p2, p3)
    bezier.draw()

    p4 = Point(260, 20, 2)
    p5 = Point(300, 200, 4)
    p6 = Point(700, 400, 4)
    p7 = Point(500, 20, 4)
    bezier = Bezier(p4, p5, p6, p7)
    bezier.draw()

    calulateTangent(p2, p3, p5, 0.5, 1, 15)


pyglet.app.run()

