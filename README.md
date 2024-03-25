## Project "Parsing Wikipedia: wiki-death dataset"
Algorithm to build a database (in json) with the Wikipedia's API for all the famous deaths from 1992 to 2022.

The database will contain:
- Death date
- Name and surname of the deceased
- Age of the deceased

### [*Wiki_deaths*](Wiki_deaths.py) contains the main part of the project: 
- the Wikipedia's API to get the data
- the *check existence* function to control if the page exists or not
- the parsing *page* and *line* functions to get days/months/years, name and other data for every person
- the build of the database (json file) called: *Death_File.json*



### [*Query_Wiki_deaths*](Query_Wiki_deaths.py) contains:
- an algorithm to read the database (json file)
- a nested for loop to create a graph with deaths per year with the use of the *matplotlib* library
