class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def get_name(self):
        return self.__name

    def get_biography(self):
        return self.__biography

    def __str__(self):
        return f"Name: {self.__name}, Biography: {self.__biography}"
    
    def save_to_db(self, cursor):
        query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"
        values = (self.name, self.biography)
        cursor.execute(query, values)