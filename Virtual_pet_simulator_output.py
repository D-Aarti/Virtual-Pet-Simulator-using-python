import time
import random
# Define a class for the virtual pet
class VirtualPet:
    def __init__(self, name):
    # Set the pet's name and initial status

        self.name = name
        self.happiness = 50 # Starts at 50
        self.hunger = 50  # Starts at 50
        self.actions_count = 0 # Count how many actions the user has taken

    def feed(self):
    # Feeding decreases hunger but slightly decreases happiness

        self.hunger = max(0, self.hunger - 15)# Avoid going below 0
        self.happiness = max(0, self.happiness - 5)
        print(f"You fed {self.name}. Hunger decreased, but happiness slightly decreased.")

    def play(self):
    # Playing increases happiness but slightly increases hunger

        self.happiness = min(100, self.happiness + 15)  # Avoid going above 100
        self.hunger = min(100, self.hunger + 5)
        print(f"You played with {self.name}. Happiness increased, but hunger slightly increased.")

    def check_status(self):
    # Display current happiness and hunger

        print(f"\n{self.name}'s Status:")
        print(f"Happiness: {self.happiness}")
        print(f"Hunger: {self.hunger}")
                # If hunger is too high, happiness drops more

        if self.hunger > 80:
            print(f"{self.name} is very hungry and is becoming sad!")
            self.happiness = max(0, self.happiness - 10)

    def time_passes(self):
    # Increase hunger and decrease happiness every few actions

        self.actions_count += 1
        if self.actions_count % 3 == 0:
            self.hunger = min(100, self.hunger + 5)
            self.happiness = max(0, self.happiness - 5)
            print(f"\nTime passes... {self.name} is getting hungrier and less happy.")

    def is_game_over(self):
                # Check if hunger or happiness hits a critical point

        if self.hunger >= 100:
            print(f"\nOh no! {self.name} got too hungry. Game over.")
            return True
        elif self.happiness <= 0:
            print(f"\nOh no! {self.name} became too sad. Game over.")
            return True
        return False


def pet_simulator():
    # Main game function

    print("!!!!!!!!.....Welcome to the Virtual Pet Simulator.....!!!!!!!")
    pet_name = input("What would you like to name your pet? ")
    pet = VirtualPet(pet_name)
    # Main game loop

    while True:
        print("\n--- Menu ---")
        print("1. Feed Pet")
        print("2. Play with Pet")
        print("3. Check Pet's Status")
        print("4. Quit Game")

        choice = input("Choose an action (1-4): ")

        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.check_status()
        elif choice == '4':
            print(f"Thanks for playing!!!! Goodbye from {pet.name}!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

        pet.time_passes()

        if pet.is_game_over():
            break

# Run the game
if __name__ == "__main__":
    pet_simulator()
