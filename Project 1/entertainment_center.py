import media
import fresh_tomatoes

thor_ragnarok = media.Movie("Thor: Ragnarok",
                        "Imprisoned, the mighty Thor finds himself"
                        "in a lethal gladiatorial contest against the Hulk,"
                        "his former ally. Thor must fight for survival"
                        "and race against time to prevent the all-powerful Hela"
                        "from destroying his home and the Asgardian civilization.",
                        "https://images-na.ssl-images-amazon.com/images/"
                        "M/MV5BMjMyNDkzMzI1OF5BMl5BanBnXkFtZTgwODcxODg5MjI@."
                        "_V1_SY1000_CR0,0,674,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=ue80QwXMRHg")

jigsaw = media.Movie("Jigsaw",
                     "Bodies are turning up around the city, each having met a uniquely gruesome"
                     " demise. As the investigation proceeds, evidence points to one suspect:"
                     " John Kramer, the man known as Jigsaw, who has been dead for ten years.",
                     "https://images-na.ssl-images-amazon.com/images/"
                     "M/MV5BNmRiZDM4ZmMtOTVjMi00YTNlLTkyNjMtMjI2OTAxNjgwMWM1XkEyXkFqcGdeQXVyMjMxOTE0ODA@."
                     "_V1_SY1000_CR0,0,648,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=vPP6aIw1vgY")
# print(avatar.storyline)
# avatar.show_trailer()

blade_runner = media.Movie("Blade Runner 2049",
                        "A young blade runner's discovery of a long-buried secret leads him"
                        "to track down former blade runner Rick Deckard,"
                        "who's been missing for thirty years.",
                        "https://images-na.ssl-images-amazon.com/images/"
                        "M/MV5BNzA1Njg4NzYxOV5BMl5BanBnXkFtZTgwODk5NjU3MzI@."
                        "_V1_SY1000_CR0,0,674,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=gCcx85zbxz4")

only_the_brave = media.Movie("Only the Brave",
                        "Based on the true story of the Granite Mountain Hotshots,"
                        "a group of elite firefighters risk everything"
                        "to protect a town from a historic wildfire.",
                        "https://images-na.ssl-images-amazon.com/images/"
                        "M/MV5BMTY5ODc5OTc2M15BMl5BanBnXkFtZTgwNjM0NjIzMzI@._V1_.jpg",
                        "https://www.youtube.com/watch?v=EE_GY6zccqc")

the_foreigner = media.Movie("The Foreigner",
                            "A humble businessman with a buried past seeks justice"
                            "when his daughter is killed in an act of terrorism."
                            "A cat-and-mouse conflict ensues with a government official,"
                            "whose past may hold clues to the killers' identities.",
                            "https://images-na.ssl-images-amazon.com/images/"
                            "M/MV5BM2RlMjcyMGQtZTU3OC00NGRlLWExMGEtYjU3ZjUyMDc0NWZmXkEyXkFqcGdeQXVyNTI4MzE4MDU@."
                            "_V1_SY1000_SX675_AL_.jpg",
                            "https://www.youtube.com/watch?v=33iuQu3UtjI")

it = media.Movie("Hunger Games",
                           "A group of bullied kids band together when a shapeshifting demon,"
                           " taking the appearance of a clown, begins hunting children.",
                           "https://images-na.ssl-images-amazon.com/images/"
                           "M/MV5BOTE0NWEyNDYtYWI5MC00MWY0LTg1NDctZjAwMjkyMWJiNzk1XkEyXkFqcGdeQXVyNjk5NDA3OTk@."
                           "_V1_SY1000_CR0,0,674,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=hAUTdjf9rko")
movies = [thor_ragnarok, jigsaw, blade_runner, only_the_brave, the_foreigner, it]
fresh_tomatoes.open_movies_page(movies)