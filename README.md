# 🫀 heart-disease-predictor-website-using-api

Check out my website, **cloud-deployed using Streamlit Cloud**:  
🌐 [Live App](https://heart-disease-predictor-website-using-api-unqfusbxu947pqbmwis9.streamlit.app/)

A web app to predict heart disease risk using a trained **XGBoost** model, built with **Streamlit**, and containerized using **Docker**.

---

## 🐳 Run with Docker (Recommended)

### 🔧 Step 1: Install Docker

Install Docker for your operating system:

- 🪟 [Docker for Windows](https://docs.docker.com/desktop/install/windows-install/)
- 🍎 [Docker for macOS](https://docs.docker.com/desktop/install/mac-install/)
- 🐧 [Docker for Linux](https://docs.docker.com/engine/install/)

> ✅ After installing Docker, make sure Docker Desktop is **running**.

---

### 🚀 Step 2: Build and Run the App

Open your terminal or CMD inside the folder that contains your files, then run:

```bash
docker build -t heart-predictor-app .
docker run -p 8501:8501 heart-predictor-app
