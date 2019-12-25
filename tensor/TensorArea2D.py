import tensor.SimpleTensor as ST
import math

class TensorArea2D:
    def __init__(self, size=[2, 2], thermalConductivity=1.0):
        self.size = size
        self.area = []
        for i in range(size[0]):
            for j in range(size[1]):
                st = ST.SimpleTensor([i, j], thermalConductivity)
                self.area.append(st)
        self.conditions = {}

    def setConditions(self, position, power, mutable=False):
        for cel in self.area:
            if cel.getPosition() == position:
                cel.setPower(power)
                cel.setMutable(mutable)

    def getLength(self, array1, array2):
        length = 0
        for row in range(len(array1)):
            length += (array1[row] - array2[row]) ** 2

        return math.sqrt(length)

    def getAround(self, position):
        result = []
        for row in self.area:
            if self.getLength(position, row.getPosition()) <= 1 and self.getLength(position, row.getPosition()) > 0:
                result.append(row)
        return result

    def calculateOne(self):
        newArrayCel = []

        result = []
        for cel in self.area:
            if cel.getMutable():
                # area arount
                new_power = 0
                aroundCel = self.getAround(position=cel.getPosition())
                for newCel in aroundCel:
                    current_power = cel.getPower()
                    neigh_power = newCel.getPower()
                    new_power += (neigh_power - current_power) * cel.getMaterial() * 0.1
                newCel = cel
                newCel.setPower(cel.getPower() + new_power)
                result.append( {"pos": cel.getPosition(), "pow": round(newCel.getPower(), 1)} )

                newArrayCel.append(newCel)

        for row in newArrayCel:
            for rowOld in self.area:
                if row.getPosition() == rowOld.getPosition():
                    rowOld.setPower(row.getPower())
        return result

#Need:
#1. Determinate more difficult mechanism for material point
#2. New block conditions
#3. Visualization
#4.