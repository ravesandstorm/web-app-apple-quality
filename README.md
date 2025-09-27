# 🍏 Machine Learning Web App - Apple Quality Prediction 

This is a **machine learning web application** project (developed for my college lab practicals) that predicts outcomes based on the [**Apple Quality Prediction**](https://www.kaggle.com/datasets/nelgiriyewithana/apple-quality) dataset. It uses **Node.js with Express.js & EJS**  for the frontend and **FastAPI** for the backend, based on the [kaggle notebook](https://www.kaggle.com/code/ravesandstorm/apple-svm-92-cv) by [Satvik](https://github.com/ravesandstorm/). Developed together with [Ishita Pradhan](https://github.com/ishitapradhan19), who worked on the frontend while I worked on the backend and deployment.

## Tech Stack
### [Ishita](https://github.com/ishitapradhan19)
- **Frontend:** Node.js, Express.js, EJS – Manages the UI.
- **Styling:** CSS – Custom UI design.

### [Satvik](https://github.com/ravesandstorm)
- **Backend:** Uvicorn, FastAPI (Python) – Handles ML model predictions and remote server.
- **Machine Learning:** Scikit-learn, NumPy, Pandas

---

## 📌 Features  

✅ Train and evaluate **six classification models**  
✅ **Data normalization and scaling** (L1, L2, Standard, MinMax)  
✅ **Hyperparameter tuning** using GridSearchCV and **10-fold cross-validation**  
✅ Interactive **web interface** for making predictions  

---

## 📂 Dataset  

The dataset used is [`apple_quality.csv`](https://www.kaggle.com/datasets/nelgiriyewithana/apple-quality), containing the features:  

- **Size**  
- **Weight**  
- **Crunchiness**  
- **Juiciness**  
- **Ripeness**  
- **Acidity**
- **Quality** 

---

## ⚙️ Machine Learning Process based on [notebook](https://www.kaggle.com/code/ravesandstorm/apple-svm-92-cv)

### 1️⃣ Applying All Classifiers  

The following six models were applied to classify apples into **good or bad** quality:  

- **K-Nearest Neighbors (KNN)**  
- **Support Vector Machine (SVM)**  
- **Decision Tree**  
- **Random Forest**  
- **Naïve Bayes**  
- **Gradient Boosting**  

Each model was evaluated using the following **metrics**:  

- **Accuracy**  
- **Precision**  
- **Recall**  
- **F1-Score**  

---

### 2️⃣ Data Normalization & Scaling  

To improve model performance, the dataset was **normalized and scaled** using four different techniques:  

- **L1 Normalization**  
- **L2 Normalization**  
- **Standard Scaling**  
- **MinMax Scaling**  

Each model was then **re-evaluated** after scaling, and the results were recorded.  

---

### 3️⃣ Hyperparameter Tuning & Cross-Validation  

To optimize model performance, **GridSearchCV** was used for **hyperparameter tuning**, along with **10-fold cross-validation** to find the best model.  

The models were evaluated again using:  

- **Cross-validated Accuracy**  
- **Precision**  
- **Recall**  
- **F1-Score**  

The best model **SVM** with **92.075% Cross Validation Accuracy** was selected based on these metrics, and then **FastAPI** was configured to run on the backend using the **Uvicorn** module, using the best model hyperparameters discovered in the notebook, developed by [Satvik](https://github.com/ravesandstorm/).

Node modules and frontend scripts with **ejs and js** were processed and developed by me.

---

## 🚀 How to Run the Application  

### 1️⃣ Clone the Repository  

git clone https://github.com/ishitapradhan19/web-app-apple-quality.git  
cd web-app-apple-quality  

### 2️⃣ Install Backend Dependencies  

pip install -r requirements.txt  

### 3️⃣ Start FastAPI Backend  

uvicorn main:app --reload  

### 4️⃣ Install Node.js Dependencies  

cd frontend  
npm install  

### 5️⃣ Start the Web Application  

nodemon index.js  

The application will be available at **http://localhost:3000**.  

---

## 📜 Contributing  

If you'd like to contribute, feel free to fork the repository and submit a pull request.  

---

## 📄 License  

This project is licensed under the **MIT License**.  

---

