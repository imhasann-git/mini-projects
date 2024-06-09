package BankingSystem;
import java.util.ArrayList;
import java.util.*;
class Account implements  Bank {
    private final ArrayList<String> ids;
    private final ArrayList<String>  names;
    private final ArrayList<Double> balances;
    private static int accountCnt;
    Random r = new Random();
    // Constructor
    public Account() {
        ids = new ArrayList<>();
        names = new ArrayList<>();
        balances = new ArrayList<>();
        accountCnt = 0;
    }

    // ID creator
    public String createID(String name) {
        int R = r.nextInt(1000);
        String id = String.format("%05d%05d", R,++accountCnt);
        id = name + id;
        return id;
    }

    // Add a new account
    @Override
    public String addAccount(String name, double initialDeposit) {
        String id = createID(name);
        ids.add(id);
        names.add(name);
        balances.add(initialDeposit);
        return id;
    }

    // Deposit money into an account
    @Override
    public boolean deposit(String id, double amount) {
        int index = ids.indexOf(id);
        if (index != -1) {
            balances.set(index, balances.get(index) + amount);
            return true;
        }
        return false;
    }

    // Withdraw money from an account
    @Override
    public boolean withdraw(String id, double amount) {
        int index = ids.indexOf(id);
        if (index != -1 && balances.get(index) >= amount) {
            balances.set(index, balances.get(index) - amount);
            return true;
        }
        return false;
    }

    // Get the balance of an account
    @Override
    public double getBalance(String id) {
        int index = ids.indexOf(id);
        if (index != -1) {
            return balances.get(index);
        }
        return -1; // Return -1 to indicate account not found
    }
    @Override
    public void display(String ID)
    {
        int index = ids.indexOf(ID);
        if(index != - 1)
        {
            System.out.println("Details : ");
            System.out.println("Account Name : " + names.get(index));
            System.out.println("Available Balance : " + balances.get(index));
        } else{
            System.out.println("Account not exist.");
        }
    }
    //will use to send money to different accounts
    @Override
    public boolean sendMoney(String SenderID,String RID,double amt)
    {
        int index = ids.indexOf(SenderID);
        boolean isAvailable = false;
        if(index != -1)
        {
            isAvailable = true;
        } else {
            isAvailable = false;
        }
        return isAvailable;
    }
}
