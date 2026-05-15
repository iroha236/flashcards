import logic
import tkinter
import _tkinter

from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

window = None

# Menu window that opens upon starting application; can choose to view sets, create sets, edit sets, or exit
def start():
    try:
        global window

        window = tkinter.Tk()

        window.title("flashcards")
        window.geometry("640x480")
        window.resizable(False, False)

        window_icon = PhotoImage(file = "res/main_logo.png")
        window.iconphoto(False, window_icon)

        logo_img = PhotoImage(file = "res/logo.png")
        logo = tkinter.Label(window, image = logo_img)
        logo.place(relx = 0.5, rely = 0.25, anchor = "center")

        view_button = tkinter.Button(window, text = "View Set", width = 20, height = 2, command = view_set)
        view_button.place(relx = 0.5, rely = 0.55, anchor = "center")

        create_button = tkinter.Button(window, text = "Create Set", width = 20, height = 2, command = create_set)
        create_button.place(relx = 0.5, rely = 0.65, anchor = "center")

        edit_button = tkinter.Button(window, text = "Edit Set", width = 20, height = 2, command = lambda: edit_set(window))
        edit_button.place(relx = 0.5, rely = 0.75, anchor = "center")

        exit_button = tkinter.Button(window, text = "Exit", width = 20, height = 2, command = lambda: exit(window))
        exit_button.place(relx = 0.5, rely = 0.85, anchor = "center")

        window.mainloop()
    except _tkinter.TclError:
        window.destroy()

        messagebox.showerror("Missing Resources", "Resources from the 'res' directory (or the directory itself) appear to be missing. Closing application.")

# Opens upon clicking "View Set" from the starting menu; displays a screen to select a set to view
def view_set():
    view_window = Toplevel(window)

    view_window.title("View Set")
    view_window.geometry("480x480")
    view_window.resizable(False, False)
    view_window.grab_set()

    select_title = tkinter.Label(view_window, text = "Select a Set")
    select_title.place(relx = 0.5, rely = 0.058, anchor = "center")

    view_window_icon = PhotoImage(file = "res/main_logo.png")
    view_window.iconphoto(False, view_window_icon)

    scrollbar = tkinter.Scrollbar(view_window)

    all_sets = logic.created_sets()
    sets = tkinter.Listbox(view_window, yscrollcommand = scrollbar.set, width = 66, height = 20)
    
    for name in all_sets:
        sets.insert(END, name[:-4])

    sets.place(x = 30, y = 55)

    scrollbar.config(command = sets.yview)
    scrollbar.place(relx = 0.894, rely = 0.116, height = 322)

    view_button = tkinter.Button(view_window, text = "View", width = 20, height = 2, command = lambda: view(view_window, sets))
    view_button.place(relx = 0.7, rely = 0.89, anchor = "center")

    cancel_button = tkinter.Button(view_window, text = "Cancel", width = 20, height = 2, command = lambda: exit(view_window))
    cancel_button.place(relx = 0.3, rely = 0.89, anchor = "center")

# Opens upon clicking "Create Set" from the starting menu; displays the set creation screen
def create_set():
    create_window = Toplevel(window)

    create_window.title("Create Set")
    create_window.geometry("480x640")
    create_window.resizable(False, False)
    create_window.grab_set()

    create_window_icon = PhotoImage(file = "res/main_logo.png")
    create_window.iconphoto(False, create_window_icon)

    instructions_title = tkinter.Label(create_window, text = "Instructions\n\nSpecify your flashcards in the form of a line of text.\n" +
                                                             "Example: What is 1 + 1?~2\n" +
                                                             "The text left of the '~' represents the front of the flashcard, while the\n" +
                                                             "the text right of it represents the back. Each line of text represents one\n" +
                                                             "flashcard, and you can write as many of them as you wish. Flashcards\n" +
                                                             "will be automatically randomized, so the order you write them in does not\n" +
                                                             "matter. Lastly, lines that do not match the specified pattern will be ignored\n" +
                                                             "when the flashcards are generated, so please follow the format properly.")
    instructions_title.place(relx = 0.5, rely = 0.15, anchor = "center")

    scrollbar = tkinter.Scrollbar(create_window, orient = "horizontal")

    box = scrolledtext.ScrolledText(create_window, xscrollcommand = scrollbar.set, width = 50, height = 21, wrap = "none")
    box.insert(tkinter.INSERT, "What is 1 + 1?~2\nWhat is 2 + 2?~4")
    box.focus()
    box.place(relx = 0.5, rely = 0.57, anchor = "center")

    scrollbar.config(command = box.xview)
    scrollbar.place(relx = 0.484, y = 542, anchor = "center", width = 405)

    create_button = tkinter.Button(create_window, text = "Create", width = 20, height = 2, command = lambda: name_prompt(create_window, box.get("1.0", "end-1c")))
    create_button.place(relx = 0.7, rely = 0.925, anchor = "center")

    cancel_button = tkinter.Button(create_window, text = "Cancel", width = 20, height = 2, command = lambda: exit(create_window))
    cancel_button.place(relx = 0.3, rely = 0.925, anchor = "center")

