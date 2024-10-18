# ToDoList Program Documentation
---

## Overview

The ToDoList program is a simple command-line application to manage tasks with assigned priority levels. Users can add, view, delete, and edit tasks.

## Classes and Their Functions

### Main Class

This class contains the main method which provides the user interface for interacting with the program.

- **main**: The entry point of the application. It presents a menu to the user and performs actions based on user input.

### Task Class

This class represents a task and contains properties for storing task names and their priorities.

- **Task**: Constructor initializes the task list and priority levels.
- **Priority**: Method to initialize priority levels.
- **viewPriority**: Method to display available priority levels.

### TaskManagement Class

This class handles the core functionality of adding, viewing, deleting, and editing tasks.

- **addTask**: Adds a new task with a specified priority.
- **viewTask**: Displays the list of all tasks with their priorities.
- **deleteTask**: Deletes a specified task.
- **editTask**: Edits the name or priority of a specified task.

## How to Run the Program

1. **Ensure you have Java installed**: Make sure Java is installed on your system. You can download it from [Java's official website](https://www.oracle.com/java/technologies/javase-downloads.html).

2. **Compile the Program**:
    - Open your terminal or command prompt.
    - Navigate to the directory where the source files are located.
    - Run the following command to compile all the Java files:
      ```
      javac ToDoList/*.java
      ```

3. **Run the Program**:
    - After successful compilation, run the `Main` class using the following command:
      ```
      java ToDoList.Main
      ```

## Example Usage

When you run the program, you will see a menu like this:

```
Menu :
1. Add Task
2. View Tasks
3. Delete Task
4. Edit Task
5. Exit
Choose an option:
```

You can select an option by entering the corresponding number and following the prompts to add, view, delete, or edit tasks.

## Contact Information

If you have any questions or need further assistance, you can reach out to me via Twitter or email.

- **Twitter**: [@Naumanxaim0](https://x.com/9manhasan_)
- **Email**: workwithnauman@gmail.com

---
