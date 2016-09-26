import media
import fresh_tomatoes

# Create instances of the Movie class for your favorite movies
how_to_train_your_dragon = media.Movie("How to Train Your Dragon",
                                       "A young Viking who aspires to hunt "
                                       "dragons becomes the unlikely friend "
                                       "of a young dragon himself",
                                       "https://upload.wikimedia.org/wikipedia/en/9/99/How_to_Train_Your_Dragon_Poster.jpg",  # NOQA
                                       "https://www.youtube.com/watch?v=oKiYuIsPxYk")  # NOQA
kung_fu_panda = media.Movie("Kung Fu Panda",
                            "The Dragon Warrior mantle is bestowed upon an "
                            "obese panda who is a tyro in martial arts",
                            "https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=PXi3Mv6KMzY")
avengers = media.Movie("Avengers",
                       "A superhero film based on the Marvel Comics superhero "
                       "team of the same name",
                       "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")
life_is_beautiful = media.Movie("Life is Beautiful",
                                "An Italian book shop owner employs his "
                                "fertile imagination to shield his son from "
                                "the horrors of internment in a Nazi"
                                "concentration camp",
                                "https://upload.wikimedia.org/wikipedia/en/7/7c/Vitaebella.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=pAYEQP8gx3w")
silver_linings_pb = media.Movie("Silver Linings Playbook",
                                "After a stint in a mental institution, "
                                "a former teacher Pat Solitano moves back in "
                                "with his parents and tries to reconcile with his ex-wife",
                                "https://upload.wikimedia.org/wikipedia/en/9/9a/Silver_Linings_Playbook_Poster.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=Lj5_FhLaaQQ")
sound_of_music = media.Movie("Sound of Music",
                             "A musical drama that tells the story of a young "
                             "Austrian woman who takes a job as governess to "
                             "a large family",
                             "https://upload.wikimedia.org/wikipedia/en/c/c6/Sound_of_music.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=UY6uw3WpPzY")


# Group the movie instances in a list
list_Of_Movies = [how_to_train_your_dragon, kung_fu_panda, avengers,
                  life_is_beautiful, silver_linings_pb, sound_of_music]

# Pass the list of movies to 'open_movies_page' function in fresh_tomatoes.py
# This outputs an HTML web page displaying those movies
fresh_tomatoes.open_movies_page(list_Of_Movies)