# Opens upon clicking "Edit Set" from the starting menu; displays a screen to select a set to edit
def edit_set(window):
    edit_window = Toplevel(window)

    edit_window.title("Edit Set")
    edit_window.geometry("480x480")
    edit_window.resizable(False, False)
    edit_window.grab_set()

    select_title = tkinter.Label(edit_window, text = "Select a Set")
    select_title.place(relx = 0.5, rely = 0.058, anchor = "center")

    edit_window_icon = PhotoImage(file = "res/main_logo.png")
    edit_window.iconphoto(False, edit_window_icon)

    scrollbar = tkinter.Scrollbar(edit_window)

    all_sets = logic.created_sets()
    sets = tkinter.Listbox(edit_window, yscrollcommand = scrollbar.set, width = 66, height = 20)
    
    for name in all_sets:
        sets.insert(END, name[:-4])

    sets.place(x = 30, y = 55)

    scrollbar.config(command = sets.yview)
    scrollbar.place(relx = 0.894, rely = 0.116, height = 322)

    edit_button = tkinter.Button(edit_window, text = "Edit", width = 15, height = 2, command = lambda: edit(edit_window, sets))
    edit_button.place(relx = 0.8, rely = 0.89, anchor = "center")

    delete_button = tkinter.Button(edit_window, text = "Delete", width = 15, height = 2, command = lambda: delete(edit_window, sets))
    delete_button.place(relx = 0.5, rely = 0.89, anchor = "center")

    cancel_button = tkinter.Button(edit_window, text = "Cancel", width = 15, height = 2, command = lambda: exit(edit_window))
    cancel_button.place(relx = 0.2, rely = 0.89, anchor = "center")

# Exit the given window
def exit(to_destroy):
    to_destroy.destroy()

# Exit the given window and lock interactions to current window (only needed if the now current window is not the starting menu)
def exit_top_window(to_destroy, prev_window):
    to_destroy.destroy()

    prev_window.grab_set()

# Opens upon clicking "Create" from the set creation screen; prompts user to enter a name for the new set
def name_prompt(window, text):
    prompt = Toplevel(window)

    prompt.title("Name Set")
    prompt.geometry("300x150")
    prompt.resizable(False, False)
    prompt.grab_set()

    prompt_window_icon = PhotoImage(file = "res/main_logo.png")
    prompt.iconphoto(False, prompt_window_icon)

    name_instructions = tkinter.Label(prompt, text = "Enter a name for the set:")
    name_instructions.place(relx = 0.5, rely = 0.2, anchor = "center")

    name_box = tkinter.Entry(prompt, width = 30)
    name_box.focus()
    name_box.place(relx = 0.5, rely = 0.45, anchor = "center")

    confirm_button = tkinter.Button(prompt, text = "Confirm", width = 10, height = 1, command = lambda: process_new_set(window, prompt, name_box.get().strip(), text))
    confirm_button.place(relx = 0.7, rely = 0.75, anchor = "center")

    cancel_button = tkinter.Button(prompt, text = "Cancel", width = 10, height = 1, command = lambda: exit_top_window(prompt, window))
    cancel_button.place(relx = 0.3, rely = 0.75, anchor = "center")

# Called upon clicking "Confirm" after entering a name when creating a new set; either saves the set or indicates that the name was invalid
def process_new_set(create_window, prompt_window, name, text):
    if(not logic.verify_set_name(name)):
        messagebox.showwarning("Invalid Name Provided", "The name you provided is invalid. Valid characters include alphabetical " +
                                                        "and numerical characters, '-', and '_'. The total number of characters must be between 1-30.", parent = prompt_window)
    elif(logic.verify_name_exists(name)):
        messagebox.showwarning("Set Already Exists", "A set with the given name already exists.", parent = prompt_window)
    else:
        logic.create_set(name, text)

        prompt_window.destroy()
        create_window.destroy()

        messagebox.showinfo("Set Creation Confirmation", "Set created successfully.")

