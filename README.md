# heart-disease-predictor-website-using-api


A web app to predict heart disease risk using a trained **XGBoost** model, built with **Streamlit** and containerized using **Docker**.

## 🐳 Run with Docker (Recommended)

### 🔧 Step 1: Install Docker

Install Docker for your system:

- [Docker for Windows](https://docs.docker.com/desktop/install/windows-install/)
- [Docker for macOS](https://docs.docker.com/desktop/install/mac-install/)
- [Docker for Linux](https://docs.docker.com/engine/install/)

>  After installing Docker, make sure it is running.

### 🚀 Step 2: Build and Run

Open your terminal or CMD in the folder where all your files are, then:

```bash
docker build -t heart-predictor-app .
docker run -p 8501:8501 heart-predictor-app
## 📂 Project Structure

Make sure **all files are in the same folder** before building or running:

```plaintext
📁 heart-disease-predictor/
├── iris_api.py         # The main Streamlit app
├── model.pkl           # The trained XGBoost model
├── requirements.txt    # Python dependencies
└── Dockerfile          # Docker build instructions


---

![Screenshot (16)](https://github.com/user-attachments/assets/a5f0d137-48ab-4b2f-b8ee-d79c75cf288d)
