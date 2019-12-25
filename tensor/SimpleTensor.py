class SimpleTensor:
    def __init__(self, position, material):
        self.desidion = len(position)
        self.position = position
        self.material = material
        self.power = 0
        self.mutable = True

    def setMaterial(self, material):
        self.material = material

    def getMaterial(self):
        return self.material

    def getPosition(self):
        return self.position

    def getPower(self):
        return self.power

    def setPower(self, power):
        self.power = power

    def setMutable(self, mutable):
        self.mutable = mutable

    def getMutable(self):
        return self.mutable
