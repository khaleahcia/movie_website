# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media # contains the Movie class that I'm using
import fresh_tomatoes # contains the HTML and CSS for the website

# Creating the instances of the Movie class
iron_man = media.Movie("Iron Man", "May 2008",
 "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG?download",
  "https://www.youtube.com/watch?v=8hYlB38asDY")

incredible_hulk = media.Movie("The Incredible Hulk", "June 2008",
 "https://upload.wikimedia.org/wikipedia/en/8/88/The_Incredible_Hulk_poster.jpg",
  "https://www.youtube.com/watch?v=FBSfUg-D7MI")

iron_man2 = media.Movie("Iron Man 2", "May 2010",
 "https://upload.wikimedia.org/wikipedia/en/e/ed/Iron_Man_2_poster.jpg",
  "https://www.youtube.com/watch?v=BoohRoVA9WQ")

thor = media.Movie("Thor", "May 2011",
 "https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",
  "https://www.youtube.com/watch?v=JOddp-nlNvQ")

captain_america_first_avenger = media.Movie("Captain America: The First Avenger", "July 2011",
 "https://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg",
  "https://www.youtube.com/watch?v=JerVrbLldXw")

avengers = media.Movie("Marvel's The Avengers", "May 2012",
 "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
  "https://www.youtube.com/watch?v=eOrNdBpGMv8")

iron_man3 = media.Movie("Iron Man 3", "May 2013",
 "https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg",
  "https://www.youtube.com/watch?v=f_h95mEd4TI&index=31&list=PLK5HARgNfgj9xRBC52Z7YRIXW2GCD99OT")

thor_dark_world = media.Movie("Thor: The Dark World", "November 2013",
 "https://upload.wikimedia.org/wikipedia/en/7/7e/Thor_-_The_Dark_World_poster.jpg",
  "https://www.youtube.com/watch?v=npvJ9FTgZbM")

captain_america_winter_soldier = media.Movie("Captain America: The Winter Soldier", "April 2014",
 "https://upload.wikimedia.org/wikipedia/en/e/e8/Captain_America_The_Winter_Soldier.jpg",
  "https://www.youtube.com/watch?v=tbayiPxkUMM")

guardians_of_the_galaxy = media.Movie("Guardians of the Galaxy", "August 2014",
 "https://upload.wikimedia.org/wikipedia/en/b/b5/Guardians_of_the_Galaxy_poster.jpg",
 "https://www.youtube.com/watch?v=d96cjJhvlMA&list=PLK5HARgNfgj9Nzu9sVTzFzn1aPMm7aGlu&index=76")

avengers_age_of_ultron = media.Movie("Avengers: Age of Ultron", "May 2015",
 "https://upload.wikimedia.org/wikipedia/en/f/ff/Avengers_Age_of_Ultron_poster.jpg",
  "https://www.youtube.com/watch?v=tmeOjFno6Do")

antman = media.Movie("Ant-Man", "July 2015",
 "https://upload.wikimedia.org/wikipedia/en/7/75/Ant-Man_poster.jpg",
  "https://www.youtube.com/watch?v=pWdKf3MneyI&list=PLK5HARgNfgj8P7WV6xvuVcZInRnqIy9Zd&index=56")

captain_america_civil_war = media.Movie("Captain America: Civil War", "May 2016",
 "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
  "https://www.youtube.com/watch?v=43NWzay3W4s&index=33&list=PLK5HARgNfgj-cuVJ8e3XrMRFtl-JE0uiQ")

doctor_strange = media.Movie("Doctor Strange", "November 2016",
 "https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg",
  "https://www.youtube.com/watch?v=HSzx-zryEgM&list=PLK5HARgNfgj9Io2PXblURA5_L5QD0zP3Z&index=33")

guardians_of_the_galaxy2 = media.Movie("Guardians of the Galaxy Vol. 2", "May 2017",
 "https://upload.wikimedia.org/wikipedia/en/a/ab/Guardians_of_the_Galaxy_Vol_2_poster.jpg",
  "https://www.youtube.com/watch?v=wUn05hdkhjM")

spiderman_homecoming = media.Movie("Spider-Man: Homecoming", "July 2017",
 "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",
  "https://www.youtube.com/watch?v=8wNgphPi5VM&list=PLK5HARgNfgj-h9eQ2KJRxanbw4QT9EsEs")

thor_ragnarok = media.Movie("Thor: Ragnarok", "November 2017",
 "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg",
  "https://www.youtube.com/watch?v=v7MGUNV8MxU&list=PLK5HARgNfgj8EwQcjz6yTvtPcA5fQowHc")

black_panther = media.Movie("Black Panther", "February 2018",
 "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
  "https://www.youtube.com/watch?v=xjDjIWPwcPU&list=PLK5HARgNfgj-ALIa2xPLXBzX8Vq9OoUU6")

avengers_infinity_war = media.Movie("Avengers: Infinity War", "April 2018",
 "https://upload.wikimedia.org/wikipedia/en/4/4d/Avengers_Infinity_War_poster.jpg",
  "https://www.youtube.com/watch?v=QwievZ1Tx-8&list=PLK5HARgNfgj-a_TYA7ZvQQldbI6m9tFMA")

# List of movies

movies = [iron_man, incredible_hulk, iron_man2, thor,
 captain_america_first_avenger, avengers, iron_man3, thor_dark_world,
  captain_america_winter_soldier, guardians_of_the_galaxy,
   avengers_age_of_ultron, antman, captain_america_civil_war, doctor_strange,
    guardians_of_the_galaxy2, spiderman_homecoming, thor_ragnarok,
     black_panther, avengers_infinity_war]

fresh_tomatoes.open_movies_page(movies)
