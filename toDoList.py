import tkinter as tk
from tkinter import ttk
from datetime import datetime

class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.task_entry = ttk.Entry(root, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.due_date_entry = ttk.Entry(root, width=10)
        self.due_date_entry.grid(row=0, column=1, padx=5, pady=10)
        self.due_date_entry.insert(0, self.get_current_date())
        

        self.priority_entry = ttk.Entry(root, width=10)
        self.priority_entry.grid(row=0, column=2, padx=5, pady=10)
        self.priority_entry.insert(0, "Priority")
        self.priority_entry.bind("<Button-1>", self.clear_priority)

        self.add_button = ttk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=3, padx=5, pady=10)

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=10, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=4, padx=10, pady=10)
        self.task_listbox.bind("<ButtonRelease-1>", self.update_entry_fields)

        self.completed_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=5, width=50)
        self.completed_listbox.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

        self.mark_completed_button = ttk.Button(root, text="Mark Completed", command=self.mark_completed)
        self.mark_completed_button.grid(row=2, column=0, padx=10, pady=10)

        self.update_button = ttk.Button(root, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=1, padx=10, pady=10)

        self.remove_button = ttk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=2, padx=10, pady=10)

        self.todo_list = []
        self.completed_list = []

    def add_task(self):
        task_description = self.task_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_entry.get()

        if task_description:
            task = Task(task_description, due_date, priority)
            self.todo_list.append(task)
            self.update_task_listbox()
            self.clear_entry_fields()
            self.update_completed_listbox()

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.todo_list.pop(index)
            task.completed = True
            self.completed_list.append(task)
            self.update_task_listbox()
            self.update_completed_listbox()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.todo_list[index]

            task_description = self.task_entry.get()
            due_date = self.due_date_entry.get()
            priority = self.priority_entry.get()

            if task_description:
                task.description = task_description
            if due_date:
                task.due_date = due_date
            if priority:
                task.priority = priority

            self.update_task_listbox()
            self.clear_entry_fields()

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.todo_list[index]
            self.update_task_listbox()
            self.clear_entry_fields()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list:
            status = "Completed" if task.completed else "Pending"
            self.task_listbox.insert(tk.END, f"[{status}] {task.description} (Due: {task.due_date}, Priority: {task.priority})")

    def update_completed_listbox(self):
        self.completed_listbox.delete(0, tk.END)
        for task in self.completed_list:
            self.completed_listbox.insert(tk.END, f"[Completed] {task.description} (Due: {task.due_date}, Priority: {task.priority})")

    def clear_entry_fields(self):
        self.task_entry.delete(0, "end")
        self.due_date_entry.delete(0, "end")
        self.due_date_entry.insert(0, self.get_current_date())
        self.clear_priority(None)

    def get_current_date(self):
        current_date = datetime.now().strftime("%Y-%m-%d")
        return current_date

    def clear_priority(self, event):
        if self.priority_entry.get() == "Priority":
            self.priority_entry.delete(0, "end")

    def update_entry_fields(self, event):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.todo_list[index]
            self.task_entry.delete(0, "end")
            self.due_date_entry.delete(0, "end")
            self.priority_entry.delete(0, "end")
            self.task_entry.insert(0, task.description)
            self.due_date_entry.insert(0, task.due_date)
            self.priority_entry.insert(0, task.priority)

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
