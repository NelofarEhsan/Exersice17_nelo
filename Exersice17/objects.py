
class Category:
    def _init_(self, id, name):
        self.id = id
        self.name = name

    def _repr_(self):
        return f"Category({self.id}, '{self.name}')"

class Movie:
    def _init_(self, id, name, year, minutes, category_id):
        self.id = id
        self.name = name
        self.year = year
        self.minutes = minutes
        self.category_id = category_id

    def _repr_(self):
        return f"Movie({self.id}, '{self.name}', {self.year}, {self.minutes}, {self.category_id})"