# AWS Cloud File Management System (EC2 + S3)

A cloud-based file management system built using **AWS S3**, **AWS EC2**, **AWS IAM**, and **Streamlit**, allowing users to upload, list, download, and manage files stored securely in the cloud through a web interface.

This project is an **enhanced and deployed extension** of my earlier AWS S3 file storage project, upgraded to a fully accessible cloud application running on an EC2 server.

---

## 🔗 Project Lineage (Previous Project)

This project extends my earlier work on basic AWS S3 file handling:

👉 **Previous Project:**  
AWS S3 Cloud File Manager (local machine-based)  
[https://github.com/VedhKamble/aws-s3-cloud-file-manager.git]

**Enhancements in this version:**
- Web-based UI using Streamlit
- Deployed on AWS EC2
- Public access via browser
- Real-world cloud networking & access handling
- Client-side file downloads fixed for production use

---

## 📌 Project Overview

The application provides a simple web interface where users can:
- Upload files to an AWS S3 bucket
- View files stored in the bucket
- Download files directly to their local system
- Interact with cloud storage without AWS Console access

The app is hosted on an **AWS EC2 instance** and is accessible publicly through the instance’s public IP and port.

---


📷 Architecture diagram available in the `/architecture diagram` folder.

---

## ✨ Features

- 🌐 Web-based file manager
- ☁️ Secure cloud storage using AWS S3
- 🚀 Deployed on AWS EC2
- 📤 Upload files to S3
- 📄 List available files
- 📥 Download files directly via browser
- 🔐 IAM-based AWS access
- 🧩 Beginner-friendly cloud architecture

---

## 🛠️ Tech Stack

- **Cloud:** AWS EC2, AWS S3, AWS IAM
- **Backend:** Python
- **SDK:** boto3
- **Frontend/UI:** Streamlit
- **OS:** Amazon Linux
- **Version Control:** Git & GitHub

---

## 🚀 Deployment Summary

1. Created and configured an AWS S3 bucket
2. Launched an EC2 instance (Amazon Linux)
3. Installed Python, pip, and dependencies
4. Configured security groups (opened port 8501)
5. Deployed Streamlit application on EC2
6. Connected EC2 to S3 using AWS credentials / IAM
7. Tested application from multiple external devices

---

## ✅ Proof of Execution

The application has been successfully tested and accessed from multiple devices outside the AWS network.

### Evidence Included:
- EC2 instance running status
- Security group inbound rules
- Web app UI screenshots
- File upload to S3
- File download working on client machines

📁 All screenshots are available in the `/Screenshots Proof` directory.

---

## 📚 Key Learnings

- Difference between local and cloud execution
- EC2 networking & security groups
- Client-side vs server-side file handling
- AWS S3 operations using boto3
- Deploying and debugging real cloud applications
- Managing production-level issues in cloud environments

---

## 🔮 Future Improvements

- IAM Role for EC2 (remove static credentials)
- HTTPS with Nginx reverse proxy
- User authentication
- File size & type restrictions
- Presigned S3 URLs
- Auto-restart using systemd
- CI/CD integration

---

## 👤 Author

**Vedh Kamble**  
Computer Science Engineering Undergraduate  
Interested in Cloud Computing, Cybersecurity & Networking  

---

## 📄 License

This project is for learning and educational purposes.


