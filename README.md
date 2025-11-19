# 🎓 Student Performance Prediction System

A machine learning web application that predicts student academic performance (CGPA) based on various academic and personal factors. Built with Streamlit and Random Forest Regression.

**Developed by:** [Ahmad Omar](https://github.com/yourusername)

## 📊 Dataset

This project uses the **Students Academic Performance Evaluation Dataset** from Mendeley Data.

**Dataset Source:** [https://data.mendeley.com/datasets/dc3797vf3t/1](https://data.mendeley.com/datasets/dc3797vf3t/1)

**Dataset Information:**
- **Total Records:** 1,195 students
- **Total Features:** 31 features
- **Target Variable:** Current CGPA (0-4.0 scale)
- **Data Collection:** Online survey from Computer Science and Engineering students at a private university in Bangladesh

## 📖 What is CGPA?

**CGPA** stands for **Cumulative Grade Point Average**. It is a standardized method used to measure a student's overall academic performance across all semesters or courses.

### How CGPA Works:
- **Scale:** Typically measured on a 0-4.0 scale (in this dataset)
- **Calculation:** CGPA is calculated by averaging the Grade Point Averages (GPA) from all completed semesters
- **Purpose:** Provides a single number that represents a student's overall academic achievement

### CGPA Scale Interpretation:
- **4.0** = Excellent (A grade, 90-100%)
- **3.0-3.9** = Very Good (B grade, 80-89%)
- **2.0-2.9** = Good (C grade, 70-79%)
- **1.0-1.9** = Average (D grade, 60-69%)
- **Below 1.0** = Needs Improvement (F grade, below 60%)

### In This Application:
The model predicts the student's **CGPA** (0-4.0), which is then converted to a **percentage** (0-100%) for easier understanding. For example:
- CGPA of 3.44 = 86% performance accuracy
- CGPA of 3.0 = 75% performance accuracy
- CGPA of 2.5 = 62.5% performance accuracy

This percentage represents the student's **expected academic performance level**, not a probability of success.

## 🔍 Features (Factors)

The model uses **31 factors** to predict student performance, organized into the following categories:

### 👤 Basic Information (6 factors)
1. **University Admission year** - Year when student was admitted
2. **Gender** - Student's gender
3. **Age** - Student's age
4. **H.S.C passing year** - Year when Higher Secondary Certificate was passed
5. **Program** - Academic program/field of study
6. **Current Semester** - Current semester number

### 📚 Academic Information (8 factors)
7. **Do you have meritorious scholarship?** - Scholarship status
8. **Status of your English language proficiency** - English proficiency level
9. **Average attendance on class** - Class attendance percentage
10. **Did you ever fall in probation?** - Probation history
11. **Did you ever got suspension?** - Suspension history
12. **Do you attend in teacher consultancy for academic problems?** - Teacher consultation usage
13. **What was your previous SGPA?** - Previous Semester Grade Point Average
14. **How many Credit did you have completed?** - Total credits completed

### 📖 Study Habits (6 factors)
15. **How many hour do you study daily?** - Daily study hours
16. **How many times do you seat for study in a day?** - Number of study sessions per day
17. **What is your preferable learning mode?** - Preferred learning method
18. **How many hour do you spent daily on your skill development?** - Daily skill development hours
19. **What are the skills do you have?** - Skills possessed by student
20. **What is you interested area?** - Area of interest

### 💻 Technology & Transportation (4 factors)
21. **Do you use smart phone?** - Smartphone usage
22. **Do you have personal Computer?** - Personal computer ownership
23. **Do you use University transportation?** - University transport usage
24. **How many hour do you spent daily in social media?** - Daily social media hours

### 👥 Personal & Lifestyle (7 factors)
25. **What is your relationship status?** - Relationship status
26. **Are you engaged with any co-curriculum activities?** - Extracurricular participation
27. **With whom you are living with?** - Living situation
28. **Do you have any health issues?** - Health problems
29. **Do you have any physical disabilities?** - Physical disabilities
30. **What is your monthly family income?** - Family monthly income

### 🎯 Target Variable
31. **What is your current CGPA?** - Current Cumulative Grade Point Average (0-4.0 scale)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/StudentPerformanceApp.git
   cd StudentPerformanceApp
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Download the dataset**
   - Download from: [Mendeley Dataset](https://data.mendeley.com/datasets/dc3797vf3t/1)
   - Place the Excel file as `Students_Performance_data_set.xlsx` in the project root

## 📝 Usage

### 1. Train the Model
```bash
python train.py
```
This will:
- Load the dataset
- Encode categorical variables
- Train a Random Forest Regressor
- Save the model and encoders as `model.pkl` and `encoders.pkl`

### 2. Run the Web Application
```bash
streamlit run app.py
```
The application will open in your default web browser at `http://localhost:8501`

### 3. Make Predictions
- Fill in all the required fields in the web interface
- Click "🔮 Predict Performance Accuracy"
- View the predicted performance as a percentage (0-100%)

## 📁 Project Structure

```
StudentPerformanceApp/
│
├── app.py                          # Streamlit web application
├── train.py                        # Model training script
├── model.pkl                       # Trained Random Forest model
├── encoders.pkl                    # Label encoders for categorical variables
├── Students_Performance_data_set.xlsx  # Dataset file
├── requirements.txt                # Python dependencies
├── README.md                       # This file
└── venv/                           # Virtual environment (not in git)
```

## 🛠️ Technologies Used

- **Python 3.x**
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation
- **Scikit-learn** - Machine learning (Random Forest Regressor)
- **Joblib** - Model serialization
- **OpenPyXL** - Excel file reading

## 📈 Model Information

- **Algorithm:** Random Forest Regressor
- **Input Features:** 30 features
- **Target:** Current CGPA (converted to percentage accuracy)
- **Output:** Performance accuracy percentage (0-100%)

## 📄 License

This project uses the dataset from Mendeley Data which is licensed under **CC BY 4.0**.

## 🙏 Acknowledgments

- **Dataset Contributors:** Arifa Tur Rahman, Suhala Lamia, Arafat Hossain Shishir, Maria Misty Barsa
- **Dataset Source:** [Mendeley Data Repository](https://data.mendeley.com/datasets/dc3797vf3t/1)

## 📧 Contact

For questions or suggestions, please open an issue on GitHub or contact the developer.

---

**Note:** Make sure to download the dataset from the Mendeley link and place it in the project directory before running the application.

