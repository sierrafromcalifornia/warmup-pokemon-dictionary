<center> <h1>Pokemon/Dictionary Warmup</h1> </center>

![Pokeball](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSvFguv_4hYhwny0d7KdBcFYHYCZ0j2uEBtr3aYmJHqNKecqEsi&usqp=CAU)

Joél is currently playing the Pokemon Crystal video game. 

Joél takes pokemon very seriously so they have downloaded [The Complete Pokemon Dataset](https://www.kaggle.com/rounakbanik/pokemon) from Kaggle and they need some help organizing the data.

Let's use our dictionary parsing skills to help Joél out!

**In the cell below,** we import the Pokemon Dataset.

*Don't worry about this code for now. Just run the cell ☺️*


```python
import json
import os

path = os.path.join('data', 'pokemon.json')
with open(path, 'r') as fp:
    data = json.load(fp)
```


```python
#__SOLUTION__
import json
import os

path = os.path.join('data', 'pokemon.json')
with open(path, 'r') as fp:
    data = json.load(fp)
```

Let's take a look at the data we just imported.


```python
data
```


```python
# __SOLUTION__
data
```

## Please answer the following questions below.

**What datatype is the data above?**

**What else can you say about the data variable?**


```python
# __SOLUTION__
# The `data` variable is a dictionary datatype.

# The data variable contains nested dictionaries for 4 out of 5 top level keys.
```

## Variable Assignment & Data Types – Practice

Variable assignment is important! Writing professional quality code will often times require you to be very thoughtful about how you assign your variables. You may be asked to define a variable with a specific name, or with a specific data type. In scenarios like this, if you were to give a variable the incorrect name or incorrect data type, the entire project could break!

The importance of how you define variables will be seen out at the end of this notebook where you will be asked to create variables that you will then submit to your instructor.  

**Let's take a look at some examples.**

<u>The following information is true about Joél's pokemon.</u>

- Joél has caught `5` pokemon
- Joél's pokemon trainer level is `'Apprentice'`.
- Joél's coolest pokemon is `'Haunter'`.
- Joél's favorite pokemon is `'Kadabra'`.
- Joél plays pokemon for 1.5 hours a day.

<u>Additionally, the names of Joél's five pokemon are:</u>

1. Bayleef
2. Haunter
3. Poliwag
4. Pidgeotto
5.  Kadabra

### Please create the following variables given the information above:

- `pokemon_count` that has a datatype of integer.
- `trainer_level` that has a datatype of string.
- `coolest_pokemon` that has a datatype of string.
- `favorite_pokemon` that has a datatype of string.
- `hours_per_day` that has a datatype of float.
- `joels_pokemon_names` that has a datatype of list.


```python
# Your code here
```


```python
# __SOLUTION__
pokemon_count = 5
trainer_level = 'Apprentice'
coolest_pokemon = 'Haunter'
favorite_pokemon = 'Kadabra'
hours_per_day = 1.5
joels_pokemon_names = ['Bayleef', 'Haunter', 'Poliwag', 'Pidgeotto', 'Kadabra']
```

The cell below tests whether or not you assigned your variables correctly!


```python
from tests import VariableAssignment

test = VariableAssignment()

test.run(pokemon_count, trainer_level, 
         coolest_pokemon, favorite_pokemon,
        hours_per_day, joels_pokemon_names)
```


```python
# __SOLUTION__
from tests import VariableAssignment

test = VariableAssignment()

test.run(pokemon_count, trainer_level, 
         coolest_pokemon, favorite_pokemon,
        hours_per_day, joels_pokemon_names)
```

# Looping

Looping is the bread and butter of code. Code is powerful because of it's speed and is especially skilled at completing repetitive tasks. 

### A simple for loop

Let's loop over the `joels_pokemon_names` list and print out each of the pokemon.


```python
# Your code here
```


```python
# __SOLUTION__

for name in joels_pokemon_names:
    print(name)

```

### Looping over a dictionary

To loop over a dictionary we will need to loop over the keys of the dictionary. 

<u>In the cell below,</u> 

- Assign the variable `data_keys` to a list containing the keys for the `data` variable.


```python
# Your code here
```


```python
# __SOLUTION__
data_keys = list(data)
```

### How many keys are in this dictionary?

In the cell below, set the variable `pokemon_total` to the number of keys in the dictionary.


```python
# Your code here
```


```python
# __SOLUTION__
pokemon_total = len(data_keys)
```

### Simple loop over dictionary

Now let's loop over the dictionary and save the top level value to a list called `pokedex`.


```python
# Your code here
```


```python
# __SOLUTION__
pokedex = []
for key in data_keys:
    pokedex.append(data[key])
```

#### Sort of a side question:

> The list we just made is the information for every pokemon in the dataset without the names. 

> What is a built in function that allows us to create a list of tuples that "zip" the names and the values together?


```python
# Your code here
```


```python
# __SOLUTION__
list(zip(data_keys, pokedex))
```

### Let's create a new dictionary called ```joels_pokemon```. 

To do this, we will:
1. Create an empty dictionary called ```joels_pokemon```
2. Loop over the names in the ```joels_pokemon_names``` list
3. Use the name to access the pokemon's information in the ```data``` dictionary
4. Add the pokemon name to the ```joels_pokemon``` dictionary as a ```key``` and the pokemon's information as the key's ```value```


```python
# Your code here
```


```python
# __SOLUTION__
joels_pokemon = {}

for pokemon in joels_pokemon_names:
    joels_pokemon[pokemon] =  data[pokemon]
```

Run the cell below to see if you successfully made the joels_pokemon dictionary!


```python
from tests import CheckDictionary

test = CheckDictionary(joels_pokemon)
test.run()
```


```python
# __SOLUTION__
from tests import CheckDictionary

test = CheckDictionary(joels_pokemon)
test.run()
```

# Visualization

Let's figure out which pokemon is Joél's strongest pokemon!

<u>In the cell below</u> 

- Create a  bar plot for that shows the attack stat for each of joel's 5 pokemon.
- Give the plot the following title: `Joel's pokemon stats`.


```python
# Your code here
```


```python
# __SOLUTION__
import matplotlib.pyplot as plt

attack_stats = [joels_pokemon[pokemon]['stats']['attack'] for pokemon in joels_pokemon]
names = list(joels_pokemon)

plt.bar(names, attack_stats)
plt.title("Joél's pokemon stats");
```

**What if we wanted to sort the graph?**

There is a couple ways we can do this, but a useful way of doing it would be to sort the dictionary itself!


```python
sorted_dict = dict(sorted(joels_pokemon.items(), key=lambda item: item[1]['stats']['attack']))

attack_stats = [sorted_dict[pokemon]['stats']['attack'] for pokemon in sorted_dict]
names = list(sorted_dict)

plt.bar(names, attack_stats)
plt.title("Joél's pokemon stats");
```


```python
# __SOLUTION__
sorted_dict = dict(sorted(joels_pokemon.items(), key=lambda item: item[1]['stats']['attack']))

attack_stats = [sorted_dict[pokemon]['stats']['attack'] for pokemon in sorted_dict]
names = list(sorted_dict)

plt.bar(names, attack_stats)
plt.title("Joél's pokemon stats");
```

![](https://gamepress.gg/pokemonmasters/sites/pokemonmasters/files/styles/300h/public/2019-08/pm0153_00_bayleaf_256.ktx.png?itok=Tr7OMsm1)

**Bayleef** is Joél's strongest pokemon. Let's create a list of all Pokemon that Bayleef is weak against.

Our dictionary gives us the *Types* of pokemon Bayleef is weak to. Our dictionary also gives us the type for each pokemon. So first we have to figure out what types of pokemon Bayleef is weak to, then grab every pokemon that has that type.

**Ok, here is how we will do it.**

*Weakness* is measured with the ```weakness``` key in our data. If the weakness value = 2, that means the pokemon is extremely weak to that type of pokemon. 

To find all pokemon that Bayleef is weak to, we have to:
1. Isolate Bayleef's weakness data from our dictionary
2. Identify any type that has a weakness score of 2 and append those types to a list called ```weakness_types```
3. Loop over our entire dataset
4. Identify pokemon who have a type that match the types in our ```weakness_types``` list.
> **Hint** The type of each pokemon can be found using the ```stats``` key
5. Append the names of those pokemon to a list called ```bayleef_weakness```

-----------------

**Let's walk through steps 1 and 2.**

You will code steps 3-5!

**Step 1:** Isolate Bayleef's weakness data from our dictionary


```python
bayleef_weakness_scores = data['Bayleef']['weakness']
```


```python
# __SOLUTION__
bayleef_weakness_scores = data['Bayleef']['weakness']
```

**Step 2:** Identify any type that has a weakness score of 2 and appending those types to a list called ```weakness_types```


We do this by:
1. Creating an empty list
2. Looping over the keys of our newly made dictionary```bayleef_weakness_score```.
    - Each key is a pokemon type
3. Checking if the score equals 2
4. Appending the key to our empty list if the score equals 2


```python
weakness_types = []

for weakness in bayleef_weakness_scores.keys():
    if bayleef_weakness_scores[weakness] == 2:
        weakness_types.append(weakness)
        
weakness_types
```


```python
# __SOLUTION__
weakness_types = []

for weakness in bayleef_weakness_scores.keys():
    if bayleef_weakness_scores[weakness] == 2:
        weakness_types.append(weakness)
        
weakness_types
```

Bayleef is weak to ice, poison, bug, fire, and flying pokemon. 


# Now your turn.

In the cell below, use the weakness_types list to identify pokemon that have one of those types, and append those pokemon to a list named ```bayleef_weakness```. 

>**Hint** The code will be very similar to the code for step 2.

>**Hint** Make sure your list doesn't contain duplicates of the same pokemon!


```python
# Your code here
```


```python
# __SOLUTION__
bayleef_weakness = set()
for key in data.keys():
    if data[key]['stats']['type1'] in weakness_types:
        bayleef_weakness.add(key)
    elif data[key]['stats']['type2'] in weakness_types:
        bayleef_weakness.add(key)
        
bayleef_weakness = list(bayleef_weakness)
```

Run the cell below to test your code! ⬇️


```python
from tests import ListCheck
test = ListCheck(bayleef_weakness)
test.run()
```


```python
# __SOLUTION__
from tests import ListCheck
test = ListCheck(bayleef_weakness)
test.run()
```
