import sqlite3

conn = sqlite3.connect("blog.db")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS blog(id integer PRIMARY KEY,title TEXT NOT NULL,create_date TEXT NOT NULL,content TEXT NOT NULL, img_path TEXT NOT NULL)")

create_table()

# def drop_table():
#     c.execute("DROP TABLE blog")
#
#
# def data_entry():
#     unix = 12345
#     datestamp = "2017-08-20"
#     keyword = "python"
#     value = 5
#     c.execute('INSERT INTO blog (unix,datestamp,keyword,value) VALUES(?,?,?,?)', (unix, datestamp, keyword, value))
#     conn.commit()
#     conn.close()
#
# def read_from_db():
#     # c.execute('SELECT * FROM stuff_to_plot')
#     c.execute('SELECT * FROM blog WHERE value=5 AND keyword="python"')
#     data = c.fetchall()
#     return data
#
# def delete_and_update():
#     c.execute('SELECT * FROM blog')
#     [print(row) for row in c.fetchall()]
#     c.execute('UPDATE blog SET value = 99 WHERE value = 8')
#     c.execute('DELETE FROM blog where value = 99')
#     conn.commit()
#     c.execute('SELECT * FROM blog')
#     [print(row) for row in c.fetchall()]
#
# for row in read_from_db():
#     print(row)
# create_table()
# data_entry()

# if __name__ == "__main__":
#     create_table()