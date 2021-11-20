import math

class Robot():

  nombre_robot = str('Brazo Robotico')
  articulaciones = ['cintura', 'hombro', 'brazo', 'antebrazo', 'muñeca', 'mano']

  def setname (self):
     nombre = input("Cambie el nombre del manipulador ")

  def getname(nombre):
    print(nombre)

  def variables (self):
    x1 = (1/8*math.cos(30*math.sin(t2*t3*t4)+25*math.cos(t2*t3*t4)+36*math.cos(t2*t3)+54*math.cos(t2)))
    y1 = (1/8*math.sin(30*math.sin(t2*t3*t4)+25*math.cos(t2*t3*t4)+36*math.cos(t2*t3)+54*math.cos(t2)))
    z1 = ((25/8)-(15/4)*math.cos(t2*t3*t4)+(25/8)*math.sin(t2*t3*t4)+(9/2)*math.sin(t2*t3)+(27/4)*math.sin(t2))

    x = math.radians(x1)
    y = math.radians(y1)
    z = math.radians(z1)

    print(f"posicion x =  {x}, \nposicion y = {y},\nposicion z =  {z}")

t1 = 90
t2 = 0
t3 = 120
t4 = 90

def main():
    pose = Robot()
    print(pose.nombre_robot)
    pose.setname()
    pose.getname()
    print(f"Articulaciones:  {pose.articulaciones}")
    pose.variables()

if __name__ == "__main__":
    main()
