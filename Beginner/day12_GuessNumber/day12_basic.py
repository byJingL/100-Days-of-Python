################### Scope ####################

# Modify Global Scope: do not want to modify it in a 

enemies = 1 # Global Scope

def increase_enemies():

    # can use global function
    print(f"enemies inside function: {enemies}") 
    return enemies + 1

increase_enemies()
print(f"enemies outside function: {enemies}")

enemies = increase_enemies()
print(f"enemies outside function2: {enemies}")

# Be careful to use global scope variables
# Can use Global Constants
pi  = 3.14 # never to change
URL = "http"

# Local scope: in the function
# Global scope: out of the function
# No block scope: such as if block, while statement

game_level  = 3

enemies = ["skelenten", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy) # No bug

game_level  = 4

def game():
    enemies2 = ["skelenten", "Alien"]
    if game_level < 5:
        new_enemy2 = enemies2[0]

#print(new_enemy2) #😢 Have  NameError