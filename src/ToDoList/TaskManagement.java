package ToDoList;

import java.util.InputMismatchException;
import java.util.Scanner;

public class TaskManagement {
    String[] p = new String[100];
    Task t = new Task();
    Scanner sc = new Scanner(System.in);
    //will use array list to store task name and a new array p to store its priority level.
    void addTask()
    {
        try{
            System.out.println("Task name : ");
            String name = sc.nextLine().trim();
            if(name.isEmpty())
            {
                System.out.println("Name cannot be empty, try again.");
                return;
            }
            System.out.println("Due date (dd-MM-yyyy): ");
            String dueDate = sc.nextLine().trim();
            if (dueDate.isEmpty()) {
                System.out.println("Due date cannot be empty, try again.");
                return;
            }
            t.dueDate.add(dueDate);
            t.TaskName.add(name);
            t.viewPriority();
            System.out.println("enter the priority number  here : ");
            int i = sc.nextInt() - 1;
            sc.nextLine();
            if(i < 0 || i >= t.priority.length) {
                System.out.println("Invalid priority number.");
                return;
            }
            p[t.index] = t.priority[i];
            t.index++;
            System.out.println("Task added successfully..");
        }catch (InputMismatchException e)
        {
            System.out.println("invalid data entered.");
            sc.next();
        }
    }
    //use to delete task by deleting its array list index and string p index 
    void deleteTask()
    {
        if (t.TaskName.size() == 0) {
            System.out.println("No task has been added.");
            return;
        }
        viewTask();
        try{
        System.out.println("Enter the task number you want to delete it.");
        int op = sc.nextInt() - 1;
        sc.nextLine();
        if (op < 0 || op >= t.TaskName.size()) {
            System.out.println("Invalid task number.");
            return;
        }
        t.TaskName.remove(op);
        t.dueDate.remove(op);
        for (int i = op; i < t.index - 1; i++) {
            p[i] = p[i + 1];
        }
        p[t.index - 1] = null;
        t.index--;
        System.out.println("Task removed successfully.");
        }catch(InputMismatchException e)
        {
            System.out.println("Invalid data type, try again.");
            sc.next();
        }
    }
    //use to view task by simply printing it.
    void viewTask()
    {
        if(t.TaskName.size() == 0)
        {
            System.out.println("No task has added.");
            return;
        }
        for (int i = 0; i < t.TaskName.size(); i++) {
            System.out.println((i + 1) + " Name: " + t.TaskName.get(i) + " Priority: " + p[i] + " Due Date: " + t.dueDate.get(i));
        }
    }
    //use to edit task.
    void editTask()
    {
        viewTask();
        if(t.TaskName.size() == 0)
        {
            System.out.println("No task has been added.");
            return;
        }
        try{
            System.out.println("Enter the task number you want to edit.");
        int index = sc.nextInt()-1;
        sc.nextLine();
        if (index < 0 || index >= t.TaskName.size()) {
            System.out.println("Invalid task number.");
            return;
        }
        System.out.println("What do you want to edit ?");
        System.out.println("1. Name.");
        System.out.println("2. priority.");
        System.out.println("3. Due Date");
        int op =  sc.nextInt();
        sc.nextLine();
        if(op == 1)
        {
         System.out.println("Change the name here : ");
        String name = sc.nextLine();
        if (name.isEmpty()) {
            System.out.println("Name cannot be empty, try again.");
            return;
        }
        t.TaskName.set(op,name);
        System.out.println("Name changed.");
        } else if(op == 2)
        {
            t.viewPriority();
            System.out.println("select the level you want to change it to.");
            int pLevel = sc.nextInt() - 1;
            sc.nextLine();
            if (pLevel < 0 || pLevel >= t.priority.length) {
                System.out.println("Invalid priority number.");
                return;
            }
            p[index] = t.priority[pLevel];
        }
        else if (op == 3) {
            System.out.println("Enter the new due date (dd-MM-yyyy): ");
            String dueDate = sc.nextLine();
            if (dueDate.isEmpty()) {
                System.out.println("Due date cannot be empty, try again.");
                return;
            }
            t.dueDate.set(index, dueDate);
            System.out.println("Due date changed.");
        }else {
            System.out.println("Invalid option, try again.");
        }
        }catch(InputMismatchException e)
        {
            System.out.println("Invalid data type, try again");
            sc.next();
        }
    }
}
