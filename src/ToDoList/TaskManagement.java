package ToDoList;

import java.util.InputMismatchException;
import java.util.Scanner;

public class TaskManagement {
    String[] p = new String[100];
    Task t = new Task();
    Scanner sc = new Scanner(System.in);
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
            System.out.println("enter the date here : ");
            t.index++;
            System.out.println("Task and added successfully..");
        }catch (InputMismatchException e)
        {
            System.out.println("invalid data entered.");
            sc.next();
        }
    }
    void viewTask()
    {
        if(t.TaskName.size() == 0)
        {
            System.out.println("No task has added.");
            return;
        }
        for (int i = 0; i < t.TaskName.size(); i++) {
            System.out.println((i+1) + "Name : " + t.TaskName.get(i) + " Priority : " + p[i]);
        }
    }
}
