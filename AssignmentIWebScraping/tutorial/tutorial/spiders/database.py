# import sqlite3

# conn = sqlite3.connect('myquotes.db') 
# curr = conn.cursor()

# #create table
# # curr.execute('''create table quotes2_tb(
# #                     title text,
# #                     author text,
# #                     tag text
# #                 )''')

# curr.execute("""insert into quotes2_tb values ('2Python!','2py','2pyth')""")

# conn.commit()
# conn.close()