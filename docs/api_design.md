# API Design Document (api_design.md)

# Project

Enterprise Banking Transaction Management System

Version: 1.0

Architecture Style: REST API

Communication Protocol: HTTPS

Data Format: JSON

Authentication: JWT (Access Token + Refresh Token)

---

# Base URL

## Development

```text
http://localhost:8000/api/v1
```

## Production

```text
https://api.bankingsystem.com/api/v1
```

---

# API Standards

## HTTP Methods

| Method | Purpose         |
| ------ | --------------- |
| GET    | Fetch Data      |
| POST   | Create Resource |
| PUT    | Update Resource |
| PATCH  | Partial Update  |
| DELETE | Delete Resource |

---

# Standard Response Format

## Success Response

```json
{
  "success": true,
  "message": "Operation completed successfully",
  "data": {},
  "timestamp": "2026-06-22T10:00:00Z"
}
```

---

## Error Response

```json
{
  "success": false,
  "message": "Insufficient balance",
  "error_code": "INSUFFICIENT_FUNDS",
  "timestamp": "2026-06-22T10:00:00Z"
}
```

---

# Authentication APIs

---

# Register Customer

## Endpoint

```http
POST /auth/register
```

## Request

```json
{
  "full_name": "Mohamed Tahir",
  "email": "tahir@gmail.com",
  "phone": "9876543210",
  "password": "Password@123"
}
```

## Response

```json
{
  "success": true,
  "message": "Customer registered successfully"
}
```

---

# Login

## Endpoint

```http
POST /auth/login
```

## Request

```json
{
  "email": "tahir@gmail.com",
  "password": "Password@123"
}
```

## Response

```json
{
  "access_token": "jwt_token",
  "refresh_token": "refresh_token",
  "token_type": "Bearer"
}
```

---

# Refresh Token

## Endpoint

```http
POST /auth/refresh
```

---

# Logout

## Endpoint

```http
POST /auth/logout
```

---

# Customer APIs

---

# Get Profile

## Endpoint

```http
GET /customers/profile
```

## Headers

```http
Authorization: Bearer <token>
```

## Response

```json
{
  "customer_id": 1,
  "full_name": "Mohamed Tahir",
  "email": "tahir@gmail.com",
  "phone": "9876543210"
}
```

---

# Update Profile

## Endpoint

```http
PUT /customers/profile
```

## Request

```json
{
  "full_name": "Mohamed Tahir",
  "phone": "9999999999"
}
```

---

# Account APIs

---

# Create Bank Account

## Endpoint

```http
POST /accounts
```

## Request

```json
{
  "account_type": "SAVINGS",
  "initial_balance": 5000
}
```

## Response

```json
{
  "account_number": "SB100001",
  "balance": 5000,
  "status": "ACTIVE"
}
```

---

# Get Account Details

## Endpoint

```http
GET /accounts/{account_id}
```

---

# Get All Accounts

## Endpoint

```http
GET /accounts
```

---

# Deposit Money

## Endpoint

```http
POST /accounts/deposit
```

## Request

```json
{
  "account_number": "SB100001",
  "amount": 1000
}
```

---

# Withdraw Money

## Endpoint

```http
POST /accounts/withdraw
```

## Request

```json
{
  "account_number": "SB100001",
  "amount": 500
}
```

---

# Fund Transfer

## Endpoint

```http
POST /accounts/transfer
```

## Request

```json
{
  "sender_account": "SB100001",
  "receiver_account": "SB100002",
  "amount": 1000,
  "remarks": "Rent Payment"
}
```

## Response

```json
{
  "transaction_id": 1201,
  "status": "SUCCESS",
  "amount": 1000
}
```

---

# Transaction APIs

---

# Get Transaction History

## Endpoint

```http
GET /transactions
```

## Query Parameters

```text
?page=1
&size=10
&sort=date
```

---

# Get Transaction By ID

## Endpoint

```http
GET /transactions/{transaction_id}
```

---

# Filter Transactions

## Endpoint

```http
GET /transactions/filter
```

## Query Parameters

```text
?start_date=2026-01-01
&end_date=2026-06-22
&type=TRANSFER
```

---

# Download Statement

## Endpoint

```http
GET /transactions/statement
```

---

# Notification APIs

---

# Get Notifications

## Endpoint

```http
GET /notifications
```

---

# Mark Notification As Read

## Endpoint

```http
PUT /notifications/{id}
```

---

# Admin APIs

---

# Get All Customers

## Endpoint

```http
GET /admin/customers
```

---

# Get Customer By ID

## Endpoint

```http
GET /admin/customers/{customer_id}
```

---

# Freeze Account

## Endpoint

```http
PUT /admin/accounts/freeze/{account_id}
```

---

# Unfreeze Account

## Endpoint

```http
PUT /admin/accounts/unfreeze/{account_id}
```

---

# Close Account

## Endpoint

```http
PUT /admin/accounts/close/{account_id}
```

---

# Dashboard Statistics

## Endpoint

```http
GET /admin/dashboard
```

## Response

```json
{
  "total_customers": 1000,
  "total_accounts": 1200,
  "total_transactions": 25000,
  "total_balance": 5000000
}
```

---

# Audit APIs

---

# Get Audit Logs

## Endpoint

```http
GET /admin/audit-logs
```

---

# Reports APIs

---

# Daily Transactions Report

## Endpoint

```http
GET /reports/daily-transactions
```

---

# Monthly Revenue Report

## Endpoint

```http
GET /reports/monthly-revenue
```

---

# Customer Activity Report

## Endpoint

```http
GET /reports/customer-activity
```

---

# Health Check APIs

---

# Health Status

## Endpoint

```http
GET /health
```

## Response

```json
{
  "status": "UP",
  "database": "UP",
  "redis": "UP"
}
```

---

# HTTP Status Codes

| Status | Description           |
| ------ | --------------------- |
| 200    | Success               |
| 201    | Created               |
| 400    | Bad Request           |
| 401    | Unauthorized          |
| 403    | Forbidden             |
| 404    | Not Found             |
| 409    | Conflict              |
| 422    | Validation Error      |
| 500    | Internal Server Error |

---

# Error Codes

| Error Code          | Description          |
| ------------------- | -------------------- |
| INVALID_CREDENTIALS | Login Failed         |
| ACCOUNT_NOT_FOUND   | Invalid Account      |
| ACCOUNT_FROZEN      | Account Frozen       |
| INSUFFICIENT_FUNDS  | Balance Low          |
| TRANSACTION_FAILED  | Transfer Failed      |
| DUPLICATE_EMAIL     | Email Already Exists |
| INVALID_TOKEN       | JWT Invalid          |

---

# API Security

* HTTPS Enabled
* JWT Authentication
* Password Hashing using BCrypt
* Rate Limiting
* Input Validation
* SQL Injection Prevention
* CORS Configuration
* Role-Based Access Control

---

# API Versioning Strategy

```text
/api/v1/
/api/v2/
```

---

# Pagination Format

```json
{
  "page": 1,
  "size": 10,
  "total_pages": 20,
  "total_records": 200,
  "data": []
}
```

---

# API Flow

```text
Client
   ↓
API Gateway
   ↓
Authentication Middleware
   ↓
Controller
   ↓
Service Layer
   ↓
Repository Layer
   ↓
PostgreSQL
   ↓
Response
```

---

# Production Features

✓ JWT Authentication

✓ Role-Based Authorization

✓ Transaction Management

✓ Audit Logging

✓ Pagination

✓ Input Validation

✓ Rate Limiting

✓ Health Checks

✓ API Versioning

✓ Standardized Error Handling

✓ Monitoring and Logging
