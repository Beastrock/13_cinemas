# 13_cinemas
Scripts parses movies\` shedule from [afisha](http://www.afisha.ru/msk/schedule_cinema/) and then parse [kinopoisk](http://kinopoisk.ru) for getting ratings and votes. In default, script outputs information table for 10 movies which consists of title, amount of cinemas movie is shown now, rating and votes. Outputted movies are sorted by kinopoisk-rating descent order.

##launching
`git clone <repository url>`  
`pip install requirements.txt`  
`python cinemas.py [--movies MOVIES] [--art] [--sorting, -s rating]`  

`--art` - adding this arguement to response will include movies shown in less than 10 cinemas. Suggested that arthouse movies are shown in small amount of cinemas.  

`--movies` - movies amount for outputting in the console, default is 10.  

`--sort`, `-s` - key parameter for sorting movies. They can be sorted by rating, cinemas, title or votes. Just use the same name argument value.  For example: `-s title` or `-sort votes`. Default sort is by rating.