# Functional Requirement Document (FRD)

## Enterprise Banking Transaction Management System (EBTMS)

---

# Document Information

| Field            | Details                                          |
| ---------------- | ------------------------------------------------ |
| Project Name     | Enterprise Banking Transaction Management System |
| Version          | 1.0                                              |
| Document Type    | Functional Requirement Document (FRD)            |
| Prepared By      | Mohamed Tahir                                    |
| Date             | June 2026                                        |
| Technology Stack | FastAPI, PostgreSQL, React, Redis, Docker        |

---

# 1. Introduction

## 1.1 Purpose

The purpose of this document is to define the functional requirements of the Enterprise Banking Transaction Management System (EBTMS). The system enables customers and administrators to perform banking operations securely while maintaining data consistency, integrity, and auditability.

---

## 1.2 Scope

The system provides:

* Customer Registration
* User Authentication
* Bank Account Management
* Deposit and Withdrawal Operations
* Fund Transfers
* Transaction History
* Notifications
* Administrative Functions
* Audit Logging

---

# 2. System Objectives

The objectives of the system are:

1. Provide secure banking operations.
2. Maintain ACID-compliant transactions.
3. Prevent inconsistent account balances.
4. Provide complete transaction traceability.
5. Support concurrent transactions.
6. Provide administrative monitoring and reporting.

---

# 3. Stakeholders

| Stakeholder            | Responsibility                        |
| ---------------------- | ------------------------------------- |
| Customer               | Perform banking transactions          |
| Administrator          | Manage users and monitor transactions |
| Database Administrator | Maintain database performance         |
| System Administrator   | Maintain servers and deployment       |
| Developer              | Develop and maintain the application  |

---

# 4. User Roles

## Customer

* Register and login
* Manage profile
* Create account
* Deposit money
* Withdraw money
* Transfer money
* View transaction history

## Administrator

* View all customers
* Freeze accounts
* Activate accounts
* Generate reports
* View system logs

---

# 5. Functional Requirements

# Module 1: User Registration

## Description

Allows new customers to register in the system.

### Inputs

* Full Name
* Email Address
* Mobile Number
* Password
* Confirm Password

### Processing

* Validate email format
* Validate password strength
* Check duplicate email
* Encrypt password
* Save customer information

### Output

* Registration Successful
* Registration Failed

### Business Rules

* Email must be unique.
* Password length must be at least 8 characters.
* Mobile number must contain 10 digits.

---

# Module 2: User Login

## Description

Authenticate customers using email and password.

### Inputs

* Email
* Password

### Processing

* Validate credentials
* Generate JWT token
* Create user session

### Output

* Access Token
* Refresh Token

### Business Rules

* Account must be active.
* User gets locked after 5 failed login attempts.

---

# Module 3: Customer Profile Management

## Description

Allows customers to view and update personal information.

### Functions

* View Profile
* Update Mobile Number
* Change Password

### Business Rules

* Email cannot be modified.
* Password must satisfy security policies.

---

# Module 4: Bank Account Creation

## Description

Create a bank account for a customer.

### Inputs

* Account Type
* Initial Deposit

### Processing

* Generate account number
* Create account record
* Set initial balance

### Output

* Account Created Successfully

### Business Rules

* Initial deposit must be greater than ₹500.
* One customer can own multiple accounts.

---

# Module 5: Deposit Money

## Description

Allows customers to deposit money.

### Inputs

* Account Number
* Amount

### Processing

* Validate account
* Update balance
* Record transaction
* Generate notification

### Output

* Deposit Successful

### Business Rules

* Deposit amount must be greater than zero.

---

# Module 6: Withdraw Money

## Description

Allows customers to withdraw money.

### Inputs

* Account Number
* Amount

### Processing

* Verify account status
* Verify available balance
* Update account balance
* Save transaction

### Output

* Withdrawal Successful

### Business Rules

* Balance cannot become negative.
* Minimum balance of ₹500 must be maintained.

---

# Module 7: Fund Transfer

## Description

Transfer money between accounts.

### Inputs

* Sender Account
* Receiver Account
* Amount

### Processing

1. Validate sender account.
2. Validate receiver account.
3. Verify sufficient balance.
4. Deduct amount from sender.
5. Credit receiver.
6. Create transaction records.
7. Send notifications.

### Output

* Transfer Successful
* Transfer Failed

### Business Rules

* Transfer amount must be greater than zero.
* Sender and receiver cannot be the same account.
* Both accounts must be active.

---

# Module 8: Transaction History

## Description

Display account transactions.

### Functions

* View Deposits
* View Withdrawals
* View Transfers
* Filter by Date

### Output

Transaction details including:

* Transaction ID
* Date
* Amount
* Status
* Transaction Type

---

# Module 9: Notifications

## Description

Notify customers about banking activities.

### Notification Types

* Deposit Notification
* Withdrawal Notification
* Transfer Notification
* Password Change Notification

---

# Module 10: Audit Logging

## Description

Maintain logs of critical activities.

### Events Logged

* Login
* Logout
* Account Creation
* Deposits
* Withdrawals
* Transfers
* Password Changes

---

# Module 11: Administrative Functions

## Description

Provides administrative capabilities.

### Features

* View Customers
* Search Customers
* Freeze Accounts
* Activate Accounts
* Generate Reports
* View Audit Logs

---

# 6. Functional Requirements Table

| Requirement ID | Requirement              |
| -------------- | ------------------------ |
| FR-001         | User Registration        |
| FR-002         | User Login               |
| FR-003         | Profile Management       |
| FR-004         | Create Bank Account      |
| FR-005         | Deposit Money            |
| FR-006         | Withdraw Money           |
| FR-007         | Transfer Money           |
| FR-008         | View Transaction History |
| FR-009         | Notification Management  |
| FR-010         | Audit Logging            |
| FR-011         | Admin Dashboard          |
| FR-012         | Generate Reports         |

---

# 7. Validation Rules

| Field             | Validation           |
| ----------------- | -------------------- |
| Email             | Must be unique       |
| Password          | Minimum 8 characters |
| Phone Number      | Exactly 10 digits    |
| Deposit Amount    | Greater than zero    |
| Withdrawal Amount | Greater than zero    |
| Transfer Amount   | Greater than zero    |
| Initial Deposit   | Minimum ₹500         |

---

# 8. Error Handling Requirements

| Error Code | Description             |
| ---------- | ----------------------- |
| ERR-001    | Invalid Credentials     |
| ERR-002    | Account Not Found       |
| ERR-003    | Insufficient Balance    |
| ERR-004    | Account Frozen          |
| ERR-005    | Duplicate Email         |
| ERR-006    | Invalid Transfer Amount |
| ERR-007    | Internal Server Error   |

---

# 9. Reports

The system shall provide:

1. Customer Report
2. Transaction Report
3. Daily Deposit Report
4. Daily Withdrawal Report
5. Fund Transfer Report
6. Audit Log Report

---

# 10. Assumptions and Dependencies

* PostgreSQL database is available.
* Email service is configured.
* Redis cache is available.
* Internet connection is available.
* JWT authentication service is operational.

---

# 11. Acceptance Criteria

The system shall:

* Successfully register customers.
* Authenticate users securely.
* Maintain ACID properties.
* Process deposits and withdrawals correctly.
* Complete fund transfers without inconsistencies.
* Generate transaction history accurately.
* Maintain complete audit logs.
* Support concurrent transactions safely.

---

