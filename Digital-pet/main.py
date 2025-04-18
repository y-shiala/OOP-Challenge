#Importing Pet class from pet.py
from pet import Pet

#creating a new pet object named Snowy.
my_pet = Pet('Snowy')

#showimg the initial status of the pet.
my_pet.get_status()

#perfoming an action and showing updated status
print("\n --- Feeding ---")
my_pet.eat() #feeding the pet
my_pet.get_status()#showing the status after eating.

print("\n ---Playing ---")
my_pet.play() #Play with the pet
my_pet.get_status()#showing the status after playing.

print("\n --- Sleeping ---")
my_pet.sleep() #getting the pet to sleep
my_pet.get_status()#showing the status after sleeping.

print("\n --- Training ---")
my_pet.train('protect') #getting the pet to train.
my_pet.train('playing-fetching') #getting the pet to train.
my_pet.train('sitting-on-command') #getting the pet to train.
my_pet.show_tricks()#showing the tricks the pet has learnt.

