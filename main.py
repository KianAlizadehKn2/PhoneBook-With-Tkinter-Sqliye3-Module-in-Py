# PhoneBook Program is programmed by Kian Alizadeh with SQL & GUI & python 3.11
"""
Programmer : Kian Alizadeh
Program Name :Phonebook
Ver : 0.0.1
"""
import sqlite3 as sdb  # my sqlite3 Module as sdb
import tabulate  # My tabulate Module
import prettytable  # My prettytable Module
from tkinter import *  # My tkinter Module
from tkinter import messagebox  # my messagebox from tkinter Module
from PIL import Image, ImageTk  # My pil from image & image tk Module


# My connect_to_my_data_base function
def connect_to_my_data_base(x):
    # Connect to SQLite database
    con = sdb.Connection("phonebook.db")
    cur = con.cursor()
    alldata = cur.execute(x)
    data = alldata.fetchall()
    con.commit()
    con.close()
    return data


# My main function
def main():
    # Create table if it doesn't exist
    cmd = """ CREATE TABLE IF NOT EXISTS contacts ( id integer primary key autoincrement, first_name TEXT,  
                                                    last_name TEXT, phone TEXT, address TEXT, 
                                                        email TEXT, NewColumn TEXT)"""
    data = connect_to_my_data_base(cmd)
    return data


