# 🎓 Student Performance Prediction System

A machine learning web application that predicts student exam scores based on various academic and personal factors. Built with Streamlit and Random Forest Regression.

**Developed by:** [Ahmad Omar](https://a7x3a.dev)

## 📊 Dataset

This project uses a merged student performance dataset from Zenodo.

**Dataset Information:**
- **Total Records:** 14,003 students
- **Total Features:** 14 features
- **Target Variable:** Exam Score (0-100 scale)
- **File Format:** CSV (`merged_dataset.csv`)

## 🎯 What is Exam Score?

The model predicts a student's **Exam Score** on a scale of **0-100**, representing their expected performance on an exam.

### Exam Score Scale Interpretation:
- **90-100** = Excellent (نایاب)
- **80-89** = Very Good (زۆر باش)
- **70-79** = Good (باش)
- **60-69** = Average (مامناوەند)
- **Below 60** = Needs Improvement (پێویستی بە باشترکردن هەیە)

### Pass/Fail Criteria:
- **60 or above** = Pass (تێپەڕ)
- **Below 60** = Fail (شکست)

## 🔍 Features (14 Factors)

The model uses **14 factors** to predict student performance, organized into the following categories:

### 👤 Demographic Information (4 factors)
1. **Gender** - Student's gender (Male/Female)
2. **Age** - Student's age
3. **Learning Style** - Preferred learning method (Visual, Auditory, Kinesthetic, Reading/Writing)
4. **Motivation** - Motivation level (Low, Medium, High)

### 📖 Study Behaviors & Engagement (6 factors)
5. **Study Hours** - Hours studied per week
6. **Attendance** - Attendance rate (%)
7. **Assignment Completion** - Assignment completion rate (%)
8. **Online Courses** - Number of online courses taken
9. **Discussions** - Participation in discussions (Yes/No)
10. **Extracurricular** - Engagement in extracurricular activities (Yes/No)

### 💻 Resources & Technology (4 factors)
11. **Resources** - Resource access level (Low, Medium, High)
12. **Internet** - Internet access availability (Yes/No)
13. **EduTech** - Use of educational technology (Yes/No)
14. **Stress Level** - Stress level (Low, Medium, High)

## 🌍 Language Support

The application supports **two languages**:
- **🇬🇧 English** - Full English interface
- **🇹🇯 کوردی (Kurdish)** - Complete Kurdish translation with RTL support

Users can switch between languages using the navigation buttons at the top of the page.

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
   - Ensure `merged_dataset.csv` is in the project root directory
   - The dataset should contain 14 feature columns plus `ExamScore` and `FinalGrade`

## 📝 Usage

### 1. Train the Model
```bash
python train.py
```
This will:
- Load the dataset from `merged_dataset.csv`
- Train a Random Forest Regressor
- Save the model as `model.pkl`
- Display training and testing R² scores

**Note:** All features in the dataset are already numeric, so no encoding is required.

### 2. Run the Web Application
```bash
streamlit run app.py
```
The application will open in your default web browser at `http://localhost:8501`

### 3. Make Predictions
1. Select your preferred language (English or Kurdish)
2. Fill in all the required fields in the form:
   - **Demographic Information** (Gender, Age, Learning Style, Motivation)
   - **Study Behaviors & Engagement** (Study Hours, Attendance, Assignments, etc.)
   - **Resources & Technology** (Resources, Internet, EduTech, Stress Level)
3. Click "🔮 Predict Exam Score" (or "🔮 پێشبینی نمرەی تاقیکردنەوە" in Kurdish)
4. View the predicted exam score (0-100) along with performance level and pass/fail status

## 📁 Project Structure

```
StudentPerformanceApp/
│
├── app.py                          # Streamlit web application
├── train.py                        # Model training script
├── model.pkl                       # Trained Random Forest model
├── merged_dataset.csv              # Dataset file (CSV format)
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

## 📈 Model Information

- **Algorithm:** Random Forest Regressor
- **Input Features:** 14 features
- **Target:** Exam Score (0-100 scale)
- **Output:** Predicted exam score with performance level and pass/fail status
- **Dataset Size:** 14,003 student records
- **Data Type:** All features are numeric (no encoding required)

## 🎨 Design Features

- **Clean Interface:** Uses Streamlit's default theme for a clean, professional look
- **Custom Header:** Beautiful gradient header with developer information
- **Bilingual Support:** Full English and Kurdish language support
- **Responsive Layout:** Two-column form layout for better organization
- **Input Validation:** All inputs are validated with min/max values from the dataset
- **Clear Results:** Results displayed using Streamlit's native components (metrics, success messages, info boxes)

## 📄 License

This project uses a dataset that may be subject to its own licensing terms. Please refer to the dataset source for licensing information.

## 🙏 Acknowledgments

- **Developer:** Ahmad Omar ([a7x3a.dev](https://a7x3a.dev))
- Dataset contributors and researchers who made this project possible

## 📧 Contact

For questions or suggestions, please open an issue on GitHub or contact the developer.

---

**Note:** Make sure the `merged_dataset.csv` file is in the project directory and the model has been trained (`model.pkl` exists) before running the application.
