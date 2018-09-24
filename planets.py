def weight_on_planets():
   earthstr = input("What do you weigh on earth?")
   ear = int(earthstr)
   mars = ear*0.38
   jup = ear*2.34
   print("\nOn Mars you would weigh %5.2f pounds.\nOn Jupiter you would weigh %6.2f pounds." %(mars, jup))
   
   
   
if __name__ == '__main__':
   weight_on_planets()
