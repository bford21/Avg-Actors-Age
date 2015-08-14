# Brian Ford
# Xamarin Coding Assignment
# Lists current movies in theaters and displays avg age of cast

import urllib
from xml.etree import ElementTree as ET

#Queries myapifilms for movies in theaters and returns result in XML format
movieRequest = 'http://www.myapifilms.com/imdb/inTheaters?format=XML&lang=en-us'
root = ET.parse(urllib.urlopen(movieRequest)).getroot()
movies = root.findall('movies/movie')

#Array to hold movie ID's for easy look up
idIMDB = []

#Iterates through all movies in theaters and prints title
print 'Movies in theaters'
for item in movies:
  print item.find('title').text
  movieID = item.find('idIMDB').text
  idIMDB.append(movieID)
  print movieID

#Queries myapifilms for actors based on movie ID passed to it and returns in XML format
actorRequest = 'http://www.myapifilms.com/imdb?idIMDB=tt1798684&format=XML&aka=0&business=0&seasons=0&seasonYear=0&technical=0&lang=en-us&actors=S&biography=1&trailer=0&uniqueName=0&filmography=0&bornDied=1&starSign=0&actorActress=0&actorTrivia=0&movieTrivia=0&awards=0&moviePhotos=N&movieVideos=N&similarMovies=0'
root = ET.parse(urllib.urlopen(actorRequest)).getroot()
actors = root.findall('actors/actor')

#Lists all actors
for item in actors:
  print item.find('actorName').text
  print item.find('biography/dateOfBirth').text
  