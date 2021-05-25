from imdb import conn
cursor=conn.cursor()
from tkinter import *
root=Tk()
def get_top_100():
      
    sql = f"""
    SELECT TOP {e.get()} *
    FROM title_basics;
    """
    cursor.execute(sql)
    rows = cursor.fetchall()
    count=1
    for row in rows:
        label=Label(text=row).grid(row=count,column=1)
        count+=1
def print_dir_query():
    
    for row in cursor.tables():
        print(row)

def close_connection():
    conn.close()

e=Entry(root,width=30)
e.grid(row=1,column=3)    
display_button=Button(root,text='click me', command=get_top_100).grid(row=0,column=0)
tables_button=Button(root,text='print tables', command=print_dir_query).grid(row=0,column=2)
close_button=Button(root,text='close connection', command=close_connection).grid(row=0,column=1)
root.mainloop()