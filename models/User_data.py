class User:
    def __init__(self, id='', name='', username='', email='', addressId='', phone='', website='', companyId=''):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.addressId = addressId #create a function to retrieve data from address
        self.phone = phone
        self.website = website
        self.companyId = companyId



    @classmethod
    def select(cls):
        return "SELECT * FROM users"
        # the cursor.execute(select_command) done in the controller



    def insert(self):
        insert_command = f"""
                INSERT INTO users (id, name, username, email, addressId, phone, website, companyId)
                VALUES ('{self.id}', '{self.name}', '{self.username}', '{self.email}', '{self.addressId}', '{self.phone}', '{self.website}', '{self.companyId}')
        """
        return insert_command




class Company:
    def __init__(self, name='', catchPhrase='', bs=''):
        self.name        = name
        self.catchPhrase = catchPhrase
        self.bs          = bs


    @classmethod
    def select(cls):
        return "SELECT * FROM company"

    def insert(self):
        insert_command = f"""
                INSERT INTO company (name, catchPhrase, bs)
                VALUES ('{self.name}', '{self.catchPhrase}', '{self.bs}')
        """

        return insert_command



class Address:
    def __init__(self, street='', suite='', city='', zipcode='', geo=''):
        self.street     = street
        self.suite      = suite
        self.city       = city
        self.zipcode    = zipcode
        self.geo        = str(geo)


    @classmethod
    def select(cls):
        return "SELECT * FROM address"


    def insert(self):
        insert_command = f"""
                INSERT INTO address (street, suite, city, zipcode, geo)
                VALUES ('{self.street}', '{self.suite}', '{self.city}', '{self.zipcode}', '{self.geo}')
        """

        return insert_command