# My class as MyFirstGUI
class MyFirstGUI:
    def __init__(self, window):  # My __init_ function in class with self and window
        self.window = window  # My window

        # My window title & geometry
        window.title('Phone Book')
        window.geometry("700x700")

        # Create the form
        # first_name_label & first_name_entry
        first_name_label = Label(window, text='First_Name:', bg="yellow", fg="black")
        first_name_label.grid(row=0, column=0, pady=2)
        self.first_name_entry = Entry(window)
        # Added 'self.' here
        self.first_name_entry.grid(row=0, column=1)

        # last_name_label & last_name_entry
        last_name_label = Label(window, text='Last_Name:', bg="black", fg="orange")
        last_name_label.grid(row=1, column=0, pady=2)
        self.last_name_entry = Entry(window)
        # Added 'self.' here
        self.last_name_entry.grid(row=1, column=1)

        # phone_label & phone_entry
        phone_label = Label(window, text='Phone:', bg="orange", fg="green")
        phone_label.grid(row=2, column=0, pady=2)
        self.phone_entry = Entry(window)
        # Added 'self.' here
        self.phone_entry.grid(row=2, column=1)

        # address_label & address_entry
        address_label = Label(window, text='Address:', bg="red", fg="blue")
        address_label.grid(row=3, column=0, pady=2)
        self.address_entry = Entry(window)
        # Added 'self.' here
        self.address_entry.grid(row=3, column=1)

        # email-label & email_entry
        email_label = Label(window, text='Email:', bg="black", fg="white")
        email_label.grid(row=4, column=0, pady=2)
        self.email_entry = Entry(window)
        # Added 'self.' here
        self.email_entry.grid(row=4, column=1)

        # id_label & id_var & id_entry
        id_label = Label(window, text='id:', bg="black", fg="green")
        id_label.grid(row=5, column=0, pady=2)
        id_var = StringVar(window, value="None")
        self.id_entry = Entry(window, textvariable=id_var)
        # Added 'self.' here
        self.id_entry.grid(row=5, column=1)

        # show_tabulate_label & show_tabulate_var & show_tabulate_entry
        show_tabulate_label = Label(window, text='Show By Tabulate:', bg="white", fg="green")
        show_tabulate_label.grid(row=6, column=0, pady=2)
        show_tabulate_var = StringVar(window, value="None")
        self.show_tabulate_entry = Entry(window, textvariable=show_tabulate_var)
        # Added 'self.' here
        self.show_tabulate_entry.grid(row=6, column=1)

        # new_column_label & new_column_var & new_column_entry
        new_column_label = Label(window, text='New/OldColumn Name:', bg="pink", fg="black")
        new_column_label.grid(row=7, column=0, pady=2)
        new_column_var = StringVar(window, value="NewColumn")
        self.new_column_entry = Entry(window, textvariable=new_column_var)
        # Added 'self.' here
        self.new_column_entry.grid(row=7, column=1)

        # new_column_value_label & new_column_value_entry
        new_column_value_label = Label(window, text='New Value Of Column:', bg="red", fg="black")
        new_column_value_label.grid(row=9, column=0, pady=2)
        self.new_column_value_entry = Entry(window)
        # Added 'self.' here
        self.new_column_value_entry.grid(row=9, column=1)

        # new_column_name_label & new_column_name_var & new_column_name_entry
        new_column_name_label = Label(window, text='New/Old Column Rename:', bg="blue", fg="orange")
        new_column_name_label.grid(row=10, column=0, pady=2)
        new_column_name_var = StringVar(window, value="None")
        self.new_column_name_entry = Entry(window, textvariable=new_column_name_var)
        # Added 'self.' here
        self.new_column_name_entry.grid(row=10, column=1)

        # show_prettytable_label & show_prettytable_var & show_prettytable_entry
        show_prettytable_label = Label(window, text='Show By PrettyTable:', bg="green", fg="pink")
        show_prettytable_label.grid(row=11, column=0, pady=2)
        show_prettytable_var = StringVar(window, value="None")
        self.show_prettytable_entry = Entry(window, textvariable=show_prettytable_var)
        # Added 'self.' here
        self.show_prettytable_entry.grid(row=11, column=1)

        # insert_button
        right_padding = 40
        insert_button = Button(window, text='Insert Contact', command=self.inserting_contact, bg="red", fg="blue")
        # Added 'self.' here
        insert_button.grid(row=12, column=0, columnspan=2, padx=(0, right_padding), pady=2)

        # exit_button
        left_padding = 40
        exit_button = Button(window, text='Exit', command=self.closing_window, bg="black", fg="purple")
        # Added 'self.' here
        exit_button.grid(row=12, column=1, columnspan=2, padx=(left_padding, 0), pady=2)

        # get_id_button
        right_padding = 40
        get_id_button = Button(window, text='Get Max Id', command=self.getting_id_contact, bg="orange", fg="black")
        # Added 'self.' here
        get_id_button.grid(row=13, column=0, columnspan=2, padx=(0, right_padding), pady=2)

        # select_button
        left_padding = 40
        select_button = Button(window, text='Select Contact',
                               command=self.selecting_all_of_my_data_contact, bg="green", fg="brown")
        # Added 'self.' here
        select_button.grid(row=13, column=1, columnspan=2, padx=(left_padding, 0), pady=2)

        # select_id_button
        right_padding = 40
        select_id_button = Button(window, text='Select by Id',
                                  command=self.selecting_my_data_contact_by_id, bg="orange", fg="red")
        # Added 'self.' here
        select_id_button.grid(row=14, column=0, columnspan=2, padx=(0, right_padding), pady=2)

        # show_table_button
        left_padding = 40
        show_tabulate_table_button = Button(window, text='Show By Tabulate',
                                            command=self.showing_my_table_by_tabulate, bg="gray", fg="green")
        # Added 'self.' here
        show_tabulate_table_button.grid(row=14, column=1, columnspan=2, padx=(left_padding, 0), pady=2)

        # update_button
        right_padding = 40
        update_button = Button(window, text='Update Contact',
                               command=self.updating_my_contacts, bg="pink", fg="blue")
        # Added 'self.' here
        update_button.grid(row=15, column=0, columnspan=2, padx=(0, right_padding), pady=2)

        # add_column_button
        left_padding = 40
        add_column_button = Button(window, text='Add Column',
                                   command=self.adding_column_to_contacts_table, bg="purple", fg="orange")
        # Added 'self.' here
        add_column_button.grid(row=15, column=1, columnspan=2, padx=(left_padding, 0), pady=2)

        # insert_new_column_button
        right_padding = 40
        insert_new_column_button = Button(window, text='Insert Old or  New Column',
                                          command=self.inserting_value_into_my_database, bg="white", fg="purple")
        # Added 'self.' here
        insert_new_column_button.grid(row=16, column=0, columnspan=2, padx=(0, right_padding), pady=2)

        # add_column_button
        left_padding = 40
        change_column_name_button = Button(window, text='Rename Column',
                                           command=self.renaming_my_new_column_of_table, bg="black", fg="white")
        # Added 'self.' here
        change_column_name_button.grid(row=16, column=1, columnspan=2, padx=(left_padding, 0), pady=2)

        # remove_column_button
        right_padding = 40
        remove_column_button = Button(window, text='Remove Old or  New Column',
                                      command=self.removing_column, bg="green", fg="orange")
        # Added 'self.' here
        remove_column_button.grid(row=17, column=0, columnspan=2, padx=(0, right_padding), pady=2)

        # show_pretty_table_button
        left_padding = 60
        show_pretty_table_button = Button(window, text='Show By PrettyTable',
                                          command=self.showing_my_table_by_pretty_table, bg="brown", fg="green")
        # Added 'self.' here
        show_pretty_table_button.grid(row=17, column=1, columnspan=2, padx=(left_padding, 0), pady=2)

        # remove_contact_by-id_button
        right_padding = 40
        remove_contact_by_id_button = Button(window, text='Remove Contact By Id',
                                             command=self.removing_contacts_data_by_id, bg="red", fg="orange")
        # Added 'self.' here
        remove_contact_by_id_button.grid(row=18, column=0, columnspan=2, padx=(0, right_padding), pady=2)

        # programmer's_name_label
        left_padding = 60
        programmer_name_label = Label(window, text='Programmed By Kian Alizadeh', bg="yellow", fg="blue")
        programmer_name_label.grid(row=18, column=1, columnspan=2, padx=(left_padding, 0), pady=2)

        # Create an object of tkinter ImageTk
        image = Image.open("pic1.png")
        photo = ImageTk.PhotoImage(image)
        p1 = PhotoImage(file='pic1.png')

        # Setting icon of master window
        window.iconphoto(False, p1)

        # Create a Label Widget to display the text or Image
        label = Label(window, image=photo)
        label.image = photo
        label.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

    # My inserting_contact function
    def inserting_contact(self):
        first_name_input = self.first_name_entry.get().strip()  # My first_name_input as an entry
        last_name_input = self.last_name_entry.get().strip()  # My last_name_input as an entry
        phone_input = self.phone_entry.get().strip()  # My phone_input as an entry
        address_input = self.address_entry.get().strip()  # My address_input as an entry
        email_input = self.email_entry.get().strip()  # My email_input as an entry

        # checking the condition of my inputs with if & else
        if not first_name_input or not last_name_input or not phone_input or not address_input or not email_input:
            messagebox.showerror('Error', 'First_Name or Last_Name or Phone or Address or Email cannot be empty')
            return
        else:
            messagebox.showinfo('Success', 'Contact saved successfully')
            self.open_inserting_window()

        #  insert name_input and phone_input into my phonebook database
        cmd = f"""INSERT INTO contacts (first_name,  last_name, phone, address, email) 
                                VALUES ('{first_name_input}','{last_name_input}', '{phone_input}', '{address_input}',
                                        '{email_input}')"""
        data = connect_to_my_data_base(cmd)
        return data

    def open_inserting_window(self):
        # open a new window to display the inserted data
        new_window = Toplevel(self.window)
        new_window.title("Contact Details are inserting")
        new_window.geometry("400x200")

        # display the inserted data in the new window
        Label(new_window, text="First_Name:", bg="red", fg="purple").grid(row=0, column=0)
        Label(new_window, text=self.first_name_entry.get()).grid(row=0, column=1)

        Label(new_window, text="Last_Name:", bg="green", fg="yellow").grid(row=1, column=0)
        Label(new_window, text=self.last_name_entry.get()).grid(row=1, column=1)

        Label(new_window, text="Phone:", bg="blue", fg="orange").grid(row=2, column=0)
        Label(new_window, text=self.phone_entry.get()).grid(row=2, column=1)

        Label(new_window, text="Address:", bg="pink", fg="brown").grid(row=3, column=0)
        Label(new_window, text=self.address_entry.get()).grid(row=3, column=1)

        Label(new_window, text="Email:", bg="red", fg="green").grid(row=4, column=0)
        Label(new_window, text=self.email_entry.get()).grid(row=4, column=1)

    #  My get id function
    def getting_id_contact(self):
        id_input = self.id_entry.get().strip()  # My id_input
        # checking the condition of my inputs with if & else
        if id_input == "None":
            messagebox.showerror('Error', 'Id cannot be None')
            return
        else:
            messagebox.showinfo('Success', 'Id contact got successfully')
            self.open_getting_id_contact_window()

    def open_getting_id_contact_window(self):
        # open a new window to display the id got
        new_window = Toplevel(self.window)
        new_window.title("Contact  Id Details are getting")
        new_window.geometry("400x200")

        # DataBase Part
        con = sdb.Connection('phonebook.db')
        cur = con.cursor()
        cur.execute(f"""SELECT MAX(id) FROM contacts""")
        rows = cur.fetchall()
        headers = [description[0] for description in cur.description]
        table = tabulate.tabulate(rows, headers=headers, tablefmt="grid")
        Label(new_window, text=table, bg="green", fg="red").pack()  # My table label

    # My selecting_all_of_my_data_contact function
    def selecting_all_of_my_data_contact(self):
        last_name_input = self.last_name_entry.get().strip()  # My last_name_input
        phone_input = self.phone_entry.get().strip()  # My phone_input

        # checking the condition of my inputs with if & else
        if not last_name_input or not phone_input:
            messagebox.showerror('Error', 'Last_Name or Phone cannot be empty')
            return
        else:
            messagebox.showinfo('Success', 'Your Data are selected  successfully')
            self.open_selecting_data_contact_window()

    def open_selecting_data_contact_window(self):
        # open a new window to display the selected data
        new_window = Toplevel(self.window)
        new_window.title("Contacts Info are selecting")
        new_window.geometry("400x400")

        # open a new window to display the id got
        last_name_input = self.last_name_entry.get().strip()
        phone_input = self.phone_entry.get().strip()

        # DataBase Part 1
        con = sdb.Connection('phonebook.db')
        cur = con.cursor()
        cur.execute(f""" SELECT * FROM contacts WHERE last_name like '%{last_name_input}%'""")
        rows = cur.fetchall()
        headers = [description[0] for description in cur.description]
        table = tabulate.tabulate(rows, headers=headers, tablefmt="grid")

        # DataBase Part 2
        con1 = sdb.Connection('phonebook.db')
        cur1 = con1.cursor()
        cur1.execute(f"""SELECT * FROM contacts WHERE phone like '%{phone_input}%'""")
        rows1 = cur1.fetchall()
        headers1 = [description[0] for description in cur1.description]
        table1 = tabulate.tabulate(rows1, headers=headers1, tablefmt="grid")

        # display the inserted data in the new window
        Label(new_window, text="Last_Name:", bg="red", fg="blue").grid(row=0, column=0)
        Label(new_window, text=table, bg="yellow", fg="green").grid(row=0, column=1)

        Label(new_window, text="Phone:", bg="green", fg="purple").grid(row=1, column=0)
        Label(new_window, text=table1, bg="orange", fg="black").grid(row=1, column=1)

    # My selecting_my_data_contact_by_id
    def selecting_my_data_contact_by_id(self):
        id_input = self.id_entry.get().strip()  # My id_input

        # checking the condition of my id_input with if & else
        if id_input == "None":
            messagebox.showerror('Error', 'Id cannot be None')
            return
        else:
            messagebox.showinfo('Success', 'Id contact selected successfully')
            self.open_selecting_my_data_contact_by_id_window()
        #  select max id from my phonebook database
        cmd = f"""SELECT * FROM contacts WHERE id= '{id_input}'"""
        data = connect_to_my_data_base(cmd)
        return data

    def open_selecting_my_data_contact_by_id_window(self):
        id_input = self.id_entry.get().strip()  # My id_input
        # open a new window to display the selecting my data contact by id
        new_window = Toplevel(self.window)
        new_window.title("Contact are selecting by id")
        new_window.geometry("400x400")

        # Database part
        con = sdb.Connection('phonebook.db')
        cur = con.cursor()
        cur.execute(f"""SELECT * FROM contacts WHERE id= '{id_input}'""")
        rows = cur.fetchall()
        headers = [description[0] for description in cur.description]
        table = tabulate.tabulate(rows, headers=headers, tablefmt="grid")
        Label(new_window, text=table, bg="red", fg="green").pack()  # My table label

    # My showing_my_table_by_tabulate function
    def showing_my_table_by_tabulate(self):
        show_input = self.show_tabulate_entry.get().strip()  # My show_input

        # checking the condition of my inputs with if & else
        if show_input == "None":
            messagebox.showerror('Error', 'Show By Tabulate cannot be None')
            return
        else:
            messagebox.showinfo('Success', 'Show By Tabulate is done successfully')
            self.open_showing_my_table_by_tabulate()

    def open_showing_my_table_by_tabulate(self):
        # open a new window to display the table by tabulate
        new_window = Toplevel(self.window)
        new_window.title("Showing table by tabulate")
        new_window.geometry("400x400")

        # Database part
        con = sdb.Connection('phonebook.db')
        cur = con.cursor()
        cur.execute("""SELECT * FROM contacts""")
        rows = cur.fetchall()
        headers = [description[0] for description in cur.description]
        table = tabulate.tabulate(rows, headers=headers, tablefmt="grid")
        Label(new_window, text=table, bg="yellow", fg="blue").pack()  # My table label

    # My updating_my_contacts function
    def updating_my_contacts(self):
        id_input = self.id_entry.get().strip()  # My id_input
        phone_input = self.phone_entry.get().strip()  # My phone_input

        # checking the condition of my inputs with if & else
        if not id_input != 'None' or not phone_input:
            messagebox.showerror('Error', ' Id or Phone cannot be None or empty')
            return
        else:
            messagebox.showinfo('Success', 'Your Data are updated  successfully')

        #  update phone from id in  my phonebook database
        cmd = f""" UPDATE contacts SET phone='{phone_input}' WHERE id='{id_input}'"""
        data = connect_to_my_data_base(cmd)
        return data

    # My adding_column_to_contacts_table function
    def adding_column_to_contacts_table(self):
        new_column_input = self.new_column_entry.get().strip()  # My new_column_input

        # checking the condition of my inputs with if & else
        if new_column_input != 'NewColumn':
            messagebox.showerror('Error', 'New/Old Column must be New Column')
            return
        else:
            messagebox.showinfo('Success', 'Your new column are added  successfully')

        #  add new column into  my phonebook database
        cmd = f"""ALTER TABLE contacts ADD COLUMN '{new_column_input}' text"""
        data = connect_to_my_data_base(cmd)
        return data

    # My inserting_value_into_my_database function
    def inserting_value_into_my_database(self):
        new_column_input = self.new_column_entry.get().strip()  # My new_column_input
        new_column_value_input = self.new_column_value_entry.get().strip()  # My new_column_input
        id_input = self.id_entry.get().strip()  # My id_input

        # checking the condition of my inputs with if & else
        if not new_column_value_input or new_column_input == 'NewColumn' or id_input == 'None':
            messagebox.showerror('Error', 'New Value Of Column or New/OldColumnName or  '
                                          '                             Id cannot be empty or NewColumn or None')
            return
        else:
            messagebox.showinfo('Success', 'Your Value of New/Old Column are added  successfully')

        #  update my new column into  my phonebook database
        cmd = f"""UPDATE contacts SET '{new_column_input}'='{new_column_value_input}' WHERE id='{id_input}' """
        data = connect_to_my_data_base(cmd)
        return data

    # My renaming_my_new_column_of_table function
    def renaming_my_new_column_of_table(self):
        rename_new_column_name_input = self.new_column_name_entry.get().strip()  # My rename_new_column_name_input
        new_column_input = self.new_column_entry.get().strip()  # My new_column_input

        # checking the condition of my inputs with if & else
        if not rename_new_column_name_input != 'None':
            messagebox.showerror('Error', ' New/Old Column Rename cannot be None')
            return
        else:
            messagebox.showinfo('Success', 'Your Data are renamed successfully')

        #  update my new column into  my phonebook database
        cmd = f"""ALTER TABLE contacts RENAME '{new_column_input}' To '{rename_new_column_name_input}' """
        data = connect_to_my_data_base(cmd)
        return data

    # My removing_column function
    def removing_column(self):
        new_column_input = self.new_column_entry.get().strip()  # My new_column_input

        # checking the condition of my inputs with if & else
        if not new_column_input:
            messagebox.showerror('Error', ' New/Old Column cannot be empty')
            return
        else:
            messagebox.showinfo('Success', 'Your Data are removed successfully')

        #  update my new column into  my phonebook database
        cmd = f"""ALTER TABLE contacts DROP COLUMN '{new_column_input}'"""
        data = connect_to_my_data_base(cmd)
        return data

    # My showing_my_table_by_pretty_table
    def showing_my_table_by_pretty_table(self):
        show_input = self.show_prettytable_entry.get().strip()  # My show_input

        # checking the condition of my inputs with if & else
        if show_input == "None":
            messagebox.showerror('Error', 'Show ByPrettyTableTabulate cannot be None')
            return
        else:
            messagebox.showinfo('Success', 'Show By PrettyTable is done successfully')
            self.open_showing_my_table_by_pretty_table()

    def open_showing_my_table_by_pretty_table(self):
        # open a new window to display the table by tabulate
        new_window = Toplevel(self.window)
        new_window.title("Showing table by prettytable")
        new_window.geometry("700x700")

        # Database part
        con = sdb.Connection('phonebook.db')
        cur = con.cursor()
        cur.execute("""SELECT * FROM contacts""")
        rows = cur.fetchall()
        headers = [description[0] for description in cur.description]
        table = prettytable.PrettyTable(rows, headers=headers, tablefmt="grid")
        for row in cur.fetchall():
            table.add_row(row)
        Label(new_window, text=table, bg="orange", fg="blue").pack()  # My table label

    # My removing_contacts_data_with_id function
    def removing_contacts_data_by_id(self):
        id_input = self.id_entry.get().strip()  # My id_input

        # checking the condition of my inputs with if & else
        if id_input == "None":
            messagebox.showerror('Error', 'Id cannot be None')
            return
        else:
            messagebox.showinfo('Success', 'Contact is removed by Id successfully')

        #  remove my contact by id from  my phonebook database
        cmd = f""" DELETE FROM contacts WHERE id='{id_input}' """
        data = connect_to_my_data_base(cmd)
        return data

    # define a function to close the window
    def closing_window(self):
        # win.destroy()
        self.window.quit()


if __name__ == '__main__':
    main()

# Create the main window
window = Tk()
window.config(bg="gray")

# Creat MyFirstGUI Class with an Object with object_oriented method
my_gui = MyFirstGUI(window)

# Run the main loop
window.mainloop()
