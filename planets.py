def weight_on_planets():
    ear = int(input("What do you weigh on earth? "))
    mars = ear*0.38
    jup = ear*2.34
    print("\nOn Mars you would weigh %.2f pounds.\nOn Jupiter you would weigh %.2f pounds." %(mars, jup))
   
   
   
if __name__ == '__main__':
   weight_on_planets()
