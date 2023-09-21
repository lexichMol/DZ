import requests
from bs4 import BeautifulSoup
import pprint
pp = pprint.PrettyPrinter(indent=4)

headers ={
  "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

list_genre = ["novinki", "komedii", "boeviki", "fantastiku", "semeynye", "trillery", "priklyucheniya",
              "dramy", "mistika", "detektivy", "melodramy", "fentezi"]

film_genre = 1
dic_films = {}

def find_films(film_genre="",film_rating=0, film_time_min=0, film_time_max=300, film_year=1900, film_countries="", film_roles = "", film_director=""):
    film_countries = film_countries.lower()
    film_roles = film_roles.lower()
    film_director = film_director.lower()

    url = "https://utorrentfilmi.fun/"
    url = url + film_genre + "/"

    req = requests.get(url, headers=headers)
    soop = BeautifulSoup(req.text, "lxml")

    all_film = soop.find_all("div", class_="short")
    for film in all_film:
        all = film.find_all("div", class_="string")

        countries = all[0].text.replace("Страна: ", "").lower()
        director = all[1].text.replace("Режиссер: ", "").lower()
        roles = all[4].text.replace("В ролях: ", "").lower()
        time = int(all[5].text.split()[1])
        rating = int(film.find("li", class_="current-rating").text)/20
        name_film = film.find("div", class_="title")

        img = film.find("div", class_="preview").find("img").get("src")
        year = int(name_film.text.split("(")[1].replace(")", ""))
        if film_countries in countries and film_director in director and film_roles in roles and film_time_min <= time and film_time_max >= time and film_rating<=rating and film_year<=year:
            dic_films[name_film.text] = {"img": img, "rating": rating,
                                    "year": year, "country": countries, "time": time,
                                    "roles": roles, "director": director}
    pp.pprint(dic_films)
find_films(film_genre="komedii")

