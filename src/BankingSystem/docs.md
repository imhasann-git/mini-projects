# Banking System Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Account Class](#account-class)
3. [Bank Interface](#bank-interface)
4. [Main Class](#main-class)
5. [Usage](#usage)
6. [Error Handling](#error-handling)
7. [Summary](#summary)

## Introduction
This simple banking system provides functionalities for creating accounts, depositing and withdrawing money, checking balances, and displaying account details. The system is implemented using three main components:
- `Account` class
- `Bank` interface
- `Main` class

## Account Class
The `Account` class implements the `Bank` interface and manages account data including account IDs, names, and balances.

### Attributes
- `ids`: ArrayList<String> - Stores account IDs.
- `names`: ArrayList<String> - Stores account holder names.
- `balances`: ArrayList<Double> - Stores account balances.
- `accountCnt`: static int - Counts the number of accounts created.
- `r`: Random - Random number generator for creating account IDs.

### Methods
- **Constructor**: Initializes the attributes.
  ```java
  public Account()
  ```

- **createID(String name)**: Creates a unique account ID.
  ```java
  public String createID(String name)
  ```

- **addAccount(String name, double initialDeposit)**: Adds a new account and returns the account ID.
  ```java
  public String addAccount(String name, double initialDeposit)
  ```

- **deposit(String id, double amount)**: Deposits money into the specified account. Returns true if successful, otherwise false.
  ```java
  public boolean deposit(String id, double amount)
  ```

- **withdraw(String id, double amount)**: Withdraws money from the specified account. Returns true if successful, otherwise false.
  ```java
  public boolean withdraw(String id, double amount)
  ```

- **getBalance(String id)**: Returns the balance of the specified account. Returns -1 if the account is not found.
  ```java
  public double getBalance(String id)
  ```

- **display(String ID)**: Displays the details of the specified account.
  ```java
  public void display(String ID)
  ```

## Bank Interface
The `Bank` interface defines the contract for the banking operations.

### Methods
- **addAccount(String name, double initialDeposit)**: Adds a new account and returns the account ID.
  ```java
  String addAccount(String name, double initialDeposit);
  ```

- **deposit(String id, double amount)**: Deposits money into the specified account.
  ```java
  boolean deposit(String id, double amount);
  ```

- **withdraw(String id, double amount)**: Withdraws money from the specified account.
  ```java
  boolean withdraw(String id, double amount);
  ```

- **getBalance(String id)**: Gets the balance of the specified account.
  ```java
  double getBalance(String id);
  ```

- **display(String ID)**: Displays the details of the specified account.
  ```java
  void display(String ID);
  ```

## Main Class
The `Main` class contains the entry point for the banking system and provides a user interface for interacting with the system.

### Attributes
- `bank`: static Bank - An instance of the `Account` class.

### Methods
- **main(String[] args)**: The main method that runs the banking system.
  ```java
  public static void main(String[] args)
  ```

- **addAccount(Scanner sc)**: Prompts the user to add a new account.
  ```java
  private static void addAccount(Scanner sc)
  ```

- **deposit(Scanner sc)**: Prompts the user to deposit money into an account.
  ```java
  private static void deposit(Scanner sc)
  ```

- **withdraw(Scanner sc)**: Prompts the user to withdraw money from an account.
  ```java
  private static void withdraw(Scanner sc)
  ```

- **checkBalance(Scanner sc)**: Prompts the user to check the balance of an account.
  ```java
  private static void checkBalance(Scanner sc)
  ```

- **display(Scanner sc)**: Prompts the user to display the details of an account.
  ```java
  private static void display(Scanner sc)
  ```

## Usage
1. **Running the System**:
    - Compile and run the `Main` class.
    - Follow the on-screen prompts to interact with the system.

2. **Options**:
    - Add a new account: Enter the account holder's name and the initial deposit amount.
    - Deposit money: Enter the account ID and the amount to deposit.
    - Withdraw money: Enter the account ID and the amount to withdraw.
    - Check balance: Enter the account ID to view the balance.
    - Display details: Enter the account ID to view account details.

## Error Handling
- Input validation is performed for numeric values to ensure proper data entry.
- If invalid input is detected, an error message is displayed and the user is prompted to enter the input again.

## Summary
This simple banking system provides basic functionalities for managing bank accounts, including creating accounts, depositing and withdrawing money, checking balances, and displaying account details. The `Account` class implements the `Bank` interface, while the `Main` class provides a user-friendly interface for interacting with the system. Error handling is implemented to manage invalid inputs gracefully.