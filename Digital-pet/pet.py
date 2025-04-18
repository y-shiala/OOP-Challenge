class Pet :
  def __init__(self, name):
    self.name = name
    self.hunger = 5
    self.energy = 5
    self.happiness = 5
    self.tricks = []
  def eat(self):
    self.hunger = max(0, self.hunger - 3)
    self.happiness = min(10, self.happiness +1)  
    print(f"{self.name} is fed and the hunger level is {self.hunger}")

  def sleep(self):
    self.energy = min(10, self.energy + 5)  
    print(f"{self.name} is now recharged energy level at {self.energy}" )

  def play(self):
    if self.energy >= 2:
      self.energy -= 2
      self.happiness = min(10, self.happiness + 2)  
      self.hunger = min(10, self.hunger + 1 )
      print(f"{self.name} played and had fun! Energy: {self.energy} Happiness: {self.happiness}, Hunger: {self.hunger} ")
    else:
      print(f"{self.name} is too tired to play.Try sleeping first.") 
#Method to teach a new trick      
  def train(self, trick):
    self.tricks.append(trick) 
    self.happiness = min(10, self.happiness + 1)
    print(f"{self.name} Learnt a new trick: {trick}! Happiness: {self.happiness}") 
#Method to display all the tricks the pet has learnt       
  def show_tricks(self):
    if self.tricks:
      print(f"{self.name} Knows these tricks: {','.join(self.tricks)}")
    else:
      print(f"{self.name} hasn't learnt any tricks yet.")  

  def get_status(self):
      print(f"\n --- {self.name}'s current status ---")
      print(f"Energy: {self.energy}/10")
      print(f"Hunger: {self.hunger}/10")
      print(f"Happiness: {self.happiness}/10\n")

