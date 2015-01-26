import peewee

myDB = peewee.MySQLDatabase("newspaper", host="localhost", port=3306, user="root", passwd="")

class MySQLModel(peewee.Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = myDB

class Category(MySQLModel) :
    id = peewee.PrimaryKeyField()
    name = peewee.CharField()


class Author (MySQLModel) :
    id = peewee.PrimaryKeyField()
    fn = peewee.CharField()
    ln = peewee.CharField()


class News(MySQLModel):
    id = peewee.IntegerField()
    title = peewee.CharField()
    body = peewee.CharField()
    date = peewee.CharField()
    category = peewee.ForeignKeyField(Category, related_name='news')
    author = peewee.ForeignKeyField(Author, related_name='news')

class negar(MySQLModel):
    id=peewee.PrimaryKeyField()
    img=peewee.CharField()
myDB.connect()

class login(MySQLModel):
    id=peewee.PrimaryKeyField()
    un=peewee.CharField()
    pas=peewee.CharField()
myDB.connect()




if __name__ == "__main__":
    # myDB.connect()
    myDB.create_tables([login])