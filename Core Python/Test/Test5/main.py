from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def calculate_toll(self):
        pass


class TwoWheeler(Vehicle):
    def __init__(self, num_persons):
        self.num_persons = num_persons

    def calculate_toll(self):
        toll = 20
        if self.num_persons > 2:
            toll += (self.num_persons - 2) * 10
        return toll


class ThreeWheeler(Vehicle):
    def __init__(self, num_persons):
        self.num_persons = num_persons

    def calculate_toll(self):
        toll = 30
        if self.num_persons > 3:
            toll += (self.num_persons - 3) * 20
        return toll


class FourWheeler(Vehicle):
    def __init__(self, num_persons):
        self.num_persons = num_persons

    def calculate_toll(self):
        toll = 40
        if self.num_persons > 4:
            toll += (self.num_persons - 4) * 40
        return toll


class HeavyVehicle(Vehicle):
    def __init__(self, num_persons):
        self.num_persons = num_persons

    def calculate_toll(self):
        toll = 60
        if self.num_persons > 6:
            toll += (self.num_persons - 6) * 100
        return toll


def main():
    while(choice <= 5):
        print("1. Two Wheeler")
        print("2. Three Wheeler")
        print("3. Four Wheeler")
        print("4. Heavy Vehicle")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if(choice == '5'):
            print("Exited Successfully!")
            break


        persons = int(input("Enter number of persons: "))

        if(choice == '1'):
            vehicle = TwoWheeler(persons)
        elif(choice == '2'):
            vehicle = ThreeWheeler(persons)
        elif(choice == '3'):
            vehicle = FourWheeler(persons)
        elif(choice == '4'):
            vehicle = HeavyVehicle(persons)
        else:
            print("Invalid choice! Try again.")
            continue

        toll = vehicle.calculate_toll()
        print(f"Total Toll to be paid:{toll}")

if(__name__ == '__main__'):
    main()