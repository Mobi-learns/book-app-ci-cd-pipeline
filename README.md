
This repository contains the code for a simple **Flask-based Book Recommendation Web Application**. It integrates a **CI/CD pipeline** using **Jenkins**, **AWS CodeDeploy**, **S3**, and **EC2**, enabling automatic deployment whenever new code is pushed to the repository.

## Features


- **Homepage**: A simple landing page displaying the main structure of the app.
- **Recommendation Page**: Displays a curated list of recommended books.
- **Flask Backend**: Powered by Python's Flask framework.
- **CI/CD Pipeline**: Automatic deployment triggered by Jenkins on every Git push.
- **AWS Integration**: Application deployment is handled by AWS CodeDeploy and hosted on EC2.

---

## Directory Structure
```
book-recommendation/
├── static/                  # Static files like CSS
│   └── styles.css
├── templates/               # HTML templates for Flask
│   ├── index.html           # Main landing page
│   └── recommend.html       # Book recommendation page
├── app.py                   # Flask application script
└── requirements.txt         # Python dependencies
```

---

## Prerequisites
### Tools
- **Python 3.x**
- **Flask** (`pip install flask`)
- **AWS Account**: To set up CodeDeploy, EC2, and S3.
- **Jenkins CI**: Installed on an EC2 instance for CI/CD.

### AWS Resources
- **S3 Bucket**: For storing deployment artifacts (e.g., `my-book-app-deployment-artifacts`).
- **EC2 Instance**: To host the web application.
- **AWS CodeDeploy**: For managing deployment to the EC2 instance.
- **IAM Role**: Ensure your EC2 instances have appropriate roles with **S3**, **CodeDeploy**, and **EC2** access.

---

## Setup Instructions

### 1. **Clone the Repository**
```bash
git clone https://github.com/your-username/book-app-ci-cd-pipeline.git
cd book-app-ci-cd-pipeline
```

### 2. **Install Dependencies**
Make sure you have Python and Flask installed. You can install the dependencies listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. **Run Locally**
To run the Flask application locally for testing:
```bash
python app.py
```
Visit `http://localhost:5000/` in your browser.

---

## CI/CD Pipeline

The CI/CD pipeline is configured to automatically deploy the application when code is pushed to the repository.

### 1. **Jenkins Configuration**
- **Jenkins Job**: A Jenkins job is set up to monitor the repository for changes.
- **Build Trigger**: A **GitHub webhook** triggers the Jenkins job on code push.
- **Build Steps**:
  - The Jenkins job packages the application files into a ZIP archive.
  - The ZIP is uploaded to the specified **S3 bucket** (`my-book-app-deployment-artifacts`).
  - AWS **CodeDeploy** pulls the artifact from S3 and deploys it to an **EC2 instance**.

### 2. **AWS CodeDeploy Configuration**
- **Application Name**: `BookRecommendationApp`
- **Deployment Group**: `BookRecommendationApp-DeploymentGroup`
- **S3 Bucket**: Artifacts are stored in the bucket (e.g., `my-book-app-deployment-artifacts`).
- **AppSpec.yml**: CodeDeploy uses this file to execute deployment steps, such as copying files and starting the application.

---

## Deployment Steps

1. **Push Changes to GitHub**:
   Any changes pushed to the GitHub repository trigger the CI/CD pipeline.

2. **Jenkins Builds the Application**:
   Jenkins pulls the latest code, zips it, and uploads the artifact to S3.

3. **AWS CodeDeploy Deploys the Application**:
   CodeDeploy automatically fetches the artifact from S3 and deploys it to the EC2 instance.

4. **Access the Application**:
   - Once the deployment is complete, you can access the app via the **public IP** of the EC2 instance:
     ```bash
     http://<EC2-Public-IP>/
     ```

---

## AppSpec.yml

This file instructs AWS CodeDeploy on how to deploy your application. It handles file copy operations and post-deployment actions like starting the Flask app.

**AppSpec.yml Example**:
```yaml
version: 0.0
os: linux
files:
  - source: /BookRecommendationApp.zip
    destination: /var/www/html/
hooks:
  AfterInstall:
    - location: scripts/install_dependencies.sh
      timeout: 300
  ApplicationStart:
    - location: scripts/start_server.sh
      timeout: 300
```

---

## IAM Role for Jenkins & EC2

Make sure your Jenkins and EC2 instances have the proper IAM role to access AWS services.

1. **S3 Full Access**: To upload deployment artifacts to S3.
2. **CodeDeploy Full Access**: To interact with CodeDeploy for deployment operations.
3. **EC2 Access**: To deploy and manage EC2 instances.

---

## How to Contribute
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and push to GitHub (`git push origin feature-branch`).
4. Submit a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
For any issues, feel free to open an issue in this repository or contact the author.
>>>>>>> origin/main