# Called upon clicking "Delete" from the edit set selection screen; prompts user to confirm if they want to delete the selected set
def delete(curr_window, sets):
    if(len(sets.curselection()) < 1):
        messagebox.showwarning("No Set Selected", "Select a set before deleting.", parent = curr_window)
    else:
        confirm = messagebox.askquestion("Delete Set", "Delete '" + sets.get(sets.curselection()[0]) + "'?", parent = curr_window, default = "no")

        if(confirm == "yes"):
            try:
                logic.process_deletion(sets.get(sets.curselection()[0]))

                curr_window.destroy()

                messagebox.showinfo("Set Deletion Confirmation", "Set deleted successfully.")
            except FileNotFoundError:
                logic.to_flashcards_dir()

                messagebox.showwarning("Could Not Find Selected Set", "The selected set could not be found. Try closing and reopening the current window, as it may be outdated.", parent = curr_window)
        else:
            pass

# Called upon clicking "Edit" from the edit set selection screen; opens the selected set for editing
def edit(curr_window, sets):
    if(len(sets.curselection()) < 1):
        messagebox.showwarning("No Set Selected", "Select a set before editing.", parent = curr_window)
    else:
        name = sets.get(sets.curselection()[0])

        try:
            text = logic.get_set_text(name)

            curr_window.destroy()

            editing_window = Toplevel(window)

            editing_window.title("Edit Set (Editing: " + name + ")")
            editing_window.geometry("480x640")
            editing_window.resizable(False, False)
            editing_window.grab_set()

            editing_window_icon = PhotoImage(file = "res/main_logo.png")
            editing_window.iconphoto(False, editing_window_icon)

            instructions_title = tkinter.Label(editing_window, text = "Instructions\n\nSpecify your flashcards in the form of a line of text.\n" +
                                                                    "Example: What is 1 + 1?~2\n" +
                                                                    "The text left of the '~' represents the front of the flashcard, while the\n" +
                                                                    "the text right of it represents the back. Each line of text represents one\n" +
                                                                    "flashcard, and you can write as many of them as you wish. Flashcards\n" +
                                                                    "will be automatically randomized, so the order you write them in does not\n" +
                                                                    "matter. Lastly, lines that do not match the specified pattern will be ignored\n" +
                                                                    "when the flashcards are generated, so please follow the format properly.")
            instructions_title.place(relx = 0.5, rely = 0.15, anchor = "center")

            scrollbar = tkinter.Scrollbar(editing_window, orient = "horizontal")

            box = scrolledtext.ScrolledText(editing_window, xscrollcommand = scrollbar.set, width = 50, height = 21, wrap = "none")
            box.insert(tkinter.INSERT, text)
            box.focus()
            box.place(relx = 0.5, rely = 0.57, anchor = "center")

            scrollbar.config(command = box.xview)
            scrollbar.place(relx = 0.484, y = 542, anchor = "center", width = 405)

            save_button = tkinter.Button(editing_window, text = "Save", width = 20, height = 2, command = lambda: save(editing_window, name, box.get("1.0", "end-1c")))
            save_button.place(relx = 0.7, rely = 0.925, anchor = "center")

            leave_button = tkinter.Button(editing_window, text = "Leave", width = 20, height = 2, command = lambda: leave_edit(editing_window, name, box.get("1.0", "end-1c")))
            leave_button.place(relx = 0.3, rely = 0.925, anchor = "center")
        except FileNotFoundError:
            logic.to_flashcards_dir()

            messagebox.showwarning("Could Not Find Selected Set", "The selected set could not be found. Try closing and reopening the current window, as it may be outdated.", parent = curr_window)

# Called upon clicking "Save" from the set editing screen; saves the set and gives a confirmation message
def save(curr_window, name, text):
    logic.create_set(name, text)

    messagebox.showinfo("Edit Confirmation", "Saved successfully.", parent = curr_window)

# Called upon clicking "Leave" from the set editing screen; either exits the editing screen or prompts users if they have unsaved changes
def leave_edit(curr_window, name, text):
    try:
        if(logic.changes_occurred(name, text)):
            confirm = messagebox.askquestion("Leave", "You have not saved your changes. Are you sure you want to leave?", parent = curr_window, default = "no")

            if(confirm == "yes"):
                curr_window.destroy()
            else:
                pass
        else:
            curr_window.destroy()
    except FileNotFoundError:
        logic.to_flashcards_dir()

        confirm = messagebox.askquestion("Leave", "You have not saved your changes. Are you sure you want to leave?", parent = curr_window, default = "no")

        if(confirm == "yes"):
            curr_window.destroy()
        else:
            pass

