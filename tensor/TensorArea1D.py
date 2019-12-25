import tensor.SimpleTensor as ST
import math


class TensorArea1D:
    def __init__(self, length=2):
        self.length = length
        self.area = []
        for i in range(length):
            st = ST.SimpleTensor([i], 1.5)
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
            length += (array1[row]-array2[row])**2

        return math.sqrt(length)

    def getAround(self, position):
        result = []
        for row in self.area:
            if self.getLength(position, row.getPosition())<=1 and self.getLength(position, row.getPosition())>0:
                result.append(row)
        return result

    def calculateOne(self):
        result = []
        for cel in self.area:
            if cel.getMutable():
                #area arount
                new_power = 0
                aroundCel = self.getAround(position=cel.getPosition())
                for newCel in aroundCel:
                    current_power = cel.getPower()
                    neigh_power = newCel.getPower()
                    new_power += (neigh_power - current_power)*cel.getMaterial()*0.1
                cel.setPower(cel.getPower() + new_power)
                result.append(round(cel.getPower(), 1))
        return result

