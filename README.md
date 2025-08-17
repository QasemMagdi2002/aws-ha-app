# AWS Cloud Infrastructure Project – Secure & Scalable Web App

This project demonstrates a **production-grade AWS architecture** with compute, storage, networking, CI/CD, monitoring, and DevSecOps practices.  
It was built to simulate a real-world cloud deployment with **scalability, security, and automation** in mind.

---

## 🏗️ Architecture Diagram

![AWS Architecture](AWS%20Architecture%20Diagram.png)

---

## 🔑 Key Features

### Networking & Compute
- **VPC** with public/private subnets, NAT Gateways, and Security Groups.  
- **Application Load Balancer (ALB)** protected by AWS WAF.  
- **EC2 Auto Scaling Group** spread across multiple AZs for high availability.  
- Private subnets isolate application servers and databases.  

### Storage & Data
- **Amazon RDS (Multi-AZ)** with synchronous replication (Primary & Standby).  
- **Amazon DynamoDB** for low-latency, event-driven storage.  

### Event-Driven & Serverless Processing
- **Amazon SQS** queue for decoupling workloads.  
- **AWS Lambda** consumer triggered by SQS to process tasks.  
- Lambda writes results into **DynamoDB**.  

### Security & DevSecOps
- **AWS WAF** in front of ALB for SQLi/XSS filtering and rate limiting.  
- **AWS Secrets Manager** for secure management of database and application credentials.  
- **Security Groups** enforce least-privilege:
  - ALB-SG: allows inbound 80/443 from the internet, forwards to EC2-SG.  
  - EC2-SG: allows inbound only from ALB-SG, outbound to DB-SG.  
  - DB-SG: allows inbound only from EC2-SG on DB port (3306/5432).  
- IAM roles with least-privilege policies.  
- **Amazon ECR** with lifecycle policies for container image storage.  
- **Trivy scans** for Docker image vulnerability detection during CI/CD.  

### CI/CD Pipeline
- **GitHub Actions** builds and pushes Docker images to **Amazon ECR**.  
- **Trivy** scan runs on each build before pushing.  
- **Auto Scaling Group refresh** ensures new EC2 instances pull the latest image from ECR automatically.  

### Monitoring & Logging
- **Amazon CloudWatch Logs & Alarms** integrated with EC2, ALB, WAF, and Lambda.  
- Monitors system metrics, application logs, and queue depth.  
- Alarms trigger notifications for failures or high utilization.  

---

## ⚙️ Tools & Technologies

- **AWS Services**: VPC • NAT Gateway • ALB/ASG • EC2 • RDS (Multi-AZ) • DynamoDB • SQS • Lambda • ECR • WAF • Secrets Manager • CloudWatch  
- **DevOps Tools**: Docker • GitHub Actions • Trivy • Bash • Terraform (optional for IaC)  

---