# Called upon clicking "View" from the view set selection screen; opens an interface that lets users observe their flashcard sets
# This includes flipping flashcards, proceeding to the next or previous flashcard, or finishing/exiting to the starting menu
def view(curr_window, sets):
    if(len(sets.curselection()) < 1):
        messagebox.showwarning("No Set Selected", "Select a set before viewing.", parent = curr_window)
    else:
        name = sets.get(sets.curselection()[0])

        try:
            if(logic.num_cards(name) < 1):
                messagebox.showwarning("No Valid Flashcards", "This set does not have any properly formatted flashcards. Please follow the flashcard creation instructions carefully.", parent = curr_window)
            else:
                cards = logic.get_cards(name)
                curr_card = [1]

                curr_window.destroy()

                viewing_window = Toplevel(window)

                viewing_window.title(name)
                viewing_window.geometry("640x400")
                viewing_window.resizable(False, False)
                viewing_window.grab_set()

                viewing_window_icon = PhotoImage(file = "res/main_logo.png")
                viewing_window.iconphoto(False, viewing_window_icon)

                text = scrolledtext.ScrolledText(viewing_window, width = 49, height = 20, wrap = tkinter.WORD)
                text.insert(END, logic.show_front(cards[curr_card[0] - 1]))
                text.config(state = "disabled")
                text.place(relx = 0.38, rely = 0.475, anchor = "center")

                count = tkinter.Label(viewing_window, text = str(curr_card[0]) + "/" + str(logic.num_cards(name)))
                count.place(relx = 0.355, rely = 0.93, anchor = "center")

                flip_button = tkinter.Button(viewing_window, text = "Flip", width = 15, height = 2, command = lambda: flip(viewing_window, name, cards, curr_card, text))
                flip_button.place(relx = 0.85, rely = 0.2, anchor = "center")

                next_button = tkinter.Button(viewing_window, text = "Next", width = 15, height = 2, command = lambda: next(viewing_window, name, cards, curr_card, text, count))
                next_button.place(relx = 0.85, rely = 0.4, anchor = "center")

                previous_button = tkinter.Button(viewing_window, text = "Previous", width = 15, height = 2, command = lambda: previous(viewing_window, name, cards, curr_card, text, count))
                previous_button.place(relx = 0.85, rely = 0.6, anchor = "center")

                finish_button = tkinter.Button(viewing_window, text = "Finish", width = 15, height = 2, command = lambda: exit(viewing_window))
                finish_button.place(relx = 0.85, rely = 0.8, anchor = "center")
        except FileNotFoundError:
            logic.to_flashcards_dir()

            messagebox.showwarning("Could Not Find Selected Set", "The selected set could not be found. Try closing and reopening the current window, as it may be outdated.", parent = curr_window)

# Called upon clicking "Flip" from the flashcard view screen; flips from the front of the flashcard to the back (or back to front)
def flip(curr_window, name, cards, curr_card, text):
    try:
        logic.set_still_exists(name)

        text.config(state = "normal")

        if(logic.show_front(cards[curr_card[0] - 1]) == text.get("1.0", "end-1c")):
            text.delete("1.0", END)
            text.insert(END, logic.show_back(cards[curr_card[0] - 1]))
        else:
            text.delete("1.0", END)
            text.insert(END, logic.show_front(cards[curr_card[0] - 1]))

        text.config(state = "disabled")
    except FileNotFoundError:
        logic.to_flashcards_dir()

        messagebox.showwarning("Set No Longer Found", "The current set no longer seems to exist. Try viewing your sets again, as the available sets may have changed.", parent = curr_window)

# Called upon clicking "Next" from the flashcard view screen; displays the next flashcard in the set
def next(curr_window, name, cards, curr_card, text, count):
    try:
        curr_card[0] = logic.next_card(name, curr_card[0])

        text.config(state = "normal")
        text.delete("1.0", END)
        text.insert(END, logic.show_front(cards[curr_card[0] - 1]))
        text.config(state = "disabled")

        count.config(text = str(curr_card[0]) + "/" + str(logic.num_cards(name)))
    except FileNotFoundError:
        logic.to_flashcards_dir()

        messagebox.showwarning("Set No Longer Found", "The current set no longer seems to exist. Try viewing your sets again, as the available sets may have changed.", parent = curr_window)

# Called upon clicking "Previous" from the flashcard view screen; displays the previous flashcard in the set
def previous(curr_window, name, cards, curr_card, text, count):
    try:
        curr_card[0] = logic.previous_card(name, curr_card[0])

        text.config(state = "normal")
        text.delete("1.0", END)
        text.insert(END, logic.show_front(cards[curr_card[0] - 1]))
        text.config(state = "disabled")

        count.config(text = str(curr_card[0]) + "/" + str(logic.num_cards(name)))
    except FileNotFoundError:
        logic.to_flashcards_dir()

        messagebox.showwarning("Set No Longer Found", "The current set no longer seems to exist. Try viewing your sets again, as the available sets may have changed.", parent = curr_window)