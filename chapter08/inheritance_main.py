from chapter08.inheritance_study import Bicycle, FoldingBicycle

if __name__ == "__main__":
    myBicycle = Bicycle(wheel_size=26, color='red')
    myFoldBicycle = FoldingBicycle(wheel_size=30, color="blue")

    cyclelist = [myBicycle, myFoldBicycle]

    [cycle.move(30) for cycle in cyclelist]
    [cycle.stop() for cycle in cyclelist]   #부모 클래스는 pass
