import random


# TODO: Implement the Die class as follows...
class Die:
 # 1) Add the class declaration. Use the following class comment.
    """A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
    """
    

        # 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """Constructs a new instance of Die with a value and points attribute.

        Args:
            self (Die): An instance of Die.
        """
        self.value = 0
        self.points = 0

        # 3) Create the roll(self) method. Use the following method comment.
    def roll(self):
        """Generates a new random value and calculates the points.
        
        Args:
            self (Die): An instance of Die.
        """
        self.value = random.randint(1, 6) 
        self.points = 50 if self.value == 5 else 100 if self.value == 1 else 0 




# import random

# class Card:# Card class declaration
#     """Hilo is a game in which the player guesses if the next 
#     card drawn by the dealer will be higher or lower than the previous one.
    
#     the responsability of the Card is to keep track the point and generate new card """
    
#     def __init__(self):# Constructs a new instance of Card with value and points attributs.
#         self.value_rand = 0 # the value_rand represent the random card
#         self.value_player = 0 #the value_player represent the user guess card
#         self.points = 300 

#     def card(self):
#         """ card Generates a new random card from 1 to 13. and calculates the points. The number represent a card."""
#         self.value_rand = random.randint(1, 13)
#         #self.val_return += 1
#         return self.value_rand
    
#     def low(self):
#         """
#         if player's guesses is lower,100 points are won. Otherwise they lose 75 points."""
#         if self.value_player < self.value_rand:
#             return self.points + 100
#         else: 
#             self.value_player > self.value_rand
#             return self.points - 75

#     def high(self):
#         """if player's guesses is higher,100 points are won. Otherwise they lose 75 points."""
#         if self.value_player > self.value_rand:
#             return self.points + 100
#         else:
#             self.value_player < self.value_rand
#             return self.points - 75
