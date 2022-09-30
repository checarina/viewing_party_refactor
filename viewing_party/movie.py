class Movie:
    def __init__(self, title, genre, rating, host, audience):
        self.title = title
        self.genre = genre
        self.rating = rating
        self.host = host
        self.audience = audience

    def update_rating(self, new_rating):
        self.rating = new_rating