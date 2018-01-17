class Player(object):
     def __init__(self, name):
         self.name = name
         self.pieces = []

     def __str__(self):
        return self.name
