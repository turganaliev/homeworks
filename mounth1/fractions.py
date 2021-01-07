class Drob:

    def __init__(self, chislitel, znamenatel):
        self.chislitel = chislitel
        self.znamenatel = znamenatel


    def __mul__(self, other):
        new_chislitel = self.chislitel * other.chislitel
        new_znamenatel = self.znamenatel * other.znamenatel

        return Drob(new_chislitel, new_znamenatel)


    def __truediv__(self, other):
        new_chislitel = self.chislitel * other.znamenatel
        new_znamenatel = self.znamenatel * other.chislitel

        return Drob(new_chislitel, new_znamenatel)


    def __add__(self, other):
        if self.znamenatel == other.znamenatel:
            new_chislitel = self.chislitel + other.chislitel
            new_znamenatel = self.znamenatel
            return Drob(new_chislitel, new_znamenatel)

        if self.znamenatel != other.znamenatel:
            new_chislitel = (self.chislitel * other.znamenatel) + (other.chislitel * self.znamenatel)
            new_znamenatel = self.znamenatel * other.znamenatel
            return Drob(new_chislitel, new_znamenatel)


    def __sub__(self, other):
        if self.znamenatel == other.znamenatel:
            new_chislitel = self.chislitel - other.chislitel
            new_znamenatel = self.znamenatel
            return Drob(new_chislitel, new_znamenatel)
        if self.znamenatel != other.znamenatel:
            new_chislitel = (self.chislitel * other.znamenatel) - (other.chislitel * self.znamenatel)
            new_znamenatel = self.znamenatel * other.znamenatel
            return Drob(new_chislitel, new_znamenatel)

    def __str__(self):
        return f"{self.chislitel}\n{max(len(str(self.znamenatel)), len(str(self.chislitel))) * '-'}\n{self.znamenatel}"


drob1 = Drob(5, 6)
drob2 = Drob(3, 2)
drob3 = drob1 - drob2
print(drob3)

drob1 = Drob(1, 2)
drob2 = Drob(1, 3)
drob3 = drob1 + drob2
print(drob3)

drob1 = Drob(1, 5)
drob2 = Drob(5, 1)
drob3 = drob1/drob2
print(drob3)

drob1 = Drob(20, 6)
drob2 = Drob(3, 9)
drob3 = drob1 * drob2
drob4 = drob3 * drob1
print(drob4)

# 1 2/3
# sokrasheniye drobei
