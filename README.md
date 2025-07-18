# 📚 BookReview DevOps Project

This is a real-time DevOps project showcasing a full-stack Book Review Web App deployed using:

- 🐳 Docker for containerization
- 🛠️ Jenkins for CI/CD
- ☁️ AWS EC2/EKS for hosting
- ⚙️ Kubernetes for orchestration
- 🌐 Terraform for infrastructure as code
- 📊 Prometheus + Grafana for monitoring

---

## 📖 About the Project

This project demonstrates how to build and deploy a real-time web application using complete DevOps practices. The goal is to showcase how a modern application is developed, containerized, automated with CI/CD, and deployed to the cloud using scalable infrastructure.

### 🔍 Key Use Case:
A simple Book Review App allows users to submit and view book reviews. This helps demonstrate:
- Frontend-backend interaction
- REST API usage
- Microservices packaging
- DevOps automation in real-world flow

---

## 🧰 Tools & Why They’re Used

| Tool | Purpose |
|------|---------|
| **Git & GitHub** | Version control & collaboration |
| **Python Flask** | Backend REST API for handling reviews |
| **HTML/CSS/JS** | Lightweight frontend for user interaction |
| **Docker** | Containerize frontend & backend for consistency |
| **Jenkins** | Automate CI/CD pipeline from code to deployment |
| **Terraform** | Define and provision cloud infra (AWS EC2, EKS) as code |
| **AWS EC2 & EKS** | Host Jenkins, deploy app on Kubernetes |
| **Kubernetes** | Scale and manage containerized apps |
| **Prometheus & Grafana** | Monitor app health and visualize metrics |

---

## 📂 Project Structure

```text
bookreview-devops/
├── backend/         # Flask API
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/        # Static HTML/CSS
│   ├── index.html
│   └── Dockerfile
├── infra/           # Terraform scripts (AWS infra)
├── k8s/             # Kubernetes YAML files
├── Jenkinsfile      # CI/CD Pipeline config
└── README.md
```

---

## 🚀 Live Goals

- ✅ Local Dockerized Setup  
- ✅ CI/CD with Jenkins  
- ✅ Deploy to EKS via Terraform  
- ✅ Monitor with Prometheus & Grafana

---

## 👨‍💻 Author

[Vignesh M](https://www.linkedin.com/in/vignesh-manoharan-6a6a58240/) – DevOps Engineer

---

## 📜 License

MIT License – free to use and modify.
