# 13_cinemas
Scripts parses movies` shedule from afisha and then parse kinopoisk for getting ratings and votes. In default, script outputs table with 10 movies info which are title, amount of cinemas movie is shown now, rating and votes. Outputted movies are sorted by kinopoisk-rating descent order.

##launching
`git clone <repository url>`
`pip install requirements.txt 
python cinemas.py [--movies MOVIES] [--art] [--sorting, -s rating]`

`--art` - adding this arguement to response will include movies shown in less than 10 cinemas. Suggested that arthouse movies are shown in small amount of cinemas.  

`--movies` - movies amount for outputting in the console, default is 10.  

`--sort`, `-s` - movies can be sorted can be sorted by rating, cinemas count, title or votes. Just use the same name argument value.  For example: `-s title` or `-sort votes`. Default sort is by rating.