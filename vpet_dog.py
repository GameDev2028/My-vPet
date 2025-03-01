class VPetDog:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50

    def feed(self):
        if self.hunger < 100:
            self.hunger += 10
            self.energy += 5
            print(f"You fed {self.name}.")
        else:
            print(f"{self.name} is not hungry.")

    def play(self):
        if self.energy > 0:
            self.happiness += 10
            self.energy -= 10
            print(f"You played with {self.name}.")
        else:
            print(f"{self.name} is too tired to play.")

    def check_status(self):
        print(f"{self.name}'s Status:")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")

    def rest(self):
        if self.energy < 100:
            self.energy += 20
            print(f"{self.name} is resting.")
        else:
            print(f"{self.name} is already fully rested.")


def main():
    name = input("What is your vPet dog's name? ")
    dog = VPetDog(name)

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Check Status")
        print("4. Rest")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            dog.feed()
        elif choice == "2":
            dog.play()
        elif choice == "3":
            dog.check_status()
        elif choice == "4":
            dog.rest()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()