import datetime
  # peewee is a small and simple ORM, like mongoose but simpler
  # import everything from peewee
  # 

from peewee import *

  # We use the built in SqliteDatabase() function from peewee 
  # to save a reference to a DB file to a DATABASE variable
  # define a file to hold our db
DATABASE = SqliteDatabase('dbreddit.db')

  # Our Sub model is pretty simple, just a name and description for now
class Sub(Model):
    #   CharField has limit but , TextField has no limit
    timestamp = DateTimeField(default=datetime.datetime.now)
    name = CharField()  
    description = TextField()

    class Meta:
        database = DATABASE
        order_by = ('-timestamp',)

    # We initialize a connection to the DATABASE, create a table for the Sub model, 
    # and close the connection

class Post(Model):
    timestamp = DateTimeField(default=datetime.datetime.now)
    user = CharField()
    title = CharField()
    text = TextField()
    # relate the Post model to the Sub model
    sub = ForeignKeyField(Sub, backref="posts") 

    class Meta:
        database = DATABASE
        order_by = ('-timestamp',)

class Comment(Model):
    timestamp = DateTimeField(default=datetime.datetime.now)
    user = CharField()
    title = CharField()
    text = TextField()
    # relate the Comment model to the Post model
    post = ForeignKeyField(Post, backref="comments") 

    class Meta:
        database = DATABASE
        order_by = ('-timestamp',)


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Sub, Post, Comment], safe=True)
    DATABASE.close()