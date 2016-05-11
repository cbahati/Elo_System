## Elo_System 

Elo_System is a website for the Loyola University Chicago FIFA Club to keep track of the members standings within our 
competitive EA Games FIFA Soccer league. it uses the ELO algorithm to award points, and a matchmaking system to match players
of similar skills together.

## Screenshots

<img src="http://i.imgur.com/H5InHaU.png?1" height="400px">
<img src= "http://i.imgur.com/nXYTdwc.png?1" height="400px">

## Requirements:

 - Python 2.7
 - Django 1.8.2

## Installation

git clone git://github.com/cbahati/Elo_System.git

## Getting Started

-To run the development server just type
 - "python manage.py runserver" 
 - you may need to reset the database and remove all migrations to start fresh
The ELO algorithm module is located within the "clubs" directory

## TODO
- This project is still a work in progress, most of the changes needed are to the aesthetic of the site HTML, CSS, etc..
- Get the team banner model and directory set up properly
- Fix slight Bug when 2 teams are tied which substract the wrong amount of point from the team with highest ELO

 
