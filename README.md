# Houhou Discord Bot
If you would like to test out the bot you can join the discord server by clicking this [link]! 

This Discord bot connects to many different APIs and can be added to a Discord server to allow users to get the functionality of the APIs without leaving Discord!

## APIs
APIs currently in use by the bot:
* [Alpha Vantage]
* [icanhazdadjoke]
* [NASA APOD]
* [NASA Image and Video Library]
* [NASA Mars Rover Photos]
* [OMBd]
* [RoboHash]

## Commands
__<ins>CAT COMMANDS</ins>__ \
!cat
 * Sends a random cat GIF
 
!cat upvote
 *  Upvotes the last cat GIF

!cat downvote
 *  Upvotes the last cat GIF
 
__<ins>DOG COMMANDS</ins>__ \
!dog
 * Sends a random dog GIF

!dog upvote
 * Upvotes the last dog GIF

!dog downvote
 * Upvotes the last dog GIF
 
__<ins>IMBD COMMANDS</ins>__ \
!imbd TITLE
 * Searches IMBd for information on the movie/series based on the title
 * `Ex. !imbd Life of Pi`

!imbd search TITLE
 * Searches IMBd for movies/series based on the title
 * `Ex. !imbd search Prisoners`
 
__<ins>JOKE COMMANDS</ins>__ \
!joke
 * Sends a random dad joke

!joke SEARCHTERM
 * Sends a random dad joke based on the search term
 * `Ex. !joke Teacher`
 
__<ins>NASA APOD COMMANDS</ins>__ \
!nasa apod
 * Sends the NASA Astronomy Picture of the Day

!nasa apod DATE
 * Sends the NASA Astronomy Picture of the Day for the given date\
 * `Ex. !nasa apod 2020-1-1`
 
__<ins>NASA ROVER COMMANDS</ins>__ \
!nasa rover
 * Send a random image from NASA's Mars Curiosity Rover

!nasa rover DATE
 * Send a random image from NASA's Mars Curiosity Rover for the given date
 * `Ex. !nasa rover 2020-1-1`
 
__<ins>NASA SEARCH COMMANDS</ins>__ \
!nasa search
 * Sends a random image from NASA's image library

!nasa search SEARCHTERM
 * Sends an image from NASA's image library based on the search term
 * `Ex. !nasa search Uranus`
 
__<ins>ROBOT COMMANDS</ins>__ \
!robot SET(optional) BACKGROUND(optional)
 * Sends a random robot image
 * `Ex. !robot set1 background1`

!robot TERM SET(optional) BACKGROUND(optional)
 * Sends a robot image based on the search term
 * `Ex. !robot My name is Alex! set4 background2`

<ins>SET can either be set1, set2, set3, set4, or set5</ins>
<ins>BACKGROUND can either be background1 or background2</ins>
 
__<ins>STOCK COMMANDS</ins>__ \
!stock STOCKTICKER
 * Sends a stock chart based on the stock ticker
 * `Ex. !stock MSFT`

!stock search SEARCHTERM
 * Searches for stocks based on the search term
 * `Ex. !stock search Amazon`

```sh
pip install Flask
```

```sh
pip install Flask-WTF
```



## Usage
To run the project through Command Prompt you have to CD into the folder and then run app.py.

```sh
cd C:\Users\Alex\Downloads\Food-Database-Project-main
```

```sh
python app.py
```

Open [localhost:5000](http://localhost:5000/).



## Authors
Trish Beeksma - [GitHub](https://github.com/TrishRB)\
Alex Mello - [GitHub](https://github.com/Alex-E-Mello)\
Matthew Siebold - [GitHub](https://github.com/DorkCube)



## License
MIT







[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [link]: <https://discord.gg/JYxbQKkB>
   
   [Alpha Vantage]: <https://www.alphavantage.co/documentation/>
   [icanhazdadjoke]: <https://icanhazdadjoke.com/api>
   [NASA APOD]: <https://api.nasa.gov/>
   [NASA Image and Video Library]: <https://images.nasa.gov/docs/images.nasa.gov_api_docs.pdf>
   [NASA Mars Rover Photos]: <https://github.com/chrisccerami/mars-photo-api>
   [OMBd]: <http://www.omdbapi.com/>
   [RoboHash]: <https://github.com/e1ven/Robohash>
