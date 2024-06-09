package BankingSystem;

public interface Bank {
    String addAccount(String name, double initialDeposit);
    boolean deposit(String id, double amount);
    boolean withdraw(String id, double amount);
    double getBalance(String id);
    void display(String ID);
    void sendMoney(String ID);
}
