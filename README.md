# 🚀 TrustChain - Transparent Welfare Distribution System

> **An AI-powered welfare distribution system that combines Machine Learning and Blockchain to make government welfare distribution more secure, transparent, and fraud-resistant.**

---

# 📖 Project Overview

Government welfare schemes such as scholarships, pensions, and subsidies are designed to support eligible citizens. However, traditional welfare distribution systems often face challenges related to fraud, transparency, and manual verification.

**TrustChain** is our proposed solution that leverages **Machine Learning**, **Blockchain**, and **Web Technologies** to create a secure, transparent, and efficient welfare distribution system.

---

# ❗ Problem Statement

Traditional welfare distribution systems face several challenges:

- ❌ Fake beneficiaries receiving government benefits
- ❌ Duplicate or multiple fraudulent claims
- ❌ Manual verification leading to delays and human errors
- ❌ Lack of transparency in fund distribution
- ❌ Difficulty tracking welfare transactions
- ❌ Possibility of record tampering in centralized databases
- ❌ Time-consuming beneficiary verification process

Because of these challenges, welfare benefits may not always reach the genuine beneficiaries, resulting in financial losses and reduced public trust.

---

# 💡 Our Solution

**TrustChain** addresses these problems by integrating modern technologies into a single platform.

The system combines:

- 🤖 **Machine Learning** for fraud detection
- ⛓️ **Blockchain** for secure and transparent transaction storage
- 🗄️ **MySQL** for beneficiary and scheme management
- 🌐 **Flask** backend with a responsive web interface
- 📋 **Rule-based eligibility verification** for welfare schemes

The system verifies beneficiaries using Aadhaar, checks eligibility according to government scheme rules, detects suspicious claim patterns using AI, stores approved transactions on Blockchain, and allows beneficiaries to track their applications using a unique Transaction Hash.

---

# ✨ Features

- ✅ Aadhaar-based Beneficiary Verification
- ✅ Multiple Government Welfare Schemes
- ✅ Rule-based Eligibility Verification
- ✅ Machine Learning-based Fraud Detection
- ✅ Blockchain Transaction Storage
- ✅ Unique Transaction Hash Generation
- ✅ Track Application Status
- ✅ Secure MySQL Database
- ✅ Transparent Welfare Distribution Process

---

# 🎯 Objectives

- Ensure welfare benefits reach genuine beneficiaries.
- Reduce fraudulent and duplicate claims.
- Improve transparency in welfare distribution.
- Secure transaction records using Blockchain.
- Detect suspicious beneficiary behavior using Machine Learning.
- Provide a simple way for beneficiaries to track their applications.

---

# 🏗️ System Architecture

![System Architecture](screenshots/system_architecture.png)

---

# 🔄 Project Workflow

1. User opens the TrustChain portal.
2. User selects a welfare scheme.
3. User enters their Aadhaar number.
4. System fetches beneficiary details from the database.
5. Rule-based eligibility verification is performed.
6. Machine Learning analyzes claim behavior for possible fraud.
7. If approved:
   - Transaction is recorded on Blockchain.
   - A unique Transaction Hash is generated.
   - Transaction details are stored in MySQL.
8. The user receives the Transaction Hash and can use it later to track the application status.

---

# 🤖 Machine Learning

### Algorithm Used

**Isolation Forest**

### Features Used

- Income
- Claim Count

### Purpose

The Isolation Forest algorithm detects suspicious beneficiary behavior by identifying applications that differ significantly from normal claim patterns.

Instead of requiring predefined fraud examples, the model learns normal beneficiary behavior and flags unusual applications for further verification.

---

# ⛓️ Blockchain Integration

### Blockchain Platform

- Ethereum Ganache

### Purpose

- Secure transaction storage
- Immutable transaction records
- Transparent verification
- Easy transaction tracking

Every approved transaction generates a unique **Transaction Hash**, which is stored in the database and can later be used to verify the application status.

---

# 🗄️ Database

The project uses **MySQL** to manage:

- Beneficiary Details
- Welfare Schemes
- Transaction Records

---

# 💻 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Flask | REST API Development |
| HTML | Frontend Structure |
| CSS | User Interface Design |
| JavaScript | Client-side Interaction |
| MySQL | Database Management |
| Isolation Forest | Fraud Detection |
| Ethereum Ganache | Blockchain Platform |
| Web3.py | Blockchain Integration |
| Git & GitHub | Version Control |

---

# 📸 Screenshots

## 🏠 Home Page

![Home](screenshots/home_page.png)

---

## 📝 Apply for Scheme

![Apply](screenshots/apply_page.png)

---

## ✅ Approval Result

![Approval](screenshots/approval_result.png)

---

## 🚨 Fraud Detection

![Fraud](screenshots/fraud_detection.png)

---

## 🔍 Track Application

![Tracking](screenshots/tracking_page.png)

---

## ⛓️ Blockchain Transaction

![Ganache](screenshots/ganache_transaction.png)

---

# 📂 Project Structure

```
TrustChain/
│
├── backend/
│   ├── app.py
│   ├── blockchain.py
│   ├── db.py
│   └── test_db.py
│
├── frontend/
│   ├── index.html
│   ├── apply.html
│   └── track.html
│
├── ml/
│   ├── train_model.py
│   └── model.pkl
│
├── screenshots/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/vamshitanniru245-cmyk/TrustChain-Welfare-System.git
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure MySQL

- Create the TrustChain database.
- Import the SQL tables.
- Update the database credentials in `backend/db.py`.

## Start Ganache

Launch Ganache on the default Ethereum test network.

## Run the Backend

```bash
cd backend
python app.py
```

## Run the Frontend

Open:

```
frontend/index.html
```

or use **VS Code Live Server**.

---

# 🚀 Future Scope

This project is a prototype developed to demonstrate how Machine Learning and Blockchain can improve welfare distribution. In the future, TrustChain can be enhanced with:

- Aadhaar API Integration
- Government Welfare Portal Integration
- Smart Contracts for automatic fund distribution
- Deployment on Ethereum Mainnet
- Mobile Application Support
- Advanced AI-based Fraud Detection Models
- SMS and Email Notifications
- Admin Dashboard with Analytics
- Multi-language Support
- Real-time Monitoring and Reporting

---

# 🌟 Our Vision

TrustChain is more than just a college project—it is **our idea to bring a positive change in the way government welfare benefits are distributed**.

We believe that technologies like **Machine Learning** and **Blockchain** have the potential to make welfare systems more transparent, secure, and trustworthy.

This project is **a prototype** created to demonstrate our concept. We understand that many improvements are possible, such as integrating official government services, deploying smart contracts, using more advanced AI models, and scaling the platform for real-world use.

Our goal was not to build the final product, but to present an innovative idea that can inspire future research and contribute towards building a transparent, efficient, and citizen-friendly digital welfare system.

---

# 👨‍💻 Team Members

- **Vamshi Tanniru**
- **Rahul Chinna**

---

# 📄 License

This project is developed for **academic and educational purposes only**.

---

## ⭐ Support

If you found this project interesting, please consider giving this repository a **⭐ Star**.

We welcome suggestions, feedback, and ideas for improving TrustChain in the future.