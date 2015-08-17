# Brian Ford
# Xamarin Coding Assignment
# Lists current movies in theaters and displays avg age of cast

import urllib, time, string
from datetime import date
from xml.etree import ElementTree as ET

#function that calculates age based off dob passed in params
def findAge(dob):
  today = date.today()
  
  #Filters string of all known ASCII characters and replaces with ' '
  dob = ''.join([i if ord(i) < 128 else ' ' for i in dob])
  
  #determines if dob contains full birthday or just year
  if ' ' in dob:
    #Parses the string representing the dob into a workable date format dd/MONTH/YEAR
    born = time.strptime(dob, "%d %B %Y")
    return today.year - born.tm_year - ((today.month, today.day) < (born.tm_mon, born.tm_mday))
  else:
    #filters string of any non digits
    dob = filter(lambda x: x.isdigit(), dob)
    born = time.strptime(dob, "%Y")
    return today.year - born.tm_year

#Array declarations
idIMDB = []
titles = []
ages = []

#Queries myapifilms for movies in theaters and returns result in XML format
movieRequest = 'http://www.myapifilms.com/imdb/inTheaters?format=XML&lang=en-us'
root = ET.parse(urllib.urlopen(movieRequest)).getroot()
movies = root.findall('movies[0]/movie')

#Iterates through all movies in theaters and prints title
print 'MOVIES IN THEATERS'
for item in movies:
  movieID = item.find('idIMDB').text
  idIMDB.append(movieID)
  title = item.find('title').text.encode('utf-8')
  titles.append(title)
  print title

#Variable used to keep track of current movie 
x = 0

#Iterates though all movies based on IMDB ID
for i in idIMDB:
  print '\nMOVIE: ' + titles[x]
  x += 1
  
  #Queries myapifilms for actors based on movie ID and returns results in XML format
  actorRequest = 'http://www.myapifilms.com/imdb?idIMDB='+i+'&format=XML&aka=0&business=0&seasons=0&seasonYear=0&technical=0&lang=en-us&actors=S&biography=1&trailer=0&uniqueName=0&filmography=0&bornDied=1&starSign=0&actorActress=0&actorTrivia=0&movieTrivia=0&awards=0&moviePhotos=N&movieVideos=N&similarMovies=0'  
  root = ET.parse(urllib.urlopen(actorRequest)).getroot()
  actors = root.findall('actors/actor')
  
  #Lists all actors and their age
  for item in actors:
    dob = item.find('biography/dateOfBirth')
    if dob is not None:
      bday = dob.text.encode('utf-8')
      age = findAge(bday)
      ages.append(age)
      print item.find('actorName').text.encode('utf-8'), str(age)
  
  total = 0
  for i in ages:
    total += i
  
  print 'AVERAGE AGE: ', str(total/len(ages))
  ages = []
  

  
