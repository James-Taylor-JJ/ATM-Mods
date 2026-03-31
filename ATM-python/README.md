# ATM Machine – Python Edition

A Python port of the [ATM-Machine-Java](../ATM) project, providing identical features so that Python programmers can extend it just like Java students extend the original.

## Requirements

- Python 3.6 or higher (no third-party packages required)

## Running the Application

```bash
cd ATM-python
python atm.py
```

## Pre-loaded Test Accounts

| Customer Number | PIN    | Checking Balance | Savings Balance |
|-----------------|--------|-----------------|-----------------|
| 952141          | 191904 | $1,000.00       | $5,000.00       |
| 123             | 123    | $20,000.00      | $50,000.00      |

## Features

- **Login** with customer number and PIN
- **Create Account** with a new customer number and PIN
- **Checking Account**
  - View balance
  - Withdraw funds
  - Deposit funds
  - Transfer funds to Savings
- **Savings Account**
  - View balance
  - Withdraw funds
  - Deposit funds
  - Transfer funds to Checking
- Input validation with clear error messages
- Currency formatted as `$X,XXX.XX`

## Project Structure

```
ATM-python/
├── atm.py          # Entry point (mirrors ATM.java)
├── option_menu.py  # Menu system / UI controller (mirrors OptionMenu.java)
├── account.py      # Account data model (mirrors Account.java)
└── README.md       # This file
```

## Example Session

```
Welcome to the ATM Project!

 Type 1 - Login
 Type 2 - Create Account

Choice: 1

Enter your customer number: 123

Enter your PIN number: 123

Select the account you want to access:
 Type 1 - Checking Account
 Type 2 - Savings Account
 Type 3 - Exit

Choice: 1

Checking Account:
 Type 1 - View Balance
 Type 2 - Withdraw Funds
 Type 3 - Deposit Funds
 Type 4 - Transfer Funds
 Type 5 - Exit

Choice: 1

Checking Account Balance: $20,000.00
```
