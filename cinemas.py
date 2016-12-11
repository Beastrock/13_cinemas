import requests
import argparse
from bs4 import BeautifulSoup
from time import sleep


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--art', action='store_true',
                        help='includes movies shown in less than ten cinemas')
    parser.add_argument('--movies', action='store', default=10,
                        help='amount for console outputting, default = 10', type=int)
    return parser.parse_args()


def fetch_afisha_page():
    return requests.get('http://www.afisha.ru/msk/schedule_cinema/').text


def parse_afisha_list(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    schedule = soup.find('div', id='schedule')
    titles = [tags.text for tags in schedule.find_all('h3', class_='usetags')]
    cinemas = [len(item.find_all('tr')) for item in schedule.find_all('tbody')]
    return [{'title': title, 'cinemas': cinemas}
            for title, cinemas in zip(titles, cinemas)]


def fetch_movies_info(movies, including_art_house):
    kinopoisk_search_url = 'http://kinopoisk.ru/index.php?first=yes&kp_query=%s'
    ten_cinemas = 10
    timeout_seconds = 2
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'UTF-8',
        'Accept-Language': 'en-US,en;q=0.8,ru;q=0.6',
        'Content-Type': 'text/html;charset=UTF-8',
        'User-Agent': 'Agent:Mozilla/5.0 (Windows NT 6.1; WOW64))'
    }
    if not including_art_house:
        movies = [movie for movie in movies if movie['cinemas'] > ten_cinemas]
    for movie in movies:
        film_url = kinopoisk_search_url % movie['title']
        sleep(timeout_seconds)
        film_html = requests.session().get(film_url, headers=headers).text
        soup = BeautifulSoup(film_html, 'html.parser')
        try:
            movie['rating'] = float(soup.find('span', 'rating_ball').text)
            movie['votes'] = soup.find('span', 'ratingCount').text
        except AttributeError:
            movie['rating'] = .0
            movie['votes'] = "0"
    return sorted(movies, key=lambda movie: movie['rating'], reverse=True)


def output_movies_to_console(movies_info, amount_to_print):
    print('{:^50}'.format('HIGH-RATED MOVIES IN MOSCOW CINEMAS:'))
    print('{:>2}|{:^7}|{:^9}|{:^6}|{:^20}'.format(
        'N', 'CINEMAS', 'VOTES', 'RATING', 'TITLE'))
    for number, movie in enumerate(movies_info[:amount_to_print], start=1):
        print('{:>2}|{m[cinemas]:^7}|{m[votes]:^9}|'
              '{m[rating]:^6}| {m[title]}'.format(number, m=movie))


if __name__ == '__main__':
    args = get_args()
    movies = parse_afisha_list(fetch_afisha_page())
    print('got titles and cinemas. fetching their kinopoisk rating...')
    movies_info = fetch_movies_info(movies, args.art)
    output_movies_to_console(movies_info, args.movies)