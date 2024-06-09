package BankingSystem;
import java.util.InputMismatchException;
import java.util.Scanner;
public class Main {
    private static final Bank bank = new Account();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean exit = false;
        try{
        while (!exit) {
            System.out.println("\nSimple Banking System");
            System.out.println("1. Add a new account");
            System.out.println("2. Deposit money");
            System.out.println("3. Withdraw money");
            System.out.println("4. Check balance");
            System.out.println("5. Display details");
            System.out.println("6. Exit");
            System.out.print("Enter your choice: ");
            int choice = sc.nextInt();
            sc.nextLine(); // Consume the newline character

            switch (choice) {
                case 1:
                    addAccount(sc);
                    break;
                case 2:
                    deposit(sc);
                    break;
                case 3:
                    withdraw(sc);
                    break;
                case 4:
                    checkBalance(sc);
                    break;
                case 5:
                    display(sc);
                    break;
                    case 6:
                    exit = true;
                    System.out.println("Thank you for using sbu");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
        sc.close();
    }
    catch(InputMismatchException e)
    {
        System.out.println("Invalid input format. Please enter a valid numeric value.");
        sc.next();
    }
    }

    // Add a new account
    private static void addAccount(Scanner sc) {
        try{
        System.out.print("Enter the account holder's name: ");
        String name = sc.nextLine();
        System.out.print("Enter the initial deposit amount: ");
        double initialDeposit = sc.nextDouble();
        sc.nextLine(); // Consume the newline character

        String accountID = bank.addAccount(name, initialDeposit);
        System.out.println("Account created successfully. Account ID: " + accountID);
        }catch(InputMismatchException e)
        {
            System.out.println("Invalid input format. Please enter a valid numeric value.");
            sc.next();
        }
    }

    // Deposit money
    private static void deposit(Scanner sc) {
        try {
            System.out.print("Enter the account ID: ");
            String id = sc.nextLine();
            System.out.print("Enter the amount to deposit: ");
            double amount = sc.nextDouble();
            sc.nextLine(); // Consume the newline character

            if (bank.deposit(id, amount)) {
                System.out.println("Deposit successful.");
            } else {
                System.out.println("Account not found.");
            }
        } catch (Exception e) {
            // TODO Auto-generated catch block
            System.out.println("Invalid input format. Please enter a valid numeric value.");
            sc.next();
        }
    }

    // Withdraw money
    private static void withdraw(Scanner sc) {
        try {
            System.out.print("Enter the account ID: ");
            String id = sc.nextLine();
            System.out.print("Enter the amount to withdraw: ");
            double amount = sc.nextDouble();
            sc.nextLine(); // Consume the newline character

            if (bank.withdraw(id, amount)) {
                System.out.println("Withdrawal successful.");
            } else {
                System.out.println("Account not found or insufficient funds.");
            }
        } catch (Exception e) {
            // TODO Auto-generated catch block
            System.out.println("Invalid input format. Please enter a valid numeric value.");
        sc.next();
        }
    }

    // Check balance
    private static void checkBalance(Scanner sc) {
        try {
            System.out.print("Enter the account ID: ");
            String id = sc.nextLine();

            double balance = bank.getBalance(id);
            if (balance != -1) {
                System.out.println("The account balance is: " + balance);
            } else {
                System.out.println("Account not found.");
            }
        } catch (Exception e) {
            System.out.println("Invalid input format. Please enter a valid numeric value.");
        sc.next();
        }
    }
    //Display details
    private static void display(Scanner sc)
    {
        System.out.println("Enter the account ID: ");
        String id = sc.nextLine();
        bank.display(id);
    }
}

