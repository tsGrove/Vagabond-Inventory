import customtkinter, sqlite3
import tkinter as tk
from PIL import Image
from tkinter import messagebox, END

MAROON = "#910000"
GRAY = "#4a4a48"

connection = sqlite3.connect('wine_database.db')
cursor = connection.cursor()

try:
    cursor.execute("""CREATE TABLE wine_database (
                    name text,
                    grape text,
                    vintage integer,
                    on_hand integer,
                    bottle_price integer
                     )""")
    print("Database Created")

except sqlite3.OperationalError:
    print('Database exists')

add_icon = customtkinter.CTkImage(Image.open("images/add.png").resize((20, 20)))
magnifying_icon = customtkinter.CTkImage(Image.open("images/magnifying-glass.png").resize((20, 20)))
remove_icon = customtkinter.CTkImage(Image.open("images/remove.png").resize((20, 20)))

class AddWineWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("750x450")
        self.title("Add New Wine")
        self.resizable(False, False)
        self.configure(fg_color=MAROON, padx=15)
        self.theme = customtkinter.set_appearance_mode("dark")

        self.canvas = tk.Canvas(self, width=350, height=350, highlightthickness=0)
        self.logo = tk.PhotoImage(file='images/grapes.png')
        self.canvas.create_image(175, 175, image=self.logo)
        self.canvas.place(x=0, y=30)
        self.canvas.config(background=MAROON)

        self.name_entry = customtkinter.CTkEntry(self, width=250)
        self.name_entry.place(x=450, y=100)
        self.name_entry_label = customtkinter.CTkLabel(self, text="Name:")
        self.name_entry_label.place(x=410, y=100)

        self.varietal_entry = customtkinter.CTkEntry(self, width=250)
        self.varietal_entry.place(x=450, y=135)
        self.varietal_entry_label = customtkinter.CTkLabel(self, text="Varietal:")
        self.varietal_entry_label.place(x=400, y=135)

        self.vintage_entry = customtkinter.CTkEntry(self, width=250)
        self.vintage_entry.place(x=450, y=170)
        self.vintage_entry_label = customtkinter.CTkLabel(self, text="Vintage:")
        self.vintage_entry_label.place(x=400, y=170)

        self.bottle_count_entry = customtkinter.CTkEntry(self, width=250)
        self.bottle_count_entry.place(x=450, y=205)
        self.bottle_count_entry_label = customtkinter.CTkLabel(self, text="Bottles on Hand:")
        self.bottle_count_entry_label.place(x=355, y=205)

        self.bottle_price_entry = customtkinter.CTkEntry(self, width=250)
        self.bottle_price_entry.place(x=450, y=240)
        self.bottle_price_entry_label = customtkinter.CTkLabel(self, text="Bottle Price:")
        self.bottle_price_entry_label.place(x=380, y=240)

        self.distributor_entry = customtkinter.CTkEntry(self, width=250)
        self.distributor_entry.place(x=450, y=275)
        self.distributor_entry_label = customtkinter.CTkLabel(self, text="Distributor:")
        self.distributor_entry_label.place(x=385, y=275)

        self.add_button = customtkinter.CTkButton(self, text="Add Wine", hover_color='white',
                                                  text_color="black", fg_color=GRAY, border_color=GRAY,
                                                  border_width=2, compound="right", width=150, height=40, image=add_icon,
                                                  command=self.add_wine_to_db)
        self.add_button.place(x=500, y=325)

    def add_wine_to_db(self):
        try:
            name = self.name_entry.get().title()
            varietal = self.varietal_entry.get().title()
            vintage = int(self.vintage_entry.get())
            on_hand = int(self.bottle_count_entry.get())
            bottle_price = int(self.bottle_price_entry.get())
            distributor = self.distributor_entry.get()

            wine_info = (name, varietal, vintage, distributor)

            if '' in wine_info:
                messagebox.showinfo(title='Wait a second', message='It would seem you left a field or two empty!')

            else:
                with connection:
                    cursor.execute("SELECT * FROM wine_database WHERE name =:name AND vintage =:vintage",
                                   {
                                       'name': name,
                                       'vintage': vintage
                                   })
                    wine = cursor.fetchone()

                    if wine is None:
                        cursor.execute("INSERT INTO wine_database VALUES (:name, :grape, :vintage,"
                                       " :on_hand, :bottle_price)",
                                       {
                                           "name": name, "grape": varietal, "on_hand": on_hand,
                                           'vintage': vintage, "bottle_price": bottle_price
                                       })
                        messagebox.showinfo(title='Successful', message=f'{name} has successfully been added '
                                                                        f'to the database!')

                    else:
                        messagebox.showerror(title="Uh-oh", message="It would appear that that wine is already "
                                                                    "in the database!")
                        self.name_entry.delete(0, END)
                        self.varietal_entry.delete(0, END)
                        self.vintage_entry.delete(0, END)
                        self.bottle_count_entry.delete(0, END)
                        self.bottle_price_entry.delete(0, END)
                        self.distributor_entry.focus()

        except ValueError:
            messagebox.showinfo(title='Wait a second', message='Make sure every field is filled out and you are'
                                                               ' entering numbers for the vintage, bottles on hand'
                                                               ' and bottle prices!')


class SearchWineWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("600x450")
        self.title("Search Inventory")
        self.resizable(False, False)
        self.configure(fg_color=MAROON, padx=15)
        self.theme = customtkinter.set_appearance_mode("dark")

        self.canvas = tk.Canvas(self, width=350, height=350, highlightthickness=0)
        self.logo = tk.PhotoImage(file='images/wine_glass.png')
        self.canvas.create_image(175, 175, image=self.logo)
        self.canvas.place(x=140, y=-30)
        self.canvas.config(background=MAROON)

        self.name_search_entry = customtkinter.CTkEntry(self, width=250)
        self.name_search_entry.place(x=200, y=285)
        self.name_search_label = customtkinter.CTkLabel(self, text="Name:")
        self.name_search_label.place(x=160, y=285)

        self.vintage_search_entry = customtkinter.CTkEntry(self, width=250)
        self.vintage_search_entry.place(x=200, y=320)
        self.vintage_search_label = customtkinter.CTkLabel(self, text="Vintage:")
        self.vintage_search_label.place(x=153, y=320)

        self.count_update = customtkinter.CTkEntry(self, width=250)
        self.count_update.place(x=200, y=355)
        self.count_update_label = customtkinter.CTkLabel(self, text="Update Count:")
        self.count_update_label.place(x=120, y=355)

        self.search_button = customtkinter.CTkButton(self,  text="Search Wines", hover_color="#ffffff",
                                                     text_color="black", fg_color=GRAY, border_color=GRAY,
                                                     border_width=2, compound="right", image=magnifying_icon,
                                                     command=self.search_wines)

        self.update_count_button = customtkinter.CTkButton(self, text="Update Count", hover_color="#ffffff",
                                                     text_color="black", fg_color=GRAY, border_color=GRAY,
                                                     border_width=2, compound="right",
                                                           command=self.update_counts)

        self.list_all_wines = customtkinter.CTkButton(self, text="List All Wines", hover_color="#ffffff",
                                                     text_color="black", fg_color=GRAY, border_color=GRAY,
                                                     border_width=2, compound="right")


        self.update_count_button.place(x=80, y=400)
        self.search_button.place(x=240, y=400)
        self.list_all_wines.place(x=400, y=400)

    def search_wines(self):
        try:
            name =  self.name_search_entry.get().title()
            vintage = int(self.vintage_search_entry.get())
            wine_info = (name, vintage)
            if '' in wine_info:
                messagebox.showinfo(title='Wait a second', message='It would seem you left a field or two empty!')
            else:
                with connection:
                    cursor.execute("SELECT * FROM wine_database WHERE name =:name AND vintage =:vintage",
                                   {
                                       'name': name,
                                       'vintage': vintage
                                   })
                    wine = cursor.fetchone()
                    if wine is not None:
                        tk.messagebox.showinfo(title='Info', message=f'Name: {wine[0]}, Varietal: {wine[1]}, '
                                                                  f'Vintage: {wine[2]},\n '
                                                                  f'Bottles on Hand: {wine[3]}, '
                                                                  f'Bottle Price: {wine[4]}')
                        self.name_search_entry.focus()
                    else:
                        tk.messagebox.showerror(title='Uh-oh', message="Sorry, looks like that wine"
                                                                    " isn't in the database!")
                        self.name_search_entry.focus()
        except ValueError:
            messagebox.showinfo(title='Wait a second', message='Make sure all the fields are filled out and you are'
                                                               ' entering numerical values for the vintage!')

    def update_counts(self):
        try:
            name = self.name_search_entry.get().title()
            vintage = int(self.vintage_search_entry.get())
            bottle_updated_count = int(self.count_update.get())
            info = (name, vintage, bottle_updated_count)

            if '' in info:
                messagebox.showinfo(title='Wait a second', message='It would seem you left a field or two empty!')

            else:
                with connection:
                    cursor.execute("SELECT * FROM wine_database WHERE name =:name AND vintage =:vintage",
                                   {
                                       'name': name,
                                       'vintage': vintage
                                   })
                    wine = cursor.fetchone()

                    if wine is not None:
                        cursor.execute("""UPDATE wine_database SET on_hand =:on_hand
                                        WHERE name =:name AND vintage =:vintage""",
                                       {
                                           'name': name, 'vintage': vintage,
                                           'on_hand': bottle_updated_count
                                       })
                        messagebox.showinfo(title='Success', message=f"Bottle count successfully updated to"
                                                                     f" {bottle_updated_count}!")
                        self.name_search_entry.delete(0, END)
                        self.vintage_search_entry.delete(0, END)
                        self.count_update.delete(0, END)
                        self.name_search_entry.focus()

                    else:
                        messagebox.showerror(title="Hold up king", message="That wine doesn't appear to be in the "
                                                                           "inventory, double check spelling.")

        except ValueError:
            messagebox.showinfo(title='Wait a second', message='Make sure all the fields are filled out and you are'
                                                               ' entering numerical values for the vintage!')

class DeleteWineWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("675x300")
        self.title("Delete Wine")
        self.resizable(False, False)
        self.configure(fg_color=MAROON, padx=15)
        self.theme = customtkinter.set_appearance_mode("dark")

        self.trash_can_canvas = tk.Canvas(self, width=225, height=248, highlightthickness=0)
        self.trash_can_logo = tk.PhotoImage(file='images/trash_can.png')
        self.trash_can_canvas.create_image(112, 124, image=self.trash_can_logo)
        self.trash_can_canvas.place(x=375, y=25)
        self.trash_can_canvas.config(background=MAROON)

        self.name_entry = customtkinter.CTkEntry(self, width=250)
        self.name_entry.place(x=70, y=115)
        self.name_entry_label = customtkinter.CTkLabel(self, text="Name:")
        self.name_entry_label.place(x=25, y=115)

        self.vintage = customtkinter.CTkEntry(self, width=250)
        self.vintage.place(x=70, y=155)
        self.vintage_label = customtkinter.CTkLabel(self, text="Vintage:")
        self.vintage_label.place(x=20, y=155)

        self.delete_button = customtkinter.CTkButton(self,  text="Delete Wine", hover_color="#ffffff",
                                                     text_color="black", fg_color=GRAY, border_color=GRAY,
                                                     border_width=2, compound="right", image=remove_icon,
                                                     command=self.delete_wine)
        self.delete_button.place(x=115, y=205)

    def delete_wine(self):
        try:
            name = self.name_entry.get().title()
            vintage = int(self.vintage.get())
            info = (name, vintage)

            if '' in info:
                messagebox.showinfo(title='Wait a second', message='It would seem you left a field or two empty!')

            else:
                with connection:
                    cursor.execute("SELECT * FROM wine_database WHERE name =:name AND vintage =:vintage", {
                        'name': name, 'vintage': vintage
                    })
                    wine_search = cursor.fetchone()
                    if wine_search is not None:
                        answer = messagebox.askyesno(title='Confirmation', message=f"Are you sure you want to delete "
                                                                                   f"{name}, "
                                                                                   f"Vintage: {vintage}"
                                                                                   f" from the database?")
                        if answer:
                            cursor.execute("DELETE from wine_database WHERE name = :name AND vintage = :vintage",
                                           {'name': name, 'vintage': self.vintage})
                            messagebox.showinfo(title="Completed",
                                                message=f"{name} has been successfully removed.")
                            self.name_entry.delete(0, END)
                            self.vintage.delete(0, END)
                            self.name_entry.focus()
                        else:
                            messagebox.showinfo(title='Okay', message='Alrighty then')
                    else:
                        messagebox.showerror(title="Hold up king", message="That wine doesn't appear to be in the "
                                                                           "inventory, double check spelling.")
                self.name_entry.focus()

        except ValueError:
            messagebox.showerror(title='Vintage', message='Make sure you are filling out both fields and '
                                                          'entering a numerical value for the vintage!')

class MainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.delete_window = None
        self.search_window = None
        self.add_window = None

        self.geometry("750x425")
        self.title("Wine Inventory")
        self.resizable(False, False)
        self.configure(fg_color=MAROON, padx=15)

        self.canvas = tk.Canvas(width=500, height=350, highlightthickness=0)
        self.logo = tk.PhotoImage(file='images/Logo.png')
        self.canvas.create_image(250, 175, image=self.logo)
        self.canvas.place(x=110, y=30)
        self.canvas.config(background=MAROON)

        self.button_frame = customtkinter.CTkFrame(self)
        self.button_frame.configure(width=625, height=100, bg_color=MAROON, fg_color=MAROON)
        self.button_frame.place(x=50, y=375)

        self.add_button = customtkinter.CTkButton(self.button_frame, text="Add Wine", hover_color='white',
                                                  text_color="black", fg_color=GRAY, command=self.add_wine_window,
                                                  border_color=GRAY, border_width=2, image=add_icon, compound="right")

        self.search_button = customtkinter.CTkButton(self.button_frame, text="Search & Update Wine", hover_color="#ffffff",
                                                     text_color="black", fg_color=GRAY, command=self.search_wine_window,
                                                     border_color=GRAY, border_width=2, image=magnifying_icon, compound="left")

        self.remove_button = customtkinter.CTkButton(self.button_frame, text="86 Wine", hover_color="#ffffff",
                                                     text_color="black", fg_color=GRAY, command=self.delete_wine_window,
                                                     border_color=GRAY, border_width=2, image=remove_icon, compound="right")


        self.add_button.grid(row=0, column=0, padx=30)
        self.search_button.grid(row=0,column=1, padx=30)
        self.remove_button.grid(row=0,column=2,padx=30)



    def add_wine_window(self):
        if self.add_window:
            self.add_window.name_entry_label.focus()
        else:
            self.add_window = AddWineWindow(self)
            self.add_window.name_entry_label.focus()


    def search_wine_window(self):
        if self.search_window:
            self.search_window.focus()
        else:
            self.search_window = SearchWineWindow(self)

    def delete_wine_window(self):
        if self.delete_window:
            self.delete_window.focus()
        else:
            self.delete_window = DeleteWineWindow(self)
