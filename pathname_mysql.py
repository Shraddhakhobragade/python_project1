import tkinter as tk
from tkinter import filedialog
import mysql.connector
import tkinter as tk


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="shraddha@2000",
  database="sk"
)


mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS files (id INT AUTO_INCREMENT PRIMARY KEY, path VARCHAR(255))")


def save_file_path():
    file_path = filedialog.askopenfilename()
    
   
    sql = "INSERT INTO files (path) VALUES (%s)"
    val = (file_path,)
    mycursor.execute(sql, val)
    mydb.commit()
    
    print("File path saved!")


base = tk.Tk()

save_button = tk.Button(base, text="Select File", fg="white",bg="#030e4f",font=("Times New Roman",12),command=save_file_path)
save_button.place(x=20,y=50)

base.mainloop()
