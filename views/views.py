# ici on doit mettre l'affichage de notre systeme
import sys
sys.path.insert(0, '../controllers/')

from controller import Controller


class View:
    menu_choice = [
        "Récupérer l'API et insérer des données dans la base de donnée",
        "Sélectionnez dans la BASE DE DONNÉES"
    ]
    selection_choice = [
        'Select all users',
        'Select all todos',
        'Select all posts',
        'Select all comments',
        'Select all albums',
        'Select all photos',
        'Select them all'
    ]
    @classmethod
    def selection(cls):
        try:
            while len(cls.selection_choice) > 0:
                for ind, choice in enumerate(cls.selection_choice):
                    print(f"                {ind + 1}.{choice}")
                print("                press 'ctrl + c': to quit")
                try:
                    schoice = int(input())
                except ValueError:
                    cls.selection()
                if schoice == 0:
                    cls.selection()
                popped = cls.selection_choice[schoice - 1].split()[2]
                Controller.insert_data_in_tables(popped)
                print(100 * '-')
                cls.selection()
        except KeyboardInterrupt:
            print()
            sys.exit('Merci! A bientot ..')



    @classmethod
    def menu(cls):
        xchoice = ''
        while xchoice == '' or xchoice is not int:
            for ind, choice in enumerate(cls.menu_choice):
                print(f"{ind + 1}.{choice}")
            try:
                xchoice = int(input())
            except ValueError:
                cls.menu()

            if xchoice == 2:
                cls.selection()
            elif xchoice == 1:
                # cls.menu_choice.remove(cls.menu_choice[xchoice - 1])
                try:
                    print('Fetching information from : jsonplaceholder.typicode.com ...')
                    Controller.display_model('all')
                    cls.menu()
                except:
                    print('The database is already provided\n You can start your queries')
                    cls.menu()



if __name__ == "__main__":
    View.menu()
