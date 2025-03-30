# 🍏 Machine Learning Web App - Apple Quality Prediction 

This project is a **machine learning web application** that predicts outcomes based on different datasets, including **Apple Quality Prediction**. It uses **FastAPI** for the backend and **Node.js with Express.js & EJS** for the frontend.

## Tech Stack
- **Backend:** FastAPI (Python) – Handles ML model predictions.
- **Frontend:** Node.js, Express.js, EJS – Manages the UI.
- **Styling:** CSS – Custom UI design.
- **Machine Learning:** Scikit-learn, NumPy, Pandas. 

---

## 📌 Features  

✅ Train and evaluate **six classification models**  
✅ **Data normalization and scaling** (L1, L2, Standard, MinMax)  
✅ **Hyperparameter tuning** using GridSearchCV and **10-fold cross-validation**  
✅ Interactive **web interface** for making predictions  

---

## 📂 Dataset  

The dataset used is `apple_quality.csv`, containing features such as:  

- **Size**  
- **Weight**  
- **Crunchiness**  
- **Juiciness**  
- **Ripeness**  
- **Acidity**
- **Quality** 

---

## ⚙️ Machine Learning Process  

### 1️⃣ Apply 6 Classifiers  

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

The **best model** was selected based on these metrics.  

---

## 🚀 How to Run the Application  

### 1️⃣ Clone the Repository  

git clone https://github.com/ishitapradhan19/apple-quality-prediction.git  
cd apple-quality-prediction  

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

