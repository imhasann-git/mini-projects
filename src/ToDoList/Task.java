package ToDoList;
import java.util.*;
public class Task {
    ArrayList<String> TaskName;
    ArrayList<String> dueDate;
    String[] priority;
    int index ;
    public Task()
    {
        TaskName = new ArrayList<>();
        dueDate = new ArrayList<>();
        priority = new String[4];
        index = 0;
        setPriorities();
    }
    //priority levels
    void setPriorities()
    {
        priority[0] = "urgent";
        priority[1] = "high";
        priority[2] = "needs attention";
        priority[3] = "bhool ja sakta hai";

    }
    void viewPriority()
    {
        System.out.println("Priority Level's : ");
        for (int i = 0; i < priority.length; i++) {
            System.out.println((i+1) + " " +  priority[i]);
        }
    }
}
