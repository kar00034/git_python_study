class Bicycle():
    def __init__(self, wheel_size, color):
        self.wheel_size = wheel_size
        self.color = color

    def move(self, speed):
        print("자전거: 시속 {} 킬로미터로 전진".format(speed))

    def turn(self, direction):
        print("자전거: {}회전".format(direction))

    def stop(self):
        # print("자전거({},{}) : 정지".format(self.wheel_size, self.color))
        pass    #추상 클래스

    def __str__(self) -> str:
        return "자전거 wheel_size : {}, color : {}".format(self.wheel_size, self.color)


class FoldingBicycle(Bicycle):
    def __init__(self, wheel_size=20, state='unfolding', color='black'):
        Bicycle.__init__(self, wheel_size, color)
        # super().__init__(wheel_size,color)
        self.state = state

    def fold(self):
        self.state = 'folding'
        print("자전거: 접기, state = {}".format(self.state))

    def unfold(self):
        self.state = 'unfolding'
        print("자전거: 펴기, state = {}".format(self.state))

    def move(self, speed):
        print("접는 자전거: 시속 {} 킬로미터로 전진".format(speed))

    def __str__(self) -> str:
        return "{}, {}".format(super().__str__(), self.state)

    def stop(self):
        print("접는 자전거: 시속 {}킬로미터로 정지".format(0))
