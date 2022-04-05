import sys
sys.path.insert(0, '../models/')
# sys.path.append("..")
from data_insertion import Model



class Controller:
    displayer = {
        'users': Model.insert_data_in_User,
        'todos': Model.insert_data_in_Todos,
        'posts': Model.insert_data_in_posts,
        'comments': Model.insert_data_in_comments,
        'albums': Model.insert_data_in_albums,
        'photos': Model.insert_data_in_photos,
        'all': [Model.insert_data_in_User, Model.insert_data_in_Todos,
                Model.insert_data_in_posts, Model.insert_data_in_comments,
                Model.insert_data_in_albums, Model.insert_data_in_photos]
    }
    insert_data = {
        'users': Model.retrieve_User_data,
        'todos': Model.retrieve_Todos_data,
        'posts': Model.retrieve_posts,
        'comments': Model.retrieve_comments,
        'albums': Model.retrieve_albums,
        'photos': Model.retrieve_photos,
        'all': [Model.retrieve_User_data, Model.retrieve_Todos_data,
                Model.retrieve_posts, Model.retrieve_comments,
                Model.retrieve_albums, Model.retrieve_photos]
    }

    @classmethod
    def display_model(cls, class_):
        if class_ == 'all':
            for display in cls.displayer.get(class_):
                display()
        else:
            cls.displayer.get(class_)()


    @classmethod
    def insert_data_in_tables(cls, class_):
        if class_ == 'all':
            for ret in cls.insert_data.get(class_):
                ret()
        else:
            cls.insert_data.get(class_)()
