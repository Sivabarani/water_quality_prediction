# 💧 Water Quality Prediction (Flask + Machine Learning)

## 📌 Project Overview

This project is a basic end-to-end Machine Learning web application built to understand how to integrate a trained ML model with a web interface using Flask.

The application takes various chemical parameters of water as input and predicts whether the water is safe to drink or not.

> ⚠️ Note: This is a learning project focused on understanding ML workflow, Flask integration, and prediction pipelines. It is not a production-ready system.

---

## 🎯 Objectives

* Understand end-to-end ML workflow
* Learn how to connect ML model with frontend (HTML form)
* Handle user inputs and convert them into model-ready format
* Perform predictions using a trained model
* Understand feature ordering and its importance in ML inference

---

## 🧠 Features Used

The model takes the following input features:

* Aluminium
* Ammonia
* Arsenic
* Barium
* Cadmium
* Chloramine
* Chromium
* Copper
* Fluoride
* Bacteria
* Viruses
* Lead
* Nitrates
* Nitrites
* Mercury
* Perchlorate
* Radium
* Selenium
* Silver
* Uranium

---

## ⚙️ Tech Stack

* Python
* Flask
* HTML & CSS
* Scikit-learn
* Joblib

---

## 🔄 Workflow

1. User opens the web application
2. Enters chemical values in the form
3. Form data is sent to Flask backend
4. Backend processes input and arranges features
5. Model predicts water quality
6. Result is displayed to the user

---

## 📂 Project Structure

```
water-quality-ml/
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── get_details.html
│   ├── result.html
│
└── notebook/
    └── training.ipynb
```

---

## 🚀 How to Run

1. Clone the repository

```
git clone https://github.com/your-username/water-quality-ml.git
cd water-quality-ml
```

2. Create virtual environment

```
python -m venv venv
```

3. Activate environment

Windows:

```
venv\Scripts\activate
```

4. Install dependencies

```
pip install -r requirements.txt
```

5. Run the application

```
python app.py
```

6. Open browser

```
http://127.0.0.1:5000/
```

---

## ⚠️ Important Notes

* Feature order must match the training dataset
* Incorrect ordering will lead to wrong predictions
* Input values should be within realistic ranges
* Model requires scikit-learn dependency

---

## 📌 Limitations

* No input validation implemented
* No model explainability
* No database integration
* Not deployed to cloud
* Basic UI only

---

## 🔮 Future Improvements

* Add ML Pipeline (Scaler + Model)
* Improve UI/UX
* Add input validation
* Deploy on cloud (Render / AWS)
* Convert to API using FastAPI
* Add feature importance / explainability

---

## 📚 Learning Outcomes

Through this project, I learned:

* How ML models are integrated into web applications
* Flask routing and request handling
* Handling form data and converting to model input
* Importance of feature consistency in ML inference
* Debugging real-world issues in ML deployment

---

## 🙌 Acknowledgement

This project was built as part of my learning journey in Machine Learning and Backend Development.

---

## 📬 Contact

Feel free to connect for feedback or collaboration.
