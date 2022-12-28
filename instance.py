class car:
    def sample_car_instance_method(self,a):
        print(a)
carObj=car()
carObj.sample_car_instance_method("Hello again!")

class car:
    someclassdummyvar='dummy'
    def sample_car_instance_method(self,a):
        print(a)
        print(self.someclassdummyvar)
carObj2=car()
carObj2.sample_car_instance_method(2)


class car:
    def __int__(self,color,max_speed,start_engine,acceleration,tyre_friction,current_speed):
        self.color=color
        self.max_speed=max_speed
        self.accelration=acceleration
        self.tyre_friction=tyre_friction
        self.start_engine=False
        self.current_speed=0
        print(self.color,max_speed,start_engine,acceleration,tyre_friction,current_speed)
    def start_engine(self):
        self.start_engine=True
        print("car engine is turned on",self.start_engine)
    def stop_engine(self):
        self.start_engine=False
        print("car engine is turned off",self.start_engine)





class shopping_cart:
    def __int__(self):
        self.cart_items={"mobile"=10000,"laptop"=200000}
        