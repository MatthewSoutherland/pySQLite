import database

myList = [
    ('1/4', '.25'),
    ('10mm', '.3937'),
    ('1/2', '.5'),
    ('5/8', '.625'),
]
database.add_many(myList)
database.show_all()

# testing