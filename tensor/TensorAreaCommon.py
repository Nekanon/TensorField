import tensor.SimpleTensor as ST
import math


class TensorAreaCommon:
    def __init__(self, size):
        self.size = size
        self.area = []
        position = []
        self.conditions = {}

    # def setConditions(self, position, power, mutable=False):
    #     for cel in self.area:
    #         if cel.getPosition() == position:
    #             cel.setPower(power)
    #             cel.setMutable(mutable)
    #
    # def getLength(self, array1, array2):
    #     length = 0
    #     for row in range(len(array1)):
    #         length += (array1[row]-array2[row])**2
    #
    #     return math.sqrt(length)
    #
    # def getAround(self, position):
    #     result = []
    #     for row in self.area:
    #         if self.getLength(position, row.getPosition())<=1 and self.getLength(position, row.getPosition())>0:
    #             result.append(row)
    #     return result


