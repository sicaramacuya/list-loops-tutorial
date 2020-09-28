# Question 1 ------------------------------------------------------------
songs = ["ROCKSTAR", "Do It", "For The Night"]
# Question 2 ------------------------------------------------------------
print(songs[0])
print(songs[2])
print(songs[1:])
# Question 3 ------------------------------------------------------------
songs[2] = "Del Mar"
# Question 4 ------------------------------------------------------------
songs.extend(["Yo Perreo Sola", "UN DIA (ONE DAY) (Feat. Tainy)", "Mi Gente (feat. Beyoncé)"])
del songs[1]
# Question 6 ------------------------------------------------------------
animals = ["Honey Badger", "Tasmania Devil", "Hippopotamus"] # Create a list with 3 animals
animals.append("Polar Bear") # Add another animal
print(animals[2]) # Print out the 3rd animal
del animals[0] # Delete the firs animal

for animal in animals: # Use a loop to print out all animals
    print(animal)