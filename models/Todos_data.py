class Todo:
    def __init__(self, userId='', id='', title='', completed=''):
        self.userId    = userId
        self.id        = id
        self.title     = title
        self.completed = int(completed)


    @classmethod
    def select(cls):
        return "SELECT * FROM todos"


    def insert(self):
        insert_command = f"INSERT INTO todos (userId, id, title, completed) VALUES ('{self.userId}', '{self.id}', '{self.title}', '{self.completed}')"
        return insert_command
