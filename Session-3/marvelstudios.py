"""Question description
Marvel Studios is known for the production of the Marvel Cinematic Universe films, based on characters that appear in Marvel Comics publications. Marvel counts among its characters such well-known superheroes as Spider-Man, Iron Man, Captain America, the Hulk, Thor, Wolverine, Ant-Man, the Wasp, Black Widow, Captain Marvel, Black Panther, Squirrel Girl, Doctor Strange, the Scarlet Witch, She-Hulk, the Vision, Psylocke, Tigra, Ghost-Spider, the Falcon, the Winter Soldier, Ghost Rider, Quake, Blade, Daredevil, Ms. Marvel, the Punisher and Deadpool. Superhero teams exist such as the Avengers, the X-Men, the Fantastic Four and the Guardians of the Galaxy as well as supervillains including Doctor Doom, Magneto, Thanos, Loki, Green Goblin, Kingpin, Diamondback, Red Skull, Ultron, the Mandarin, MODOK, Doctor Octopus, Kang, Dormammu, Venom and Galactus. Marvel decided to create a new story. Can you suggest them that the character names which will be present in that film to make a film as block buster?
Constraints
Input Format: First line represents number of names involved. Second line onwards the character names.
Output Format: Display the character names in alphabetical order.
"""
# Read the number of names
n = int(input())

# Read the character names
names = []
for i in range(n):
    names.append(input())

# Sort the names in alphabetical order
names.sort()

# Display the sorted names
for name in names:
    print(name)