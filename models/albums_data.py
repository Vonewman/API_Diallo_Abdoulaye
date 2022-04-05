class Album:
    def __init__(self, userId='', id='', title=''):
        self.userId    = userId
        self.id        = id
        self.title     = title


    @classmethod
    def select(cls):
        return "SELECT * FROM albums"



    def insert(self):
        insert_command = f"INSERT INTO albums (userId, id, title) VALUES ('{self.userId}', '{self.id}', '{self.title}')"
        return insert_command
