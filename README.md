
<center> <h1>Pokemon/Dictionary Warmup</h1> </center>

![Pokeball](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSvFguv_4hYhwny0d7KdBcFYHYCZ0j2uEBtr3aYmJHqNKecqEsi&usqp=CAU)

Joél is currently playing the Pokemon Crystal video game. 

Joél takes pokemon very seriously so they have downloaded [The Complete Pokemon Dataset](https://www.kaggle.com/rounakbanik/pokemon) from Kaggle and needs some help organizing the data.

Let's use our dictionary parsing skills to help Joél out!

**In the cell below,** we import the Pokemon Dataset.

*Don't worry about this code for now. It will make sense later on*

For now, just run the cell :)


```python
import json

with open('./data/pokemon.json', 'r') as fp:
    data = json.load(fp)
```


```python
#__SOLUTION__

import json

with open('./data/pokemon.json', 'r') as fp:
    data = json.load(fp)
```

Joél has caught the following pokemon.
- Bayleef 
- Haunter
- Poliwag
- Pidgeotto
- Kadabra

In the cell below, we create a list called ```joels_pokemon_names``` containing each of his pokemon's names.


```python
joels_pokemon_names = ['Bayleef', 'Haunter', 'Poliwag', 'Pidgeotto', 'Kadabra']
```


```python
# __SOLUTION__

joels_pokemon_names = ['Bayleef', 'Haunter', 'Poliwag', 'Pidgeotto', 'Kadabra']
```

## Coding time:

Let's create a new dictionary called ```my_pokemon```. 

To do this, we will
- Create an empty dictionary called ```my_pokemon```
- loop over the names in the ```joels_pokemon_names``` list
- Use the name to access the pokemon's data in the ```data``` dictionary
- Add the pokemon name to the ```my_pokemon``` dictionary as a ```key``` and the pokemon's data as the key's ```value```


```python
# YOUR CODE HERE
joels_pokemon = {}

```


```python
# __SOLUTION__

joels_pokemon = {}

for pokemon in joels_pokemon_names:
    joels_pokemon[pokemon] = data[pokemon]
```

Run the cell below to see if you successfully made the joels_pokemon dictionary!


```python
from tests import CheckDictionary

test = CheckDictionary(joels_pokemon)
test.run()
```


```python
#__SOLUTION__

from tests import CheckDictionary

test = CheckDictionary(joels_pokemon)
test.run()
```

![](https://gamepress.gg/pokemonmasters/sites/pokemonmasters/files/styles/300h/public/2019-08/pm0153_00_bayleaf_256.ktx.png?itok=Tr7OMsm1)

**Bayleef** is Joél's strongest pokemon. Let's create a list of all Pokemon that Bayleef is weak against.

*Weakness* is measured with the ```weakness``` key in our data. If the weakness value = 2, that means the pokemon is extremely weak to that type of pokemon. 

To find all pokemon that Bayleef is weak to, we have to:
1. Isolate Bayleef's weakness data from our dictionary
2. Identify any type that has a weakness score of 2 and appending those types to a list called ```weakness_types```
3. Loop over our entire dataset
4. Identify pokemon who have a type that match the types in our ```weakness_types``` list.
> **Hint** The type value for each pokemon can be found in using the ```stats``` key
5. Append the names of those pokemon to a list called ```bayleef_weakness```

-----------------

Let's walk through steps 1 and 2.

We'll have you code steps 3-5!

**Step 1:** Isolate Bayleef's weakness data from our dictionary


```python
bayleef_weakness_scores = data['Bayleef']['weakness']
```


```python
#__SOLUTION__

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
#__SOLUTION__

weakness_types = []

for weakness in bayleef_weakness_scores.keys():
    if bayleef_weakness_scores[weakness] == 2:
        weakness_types.append(weakness)
        
weakness_types
```

Bayleef is weak to ice, poison, bug, fire, and flying pokemon. 


**Now your turn.** In the cell below, use the weakness_types list to identify pokemon that have one of those types.

>**Hint** The code will be very similar to the code for step 2.


```python
# Your Code Here
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
#__SOLUTION__

from tests import ListCheck
test = ListCheck(bayleef_weakness)
test.run()
```
