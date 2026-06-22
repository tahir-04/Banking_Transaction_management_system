# Banking Transaction Management System

## Use Case Document (UCD)

**Project Name:** Enterprise Banking Transaction Management System
**Version:** 1.0
**Prepared By:** Mohamed Tahir
**Date:** June 2026

---

# 1. Introduction

## Purpose

This document describes all the use cases of the Banking Transaction Management System. It defines how different users interact with the system and outlines the expected behavior of the application.

## Scope

The system allows customers to perform banking operations digitally while enabling administrators to manage customers, accounts, and monitor transactions securely.

---

# 2. Actors

| Actor                | Description                                                                  |
| -------------------- | ---------------------------------------------------------------------------- |
| Customer             | Registered user who performs banking operations.                             |
| Admin                | Bank employee responsible for managing accounts and monitoring transactions. |
| Notification Service | Sends email or SMS notifications to customers.                               |
| Database System      | Stores and manages all banking data.                                         |

---

# 3. Use Case Diagram (Text Representation)

```text
Customer
│
├── Register
├── Login
├── View Profile
├── Create Account
├── Deposit Money
├── Withdraw Money
├── Transfer Money
├── View Balance
├── View Transaction History
└── Logout

Admin
│
├── Login
├── View Customers
├── Approve Account
├── Freeze Account
├── Unfreeze Account
├── View Transactions
└── Generate Reports
```

---

# UC-01: Customer Registration

## Description

Allows a new customer to create an account in the banking system.

## Primary Actor

Customer

## Preconditions

* Customer is not already registered.

## Postconditions

* Customer account is created successfully.

## Main Flow

1. Customer opens registration page.
2. Customer enters personal details.
3. System validates input.
4. System checks for duplicate email.
5. System saves customer information.
6. System displays registration success message.

## Alternative Flow

* Email already exists.
* Invalid input data.

## Exceptions

* Database failure.

---

# UC-02: Customer Login

## Description

Allows customers to log in to the system.

## Primary Actor

Customer

## Preconditions

* Customer account exists.

## Postconditions

* JWT token generated.
* User session created.

## Main Flow

1. Enter email and password.
2. System validates credentials.
3. System generates access token.
4. Dashboard is displayed.

## Alternative Flow

* Incorrect password.
* Account is blocked.

## Exceptions

* Database unavailable.

---

# UC-03: View Profile

## Description

Customer can view personal information.

## Primary Actor

Customer

## Preconditions

* User is logged in.

## Postconditions

* Customer information displayed.

## Main Flow

1. Login.
2. Click Profile.
3. System fetches customer details.
4. Display profile information.

---

# UC-04: Create Bank Account

## Description

Customer creates a savings or current account.

## Primary Actor

Customer

## Preconditions

* User is registered.
* User is logged in.

## Postconditions

* New account created.

## Main Flow

1. Select account type.
2. Submit request.
3. System generates account number.
4. Account is created.

## Alternative Flow

* Customer already has maximum allowed accounts.

---

# UC-05: Deposit Money

## Description

Customer deposits money into an account.

## Primary Actor

Customer

## Preconditions

* Account is active.

## Postconditions

* Balance updated.
* Transaction recorded.

## Main Flow

1. Select account.
2. Enter amount.
3. Validate amount.
4. Update balance.
5. Record transaction.
6. Send notification.

## Alternative Flow

* Invalid amount.

## Exceptions

* Database failure.

---

# UC-06: Withdraw Money

## Description

Customer withdraws money from an account.

## Primary Actor

Customer

## Preconditions

* Account is active.
* Sufficient balance exists.

## Postconditions

* Balance reduced.
* Transaction recorded.

## Main Flow

1. Select account.
2. Enter withdrawal amount.
3. Validate balance.
4. Deduct amount.
5. Save transaction.
6. Send notification.

## Alternative Flow

* Insufficient funds.

## Exceptions

* Database error.

---

# UC-07: Transfer Money

## Description

Customer transfers money to another account.

## Primary Actor

Customer

## Preconditions

* Sender account exists.
* Receiver account exists.
* Sufficient balance available.

## Postconditions

* Sender balance deducted.
* Receiver balance credited.
* Transaction recorded.

## Main Flow

1. Enter receiver account number.
2. Enter transfer amount.
3. Validate sender balance.
4. Lock sender account.
5. Deduct amount.
6. Credit receiver account.
7. Save transaction record.
8. Commit transaction.
9. Send notification.

## Alternative Flow

* Invalid receiver account.
* Insufficient funds.

## Exceptions

* Database failure.
* Transaction rollback.

---

# UC-08: View Account Balance

## Description

Customer checks current account balance.

## Primary Actor

Customer

## Preconditions

* User logged in.

## Postconditions

* Current balance displayed.

## Main Flow

1. Select account.
2. System fetches balance.
3. Display balance.

---

# UC-09: View Transaction History

## Description

Customer views previous transactions.

## Primary Actor

Customer

## Preconditions

* User logged in.

## Postconditions

* Transaction list displayed.

## Main Flow

1. Select account.
2. System retrieves transactions.
3. Display transaction history.

---

# UC-10: Logout

## Description

Customer ends current session.

## Primary Actor

Customer

## Preconditions

* User logged in.

## Postconditions

* Session terminated.

## Main Flow

1. Click logout.
2. Token invalidated.
3. Redirect to login page.

---

# UC-11: Admin Login

## Description

Administrator logs into the system.

## Primary Actor

Admin

## Preconditions

* Admin account exists.

## Postconditions

* Admin dashboard displayed.

---

# UC-12: View Customers

## Description

Admin views all registered customers.

## Primary Actor

Admin

## Preconditions

* Admin logged in.

## Postconditions

* Customer list displayed.

---

# UC-13: Freeze Account

## Description

Admin freezes suspicious accounts.

## Primary Actor

Admin

## Preconditions

* Account exists.

## Postconditions

* Account status changed to Frozen.

## Main Flow

1. Search account.
2. Select Freeze.
3. Update account status.
4. Notify customer.

---

# UC-14: Unfreeze Account

## Description

Admin activates frozen accounts.

## Primary Actor

Admin

## Preconditions

* Account is frozen.

## Postconditions

* Account status changed to Active.

---

# UC-15: Generate Reports

## Description

Admin generates banking reports.

## Primary Actor

Admin

## Reports

* Total Customers
* Total Accounts
* Daily Transactions
* Failed Transactions
* Account Status Report
* Revenue Report

---

# UC-16: Notification Service

## Description

System sends notifications after transactions.

## Primary Actor

Notification Service

## Triggers

* Registration successful.
* Deposit successful.
* Withdrawal successful.
* Money transfer successful.
* Account frozen.

---

# Business Rules

BR-01: Account number must be unique.

BR-02: Balance cannot become negative.

BR-03: Transfer amount must be greater than zero.

BR-04: Frozen accounts cannot perform transactions.

BR-05: Transactions cannot be deleted.

BR-06: Every transaction must be logged.

BR-07: All financial operations must satisfy ACID properties.

---

# Non-Functional Requirements

* Authentication: JWT
* Password Encryption: BCrypt
* Availability: 99.9%
* Response Time: < 2 seconds
* Concurrent Users: 1000+
* Audit Logging: Enabled
* Database Backup: Daily

---
