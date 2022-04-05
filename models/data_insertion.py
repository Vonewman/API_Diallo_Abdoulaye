from User_data import User
from User_data import Address
from User_data import Company
from Todos_data import Todo
from posts_data import Post
from comments_data import Comment
from albums_data import Album
from photos_data import Photo
from json import dumps
import mysql.connector
import requests


class Model:
  
    api_url    = 'https://jsonplaceholder.typicode.com/'

    @classmethod
    def database_initializer(cls):
        cls.mydb = mysql.connector.connect(
            host='localhost',
            database='projet_api',
            user='root',
            password='root'
        )
        cls.mycursor = cls.mydb.cursor()

        return cls.mycursor

    @classmethod
    def close_db(cls):
        cls.mydb.commit()
        cls.mydb.close()

    @classmethod
    def retrieve_albums(cls):
        cls.retrieve_from(Album)

    @classmethod
    def retrieve_photos(cls):
        cls.retrieve_from(Photo)


    @classmethod
    def retrieve_posts(cls):
        cls.retrieve_from(Post)



    @classmethod
    def retrieve_comments(cls):
        cls.retrieve_from(Comment)


    # this insert the User_data data in the database
    @classmethod
    def insert_data_in_User(cls):
        mycursor = cls.database_initializer()
        json_obj = requests.get(cls.api_url + 'users').json()
        for user in json_obj:
            id        = user.get('id')
            name      = user.get('name')
            username  = user.get('username')
            email     = user.get('email')
            phone     = user.get('phone')
            website   = user.get('website')

            #  hanling the address
            address = user.get('address')
            street  = address.get('street')
            suite   = address.get('suite')
            city    = address.get('city')
            zipcode = address.get('zipcode')
            geo     = dumps(address.get('geo'))

            # create an Address object
            address_instance = Address(street, suite, city, zipcode, geo)
            mycursor.execute(address_instance.insert())

            # retrieve address identificator
            addressId = f"SELECT id FROM address WHERE suite = '{suite}'"
            mycursor.execute(addressId)
            addressId = mycursor.fetchone()[0]

            # handling the company
            company      = user.get('company')
            company_name = company.get('name')
            catchPhrase  = company.get('catchPhrase')
            bs           = company.get('bs')
            company_instance = Company(company_name, catchPhrase, bs)
            mycursor.execute(company_instance.insert())

            # retrieve company identificator
            companyId = f"SELECT id FROM company WHERE name = '{company_name}'"
            mycursor.execute(companyId)
            companyId = mycursor.fetchone()[0]

            # create user object
            user_instance = User(id, name, username, email, addressId, phone, website, companyId)
            mycursor.execute(user_instance.insert())
        cls.close_db()




    @classmethod
    def insert_data_in_Todos(cls):
        mycursor = cls.database_initializer()
        json_obj = requests.get(cls.api_url + 'todos').json()
        for todo in json_obj:
            userId      = todo.get('userId')
            id          = todo.get('id')
            title       = todo.get('title')
            completed   = todo.get('completed')

            # create a todo object
            todo_instance = Todo(userId, id, title, completed)
            mycursor.execute(todo_instance.insert())
        cls.close_db()
        

    @classmethod
    def insert_data_in_posts(cls):
        mycursor = cls.database_initializer()
        json_obj = requests.get(cls.api_url + 'posts').json()
        for post in json_obj:
            userId  = post.get('userId')
            id      = post.get('id')
            title   = post.get('title')
            body    = post.get('body')

            # create a post object
            post_instance = Post(userId, id, title, body)
            mycursor.execute(post_instance.insert())
        cls.close_db()



    @classmethod
    def insert_data_in_comments(cls):
        mycursor = cls.database_initializer()
        json_obj   = requests.get(cls.api_url + 'comments').json()
        for comment in json_obj:
            postId    = comment.get('postId')
            id        = comment.get('id')
            name      = comment.get('name')
            email     = comment.get('email')
            body      = comment.get('body')

            # create a comment object
            comment_instance = Comment(postId, id, name, email, body)
            mycursor.execute(comment_instance.insert())
        cls.close_db()



    @classmethod
    def insert_data_in_albums(cls):
        mycursor = cls.database_initializer()
        json_obj = requests.get(cls.api_url + 'albums').json()
        for album in json_obj:
            userId    = album.get('userId')
            id        = album.get('id')
            title     = album.get('title')

            # create an instance of album
            album_instance = Album(userId, id, title)
            mycursor.execute(album_instance.insert())
        cls.close_db()




    @classmethod
    def insert_data_in_photos(cls):
        mycursor = cls.database_initializer()
        json_obj = requests.get(cls.api_url + 'photos').json()
        for photo in json_obj:
            albumId         = photo.get('albumId')
            id              = photo.get('id')
            title           = photo.get('title')
            url             = photo.get('url')
            thumbnailUrl    = photo.get('thumbnailUrl')

            # create a photo object
            photo_instance = Photo(albumId, id, title, url, thumbnailUrl)
            mycursor.execute(photo_instance.insert())
        cls.close_db()


    @classmethod
    def retrieve_from(cls, my_class):
        mycursor = cls.database_initializer()
        mycursor.execute(my_class.select())
        result = mycursor.fetchall()
        for res in result:
            print(res)
        print()

    @classmethod
    def retrieve_User_data(cls):
        cls.retrieve_from(User)

    @classmethod
    def retrieve_Todos_data(cls):
        cls.retrieve_from(Todo)

    @classmethod
    def retrieve_albums(cls):
        cls.retrieve_from(Album)

    @classmethod
    def retrieve_photos(cls):
        cls.retrieve_from(Photo)


    @classmethod
    def retrieve_posts(cls):
        cls.retrieve_from(Post)

    @classmethod
    def retrieve_comments(cls):
        cls.retrieve_from(Comment)
