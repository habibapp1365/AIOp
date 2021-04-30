class circle(object):

    pi= 3.14

    def __init__(self,radius = 10):
        self.radius = radius

    def get_area(self):
        return self.radius**2 * circle.pi

qaz = circle()
qaz.radius=20
print(qaz.get_area())