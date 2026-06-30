# 📝 Console-Based To-Do List Application

A simple yet efficient **Command-Line To-Do List Manager** built with
**Python**. The application allows users to manage daily tasks through
an interactive console interface while ensuring data persistence by
storing tasks in a text file.

------------------------------------------------------------------------

## ✨ Features

-   ➕ Add new tasks
-   📋 View all tasks
-   ❌ Remove tasks
-   💾 Automatically save tasks to a text file
-   📂 Persistent storage using `tasks.txt`
-   🔄 Menu-driven interface
-   ✅ Input validation and error handling

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   **Language:** Python 3
-   **IDE:** Visual Studio Code (or any Python IDE)
-   **Storage:** Text File (`tasks.txt`)

------------------------------------------------------------------------

## 📂 Project Structure

``` text
ToDo-List/
│
├── todo.py
├── tasks.txt
└── README.md
```

------------------------------------------------------------------------

## 🚀 Getting Started

### Clone the Repository

``` bash
git clone https://github.com/your-username/ToDo-List.git
```

### Navigate to the Project Directory

``` bash
cd ToDo-List
```

### Run the Application

``` bash
python todo.py
```

------------------------------------------------------------------------

## 📋 Menu

``` text
========================================
        TO-DO LIST MANAGER
========================================
1. View Tasks
2. Add Task
3. Remove Task
4. Exit
========================================
```

------------------------------------------------------------------------

## 💻 Example

``` text
Choose an option (1-4): 2

Enter a new task:
Complete Python Assignment

Task added successfully.
```

``` text
Choose an option (1-4): 1

========================================
            YOUR TO-DO LIST
========================================
1. Complete Python Assignment
========================================
```

------------------------------------------------------------------------

## 💾 Data Persistence

All tasks are stored in **tasks.txt**. Every time a task is added or
removed, the file is updated automatically, ensuring your task list
remains available even after closing the application.

------------------------------------------------------------------------

## ⚠️ Error Handling

The application gracefully handles:

-   Invalid menu selections
-   Empty task entries
-   Invalid task numbers
-   Non-numeric input while removing tasks
-   Missing `tasks.txt` file (created automatically)

------------------------------------------------------------------------

## 🎯 Learning Objectives

This project demonstrates:

-   Python Functions
-   Lists
-   Loops
-   Conditional Statements
-   File Handling (`open()`)
-   Exception Handling
-   Input Validation
-   Modular Programming

------------------------------------------------------------------------

## 🚀 Future Enhancements

-   ✔️ Mark tasks as completed
-   📅 Add due dates
-   ⭐ Task priorities
-   🔍 Search tasks
-   ✏️ Edit tasks
-   🖥️ GUI version using Tkinter
-   🗃️ SQLite database integration

------------------------------------------------------------------------

## 👨‍💻 Author

**Himanshu Batra**

B.Tech Computer Science Engineering (Data Science & Machine Learning)

------------------------------------------------------------------------

## 📜 License

This project was developed for educational and internship assessment
purposes.
