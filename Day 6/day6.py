''' This program writes to a file programatically using a list in Python'''

# Import the library to be used
import random

# Create a list of syllables to be used
syllables = [
    'mon','fay','shi','zag','blarg','rash','izen','diz','kiz','zay','zod','zak','zaz','zi'
]


# Create a function to generate a name
def generate_name(used_names):
    name = random.choice(syllables) + random.choice(syllables) + random.choice(syllables)
    capitalized_name = name.capitalize()
    if name in used_names:
        return generate_name(used_names)
    used_names.add(capitalized_name)
    return capitalized_name

# Ask the user how many names they would like to generate
number_of_names = int(input('How many names would you like to generate? '))

# Generate the names        
used_names = set()
character_names = [generate_name(used_names) for _ in range(number_of_names)]

# Print the names to the console
with open('character_names.txt', 'w') as f:
        for names in character_names:
            f.write(names + '\n')

print('Names written to file')