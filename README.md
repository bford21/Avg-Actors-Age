# XamarinCodingAssignment

To run this Python script, first have Python 2 installed on the machine you are trying to run it on. Next open a terminal window and navigate to the directory in which the file is stored. You can then launch the script by typeing "python codingAssignment.py". 

Design: 
In order to get the data needed for this project I used a public API provided by www.myapifilms.com. The API made it easy to construct queries and get the names of current movies in theaters as well as the cast and their birthdays. The information was returned in XML format which also made it easy to parse through. Although the API did not return the specific age of the actors, I designed a function that took their birthdays and calculated their age based on the current date.

I had originally started to program the project in PHP but ran into trouble with my free webhost reseting the connection to the server due to the queries taking to long. I decided to use Python instead, despite not having any previous knowledge of the language. I found Python very easy to pick up and I really enjoyed working with it. 

Design Questions: 
If the data size got to much larger I would definitely explore other options for obtaining the data. The API I used certainly wasnt the fastest and it's for that same reason that if the query changed and obtained more data, it would have a negative impact on performance.

As long as the API stays up to date and returns valid data the program is designed in such a way that it will continue working as it should. Over time, if changes are made to the API that change the tags within the XML document it returns then changes will have to be made in the program in order to accomdate the new XML tags. 

Conclusion: I had a lot of fun on this project and learned quite a few things. I really enjoyed learning Python, so much so I'm currently fooling around with the Python Library called Plotly that would enable me to graphically display data such as the average cast age!
