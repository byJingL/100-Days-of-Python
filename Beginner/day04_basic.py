import random
import mymodule

print(mymodule.pi)

#Random Module
random_int = random.randint(1, 10) #[1, 10]
print(random_int)

random_float1 = random.random() #[0,1)
random_float2 = random.uniform(0, 5)
print(random_float2)
