'''list comprehensions'''

artists = [("Ella", "Fitzgerald"), ("Rakim", ""), ("John", "Bon Jovi"), ("Dave", "Matthews")]
pythonated_artists = []
for artist in artists:
    pythonated = artist.lower().replace(" ", "_")
    pythonated_artists.append(pythonated)
# the line below is equivalent to lines 4-7
pythonated_artists = [artist.lower().replace(" ", "_") for artist in artists]
print(pythonated_artists)

last_names = [f"{artist[0]}, {artist[1].upper()}" for artist in artists]
print(last_names)


numbers = [1.234657, 5.9038, 3.098367854]
rounded_numbers = [int(round(number)) for number in numbers]
print(rounded_numbers)