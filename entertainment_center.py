import media
import fresh_tomatoes

# Creating instances of movies.
batman_vs_superman = media.Movie("Batman vs Superman",
                                 "https://upload.wikimedia.org/wikipedia/en/2/20/Batman_v_Superman_poster.jpg",
                                 "https://www.youtube.com/watch?v=NhWg7AQLI_8",
                                 "Action, Adventure, Fantasy"
                                 )
deadpool = media.Movie("Deadpool",
                       "https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                       "https://www.youtube.com/watch?v=ZIM1HydF9UA",
                       "Action, Adventure, Comedy")
captain_america = media.Movie("Captain America",
                              "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",
                              "https://www.youtube.com/watch?v=dKrVegVI0Us",
                              "Action, Sci-Fi, Thriller")

the_secret_life_of_pets = media.Movie("The Secret Life of Pets",
                                      "https://upload.wikimedia.org/wikipedia/en/6/64/The_Secret_Life_of_Pets_poster.jpg",  # NOQA
                                      "https://www.youtube.com/watch?v=UZJVc_JTI_w",
                                      "Animation, Comedy, Family")

zootopia = media.Movie("Zootopia",
                       "https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM",
                       "Animation, Comedy, Family")
# Saving movies in a list
movies_list = [batman_vs_superman, deadpool, captain_america, the_secret_life_of_pets, zootopia]

# running the application passing the movie list to the function
fresh_tomatoes.open_movies_page(movies_list)
