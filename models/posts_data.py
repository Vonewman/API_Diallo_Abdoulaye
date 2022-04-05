class Post:
    def __init__(self, userId='', id='', title='', body=''):
        self.userId = userId
        self.id     = id
        self.title  = title
        self.body   = body


    @classmethod
    def select(cls):
        return "SELECT * FROM posts"
        # the cursor.execute(select_command) done in the controller



    def insert(self):
        insert_command = f"""
                INSERT INTO posts (userId, id, title, body)
                VALUES ('{self.userId}', '{self.id}', '{self.title}', '{self.body}')
        """
        return insert_command
