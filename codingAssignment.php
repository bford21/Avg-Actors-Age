<?php
/*
Brian Ford
Xamarin Coding Assignment
This program lists the movies currently out in theaters and the average age of the cast.
*/

// Queries myapifilms for movies currently in theaters
$requestURL = "http://www.myapifilms.com/imdb/inTheaters?format=XML&lang=en-us";
$xml = simplexml_load_string(file_get_contents($requestURL)) or die("Error: Cannot create object");
	
echo "<h2>Movies in Theaters</h2>";
$totalMovies = count($xml->movies[1]);

//Prints the list of movies currently in theaters
for ($x = 0; $x <= $totalMovies; $x++) {
	echo $xml->movies[1]->movie[$x]->title;
	echo "<br>";
}
?>