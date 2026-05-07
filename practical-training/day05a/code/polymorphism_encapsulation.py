class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal: Animal):
    print(animal.speak())

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.__balance

if __name__ == "__main__":
    print("--- Polymorphism Test ---")
    dog = Dog()
    cat = Cat()
    animal_sound(dog)
    animal_sound(cat)

    print("\n--- Encapsulation Test ---")
    account = BankAccount("Alice", 1000)
    print(f"Initial balance: {account.get_balance()}")
    account.deposit(500)
    account.withdraw(200)

    # Trying to tamper with the private attribute
    account.__balance = 9999999 # This creates a new attribute on the instance, doesn't change the private one
    print(f"Attempted to tamper. Balance is still: {account.get_balance()}")
    print(f"The tampered fake balance is: {account.__balance}")
