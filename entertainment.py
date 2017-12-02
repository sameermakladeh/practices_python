import Movieclass
import fresh_tomatoes

toy_story = Movieclass.Movie("Toy story", "A story about a boi and his toys that come to life",
                             "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                             "https://www.youtube.com/watch?v=KYz2wyBy3kc")
# print (toy_story.story_line)

school_of_rock = Movieclass.Movie("School of Rock!", "best out there evar!",
                                  "http://www.imdb.com/title/tt0332379/mediaviewer/rm3808337152",
                                  "https://www.youtube.com/watch?v=vbF4qz_-PCM")

snakes_on_a_plan = Movieclass.Movie("Snakes on a plane",
                                    "Enough with the motherfucking snakes on the motherfucking plane",
                                    "http://www.imdb.com/title/tt0417148/mediaviewer/rm753208064",
                                    "https://www.youtube.com/watch?v=z4t6zNZ-b0A")
# school_of_rock.show_trailer()
snakes_on_a_plan.show_trailer()

#print (Movieclass.Movie.valid_ratings)

#m_movies = [toy_story, school_of_rock, snakes_on_a_plan]
#fresh_tomatoes.open_movies_page(m_movies)
