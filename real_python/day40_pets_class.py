class Dog:
    
    # Class Attribute
    # class attributes are the same for all instances
    species = 'mammal'
    is_hungry = True

    def __init__(self, name, age):
        """Initializer

        You will never have to call the __init__() method;
        it gets called automatically when you create a 
        new ‘Dog’ instance.
        """
        # Instance Attributes
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return '{} is {} years old.'.format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return '{} say {}'.format(self.name, sound)

    def eat(self):
        self.is_hungry = False

    def walk(self):
        return '{} is walking!'.format(self.name)


class Pets:

    dogs = []

    def __init__(self, dogs):
        if isinstance(dogs,list):
            self.dogs = dogs

    def add(self, dog):
        self.dogs.append(dog)

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())

    def listed_dogs(self):

        print('I have {} dogs.'.format(len(self.dogs)))

        for dog in self.dogs:
            print('{} is {}'.format(dog.name, dog.age))

        print('And they\'re all {}, of course'.format(Dog.species))

    def are_hungry(self):
        count_hungry = 0

        for dog in self.dogs:
            if dog.is_hungry:
                count_hungry += 1

        if count_hungry == 0:
            print('My dogs are not hungry')
        elif count_hungry == len(self.dogs):
            print('My dogs are very hungry')
        else:
            print('Now, Only {} dogs are hungry'.format(count_hungry))


if __name__ == '__main__':
    zeus = Dog('Zeus',7)
    negro = Dog('Negro',8)
    hashi = Dog('Hashi',3)

    pets = Pets([zeus, negro, hashi])
    pets.listed_dogs()
    pets.are_hungry()
    negro.eat()
    zeus.eat()
    pets.are_hungry()

    pets.walk()


        
