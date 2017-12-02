# Make a movie program!!!

import webbrowser
class Movie():
    valid_ratings = ["G","PG","PG-13","18+","R"]
    def __init__(self,title,story_line,poster_image_url,trailer_url):
        self.title = title
        self.story_line = story_line
        self.poster_image_url = poster_image_url
        self.trailer_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_url)

