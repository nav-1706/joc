import random

print("Random integer by randint")

a = random.randint(1,5) # both 1 and 5 inclsive
print(a)
print(random.randint(1,5));
print(random.randint(1,5));
print(random.randint(1,5));
print(random.randint(1,5));
print(random.randint(1,5));

print("Random integer by randrange")

b = random.randrange(1,5) # lower_limit and upper_limit-1 inclusive
print(b);
print(random.randrange(1,5));
print(random.randrange(1,5));
print(random.randrange(1,5));
print(random.randrange(1,5));

print("Random integer by randrange with steps")

print(random.randrange(1,10, 2)); # lower_limit, lower_limit, range --> form 1 to 9 with gap of 2, --> generate always odd number
print(random.randrange(1,10, 2));
print(random.randrange(1,10, 2));
print(random.randrange(1,10, 2));
print(random.randrange(1,10, 2));

print(random.randrange(2,10, 2)); # wil generate only even number
print(random.randrange(2,10, 2));
print(random.randrange(2,10, 2));
print(random.randrange(2,10, 2));
print(random.randrange(2,10, 2));
 
print("Random number by random.random") # reand decimal number b/w 0 and 1 both exclusive

c = random.random();
print(c);
print(random.random());
print(random.random());
print(random.random());
print(random.random());
print(random.random());
print(random.random());

print("Random number by random.choise") # choose a random value from the given list

d = random.choice([1,2,3,4,5,6,7,8])
print(d);

print(random.choice([1,2,3.2,4,5,6,7.4,8]))
print(random.choice([1,2,3.2,4,5,6,7.4,8]))
print(random.choice([1,2,3.2,4,5,6,7.4,8]))
print(random.choice([1,2,3.2,4,5,6,7.4,8]))
print(random.choice([1,2,3.2,4,5,6,7.4,8]))
print(random.choice([1,2,3.2,4,5,6,7.4,8]))