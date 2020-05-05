# my_lambdata/polo.py

# attributes / properties (Nouns): size, style, color, texture, price
# method (VERBS): wash, fold, pop collar

class Polo():
    def __init__(self, size, color):
        self.size = size
        self.color = color

    def wash(self):
        print('WASHING THE POLO!')

    def fold(self):
        print('FOLDING THE POLO!')


if __name__ == "__main__":

    # inititalize a small blue polo and a large yellow polo

    p1 = Polo(size= 'Small', color= 'Blue')
    print(p1.size, p1.color)
    p1.wash()

    p2 = Polo(size= 'Large', color= 'Yellow')
    print(p2.size, p2.color)
    p2.fold()