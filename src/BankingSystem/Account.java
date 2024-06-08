package BankingSystem;

public class Account {
<<<<<<< HEAD
    
}
=======
    // Account balance
    private double balance;
    private String accHolderName;
    private String accNum;
    public Account(double bal, String name,String accNumber)
    {
        this.balance = bal;
        this.accHolderName = name;
        this.accNum = accNumber;
    }
    //getter to get all this data
    public String getAccNumber() {
        return accNum;
    }

    public String getAccHolderName() {
        return accHolderName;
    }

    public double getBalance() {
        return balance;
    }
    //methods to deposit,withdraw and check account balance.
    public void deposit(double amt)
    {
        balance +=amt;
        System.out.println("Successfully deposited the amount");
    }
    public boolean withdraw(double amt)
    {
        if(amt <= balance)
        {
            balance -= amt;
            System.out.println("Successfully withdrew the money.");
            return true;
        } else 
        {
            System.out.println("insufficient funds");
            return false;
        }
    }
    public void checkBalance()
    {
        System.out.println("Account Number: " + accNum);
        System.out.println("Account Holder Name: " + accHolderName);
        System.out.println("Balance: $" + balance);
    }
}
>>>>>>> b7720f3947bbbab843559692d22edb84b25ba385
