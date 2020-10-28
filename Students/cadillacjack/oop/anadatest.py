import requests
class Machine:
  destruction_power = 20
  def __init__(self, power, speed, control):
    self.power = power
    self.speed = speed
    self.control = control
  def increase_speed(self):
    self.speed = self.speed * 5
    return self.speed
  @classmethod
  def berserk_mode(cls, amount):
    cls.destruction_power = amount
  @staticmethod
  def tell_joke():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    data = response.json()
    print(data["value"])
jeeg_robot = Machine(10, 20, 30)
#class method:
Machine.berserk_mode(50)
(jeeg_robot.destruction_power)

#static method
jeeg_robot.tell_joke()