class Photo:
    def __init__(self, albumId, id, title, url, thumbnailUrl):
        self.albumId      = albumId
        self.id           = id
        self.title        = title
        self.url          = url
        self.thumbnailUrl = thumbnailUrl


    @classmethod
    def select(cls):
        return "SELECT * FROM photos"


    def insert(self):
        insert_command = f"""
                INSERT INTO photos (albumId, id, title, url, thumbnailUrl)
                VALUES ('{self.albumId}', '{self.id}', '{self.title}', '{self.url}', '{self.thumbnailUrl}')
        """
        return insert_command
