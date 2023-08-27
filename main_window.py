import customtkinter, sqlite3
import tkinter as tk
from PIL import Image

MAROON = "#910000"
GRAY = "#4a4a48"

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

        self.vintage_entry = customtkinter.CTkEntry(self, width=250)
        self.vintage_entry.place(x=450, y=135)
        self.name_entry_label = customtkinter.CTkLabel(self, text="Varietal:")
        self.name_entry_label.place(x=400, y=135)

        self.entry = customtkinter.CTkEntry(self, width=250)
        self.entry.place(x=450, y=170)
        self.name_entry_label = customtkinter.CTkLabel(self, text="Vintage:")
        self.name_entry_label.place(x=400, y=170)

        self.entry = customtkinter.CTkEntry(self, width=250)
        self.entry.place(x=450, y=205)
        self.name_entry_label = customtkinter.CTkLabel(self, text="Bottles on Hand:")
        self.name_entry_label.place(x=355, y=205)

        self.entry = customtkinter.CTkEntry(self, width=250)
        self.entry.place(x=450, y=240)
        self.name_entry_label = customtkinter.CTkLabel(self, text="Bottle Price:")
        self.name_entry_label.place(x=380, y=240)

        self.entry = customtkinter.CTkEntry(self, width=250)
        self.entry.place(x=450, y=275)
        self.name_entry_label = customtkinter.CTkLabel(self, text="Distributor:")
        self.name_entry_label.place(x=385, y=275)

        self.add_button = customtkinter.CTkButton(self, text="Add Wine", hover_color='white',
                                                  text_color="black", fg_color=GRAY, border_color=GRAY,
                                                  border_width=2, compound="right", width=150, height=40, image=add_icon)
        self.add_button.place(x=500, y=325)

class SearchWineWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("600x450")
        self.title("Search Inventory")
        self.resizable(False, False)
        self.configure(fg_color=MAROON, padx=15)
        self.theme = customtkinter.set_appearance_mode("dark")

        self.name_search = customtkinter.CTkEntry(self, width=250)
        self.name_search.place(x=200, y=285)
        self.name_search_label = customtkinter.CTkLabel(self, text="Name:")
        self.name_search_label.place(x=160, y=285)

        self.vintage_search = customtkinter.CTkEntry(self, width=250)
        self.vintage_search.place(x=200, y=320)
        self.vintage_search_label = customtkinter.CTkLabel(self, text="Vintage:")
        self.vintage_search_label.place(x=153, y=320)

        self.count_update = customtkinter.CTkEntry(self, width=250)
        self.count_update.place(x=200, y=355)
        self.count_update_label = customtkinter.CTkLabel(self, text="Update Count:")
        self.count_update_label.place(x=120, y=355)

        self.search_button = customtkinter.CTkButton(self,  text="Search Wines", hover_color="#ffffff",
                                                     text_color="black", fg_color=GRAY, border_color=GRAY,
                                                     border_width=2, compound="right")

        self.update_count_button = customtkinter.CTkButton(self, text="Update Count", hover_color="#ffffff",
                                                     text_color="black", fg_color=GRAY, border_color=GRAY,
                                                     border_width=2, compound="right")

        self.list_all_wines = customtkinter.CTkButton(self, text="List All Wines", hover_color="#ffffff",
                                                     text_color="black", fg_color=GRAY, border_color=GRAY,
                                                     border_width=2, compound="right")


        self.update_count_button.place(x=80, y=400)
        self.search_button.place(x=240, y=400)
        self.list_all_wines.place(x=400, y=400)

class DeleteWineWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("675x300")
        self.title("Delete Wine")
        self.resizable(False, False)
        self.configure(fg_color=MAROON, padx=15)
        self.theme = customtkinter.set_appearance_mode("dark")

        self.name_entry = customtkinter.CTkEntry(self, width=250)
        self.name_entry.place(x=70, y=115)
        self.name_entry_label = customtkinter.CTkLabel(self, text="Name:")
        self.name_entry_label.place(x=20, y=115)

        self.vintage = customtkinter.CTkEntry(self, width=250)
        self.vintage.place(x=70, y=155)
        self.vintage_label = customtkinter.CTkLabel(self, text="Vintage:")
        self.vintage_label.place(x=20, y=155)

        self.delete_button = customtkinter.CTkButton(self,  text="Delete Wine", hover_color="#ffffff",
                                                     text_color="black", fg_color=GRAY, border_color=GRAY,
                                                     border_width=2, compound="right")
        self.delete_button.place(x=115, y=205)

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

root = MainWindow()
root.mainloop()