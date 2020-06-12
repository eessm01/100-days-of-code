class Dog:
    
    # Class Attribute
    # class attributes are the same for all instances
    species = 'mammal'

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


# child class (inherints from Dog class)
class RussellTerrier(Dog):
    def eat(self, food):
        return '{} eats {}'.format(self.name, speed)


# Child class (inherits from Dog class)
class BullDog(Dog):
    def run(self, speed):
        return '{} runs {}'.format(self.name, speed)
 

# Determine the oldest dog
def get_biggest_number(*args):
    return max(args)


if __name__ == '__main__':
    a = Dog('lala',2)
    print(type(a))  # <class '__main__.Dog'>

    # Instantiate the Dog objetcs
    philo = Dog('Philo', 5)
    mikey = Dog('Mikey', 6)
    lolo = Dog('Lolo',3)

    # Access the instance attributes
    print('{} is {} and {} is {}'.format(
        philo.name, philo.age, mikey.name, mikey.age
    ))

    # Is Philo a mammal?
    if philo.species == 'mammal':
        print('{1} is a {0}'.format(philo.species, philo.name))


    print('The oldest dog is {} years old.'.format(
        get_biggest_number(philo.age, mikey.age, lolo.age)
    ))

    zeus = Dog('Zeus',8)
    print(zeus.speak('Gruff Gruff'))

    # Child classes inherit attributes 
    # and behaviors from the parent class
    jim = BullDog('Jim', 10)
    print(jim.description())

    # Child classes have specific attributes
    # and behaviors as well
    print(jim.run('slowly'))

    # Is jim an instanceof Dog?
    print(isinstance(jim, Dog))

    # Is jim an instanceof Dog?
    julie = Dog('Julie',6)
    print(isinstance(julie,Dog))

    # Is jonny walker an instance of 
    # Bulldog or RussellTerrier?
    jonnywalker = RussellTerrier('Johny Walker',3)
    print(isinstance(jonnywalker, BullDog))
    print(isinstance(jonnywalker, RussellTerrier))

    # Is jules and instance of jim?
    print(isinstance(julie, jim))