# "Database code" for the DB Forum.

import datetime

POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
		db = psycopg2.connect("dbname=forum")
		c = db.cursor()
		c.exexute("SELECT time, content FROM posts ORDER BY time")
		posts = ({'content' : str(row[1]), 'time' : str(row[0])}
				for row in c.fetchall())
		db.close()
		return posts

def add_post(content):
		db= psycopg2.connect("dbname=forum")
		c = db.cursor()
		c.execute("INSERT INTO posts (content) VALUES (%s)",
					(content,)
		db.commit()
		c.execute("UPDATE posts set content ='cheese' where content like '% spam %'")
		db.commit()
		db.close()


