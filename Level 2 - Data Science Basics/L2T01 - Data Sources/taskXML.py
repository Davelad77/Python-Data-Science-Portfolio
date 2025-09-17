# write a python program to read in the XML file 'movie.xml'
# list all the child tags of the movie element using iter()
# print out the movie descriptions using itertext()
# find the number of movies that are favourites and the number that are not

# parse in the movie.xml file
import xml.etree.ElementTree as ET
tree = ET.parse('movie.xml')
root = tree.getroot()

# iterate through the movie elements and print each child tag
for movie in root.iter('movie'):
    print(movie.tag, movie.attrib)

print()

# print the title of each movie followed by the description
for movie in root.iter('movie'):
    print(f"Description of movie {movie.attrib.get('title')}:")     # for each movie element retrieve the title attribute and insert into the text
    movie_description = movie.find('description')       # create a varialbe and write in the text from the description child
    print(movie_description.text)
    print()

# find the number of movies that are favourites and the number that are not
favourite_movies = 0        # create a variable to store the number of favourite movies
not_favourite_movies = 0        # create a variable to store the number of not favourite movies
for movie in root.iter('movie'):    # iterate through the movie elements
    if movie.attrib.get('favorite') == 'True':   # if the favourite attribute is True
        favourite_movies += 1       # increment the favourite_movies variable by 1
    else:
        not_favourite_movies += 1       # otherwise increment the not_favourite_movies variable by 1

print(f"Number of favourite movies: {favourite_movies}")
print(f"Number of not favourite movies: {not_favourite_movies}")