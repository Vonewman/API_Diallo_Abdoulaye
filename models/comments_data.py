class Comment:
    def __init__(self, postId='', id='', name='', email='', body=''):
        self.postId = postId
        self.id     = id
        self.name   = name
        self.email  = email
        self.body   = body


    @classmethod
    def select(cls):
        return "SELECT * FROM comments"


    def insert(self):
        insert_command = f"""
                INSERT INTO comments (postId, id, name, email, body)
                VALUES ('{self.postId}', '{self.id}', '{self.name}', '{self.email}', '{self.body}')
        """
        return insert_command
