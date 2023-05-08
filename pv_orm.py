
import peewee
import datetime

db = peewee.SqliteDatabase('test.db')

class Author(peewee.Model):

    first_name = peewee.CharField(max_length=255)
    last_name = peewee.CharField(max_length=255)
    
    class Meta:

        database = db
        db_table = 'author'
        
class Article(peewee.Model):
    
    author = peewee.ForeignKeyField(Author, backref='author')
    title = peewee.CharField(max_length=255)
    publised_date = peewee.DateField(null=True)
    pages = peewee.IntegerField(null=True)
    
    class Meta:
        database = db
        db_table = 'article'
        
        
# Creating the table


def create_tables():
    with db:
        db.create_tables([Author, Article])
        

def create_author(fname: str, lname: str):
    Author.create(first_name = fname, last_name=lname)
    
def get_author(fname: str)-> int:

    return Author.select().where(Author.first_name==fname).get()
    
def create_article(author: str, title: str, publised):

    Article.create(author=author, title=title, publised=publised)
    
def get_article_by_title(title: str):

    return Article.select().where(Article.title==title)

def get_article_by_author_first_name(fname: str):

    return Article.select().join(Author).where(Author.first_name==fname)

def delete_author(fname: str):
    query = Author.delete().where(Author.first_name==fname)
    query.execute()

def update_author_lastname_by_firstname(fname: str, lname: str):
    query = Author.update(last_name=lname).where(Author.first_name==fname)
    query.execute()
    
# using methods
create_tables()
create_author("vikram", "Choudhary")

update_author_lastname_by_firstname("vikram", "k")
author = get_author(fname="vikram") 
print(author.last_name)
# create_article(author=author, title="Journey to the west", publised=datetime.date(1993,7,7))

# k = Article.select().join(Author).where(Author.first_name=="vikram").get()
# print(k.title)

# k = get_article_by_title("Journey to the west")
# print(k)
# s = delete_author("vikram")
# s = s.execute()
# print(s)