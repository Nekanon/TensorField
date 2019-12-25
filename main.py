import tensor.TensorArea1D as oned
import tensor.TensorArea2D as twod
import tensorFlowMy.TestOne as to

def main():
    # ta1D = oned.TensorArea1D(length=4)
    # ta1D.setConditions([0], 200.0)
    # ta1D.setConditions([1], -200.0, True)
    # ta1D.setConditions([2], 200.0, True)
    # ta1D.setConditions([3], -200.0)
    # for i in range(25):
    #     print(ta1D.calculateOne())

    size = [3, 3]
    ta2D = twod.TensorArea2D(size=size, thermalConductivity=2.0)
    ta2D.setConditions([0, 0], 20.0)
    ta2D.setConditions([2, 2], -20.0)
    for i in range(25):
        print(ta2D.calculateOne())

    # t1 = to.TestOne()
    # t1.t1()

if __name__=="__main__":
    main()