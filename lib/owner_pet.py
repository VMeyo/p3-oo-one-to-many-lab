class Pet:
    # Class variable to store all pet types
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    # Class variable to store all instances of Pet
    all = []

    def __init__(self, name, pet_type, owner=None):
        # Instance attributes
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        # Validate pet_type
        if self.pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type.")

        # Add the pet instance to the all list
        Pet.all.append(self)

        # If an owner is provided, add this pet to the owner's list of pets
        if self.owner is not None:
            if isinstance(self.owner, Owner):
                self.owner.add_pet(self)
            else:
                raise Exception("owner must be an instance of Owner class.")

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []  # Instance attribute to store pets

    def get_pets(self):  # Renamed from pets() to get_pets() to avoid conflict
        return self.pets

    def add_pet(self, pet):
        # Validate that pet is an instance of Pet
        if isinstance(pet, Pet):
            self.pets.append(pet)
            pet.owner = self  # Ensure that the owner is set on the pet
        else:
            raise Exception("pet must be an instance of Pet class.")

    def get_sorted_pets(self):
        # Return the pets sorted by their names
        return sorted(self.pets, key=lambda pet: pet.name)
