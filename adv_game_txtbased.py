import tkinter as tk

# Define game variables
inventory = []
left_path_completed = False
right_path_completed = False
current_location = "start"

# Create main game window interface
root = tk.Tk()
root.title("Text Adventure Game")

# Create text label to display the game o/p
output_label = tk.Label(root, text="", wraplength=600, justify="left")
output_label.pack()

# Create entry widget for player i/p
input_entry = tk.Entry(root)
input_entry.pack()

# Create a button to submit player i/p
submit_button = tk.Button(root, text="Submit", command=lambda: process_input(input_entry))
submit_button.pack()

# Func to update the game output with available choices
def update_output(text, choices=[]):
    if choices:
        text += "\nChoices: '" + "', '".join(choices) + "'"
    output_label.config(text=text)

# Define game funcs
def start_game():
    global current_location, inventory, left_path_completed, right_path_completed
    current_location = "start"
    inventory = []
    left_path_completed = False
    right_path_completed = False
    output_text = "You wake up in a mysterious forest. You can see two paths in front of you."
    update_output(output_text, ["left", "right"])

def left_path():
    global current_location
    current_location = "left"
    output_text = "You find a hidden cave and discover a treasure chest!"
    output_text += "\nDo you want to open the chest? (yes/no) or continue to the right path? (right)"
    update_output(output_text, ["yes", "no", "right"])

def right_path():
    global current_location
    current_location = "right"
    output_text = "You encounter a hostile dragon!"
    output_text += "\nDo you want to fight or run?"
    update_output(output_text, ["fight", "run"])

def end_game(result):
    if result == "win":
        output_text = "Congratulations! You WIN!!!You've successfully escaped the forest with a valuable gem and a magical potion."
        output_text += "\nDo you want to continue or quit the game?"
        update_output(output_text, ["continue", "quit"])
    else:
        output_text = "Game over. You didn't make it out of the forest as you did not have a sword to fight against the dragon."
        output_text += "\nDo you want to continue or quit the game? If you want to continue type right"
        update_output(output_text, ["continue", "quit"])

# Func to process player i/p with current_location as parameter
def process_input(input_field):
    choice = input_field.get().lower()
    input_field.delete(0, tk.END)  # Clr the i/p field

    if choice == "quit":
        output_text = "You quit the game."
        update_output(output_text)
        root.quit()  # Close the game win and exit the application
        return

    if current_location == "start":
        if choice == "left":
            left_path()
        elif choice == "right":
            right_path()
        else:
            output_text = "Invalid choice. Please choose one of the available options."
            update_output(output_text, ["left", "right"])
    elif current_location == "left":
        if choice == "yes":
            inventory.append("gem")
            inventory.append("potion")
            output_text = "You find a valuable gem and add it to your inventory.\nYou also find a magical potion."
            output_text += "\nDo you want to continue or quit the game?"
            update_output(output_text, ["continue", "quit"])
            left_path_completed = True
            check_game_over()
        elif choice == "no":
            output_text = "You leave the chest and continue your journey."
            output_text += "\nDo you want to continue or quit the game?"
            update_output(output_text, ["continue", "quit"])
            left_path_completed = True
            check_game_over()
        elif choice == "right":
            right_path()  # Continue to the right path
    elif current_location == "right":
        if choice == "fight":
            if "sword" in inventory:
                end_game("win")
            else:
                end_game("lose")
            right_path_completed = True
            check_game_over()
        elif choice == "run":
            inventory.append("sword")
            output_text = "You run away from the dragon and find a sword in a nearby cave."
            output_text += "\nDo you want to continue or quit the game?"
            update_output(output_text, ["continue", "quit"])
            right_path_completed = True
            check_game_over()

def check_game_over():
    if left_path_completed and right_path_completed:
        end_game("lose")  # Both paths completed, game over

# Start the game
start_game()

root.mainloop()
