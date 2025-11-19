import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS - Only for Header
st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 30px 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        border-radius: 15px;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    .main-header h1 {
        color: #ffffff;
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    }
    .author-name {
        color: rgba(255, 255, 255, 0.95);
        font-size: 14px;
        margin-top: 10px;
        font-weight: 500;
    }
    .author-name a {
        color: rgba(255, 255, 255, 0.95);
        text-decoration: none;
        font-weight: 600;
        border-bottom: 1px solid rgba(255, 255, 255, 0.5);
    }
    .author-name a:hover {
        color: #ffffff;
        border-bottom-color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="main-header">
        <h1>🎓 Student Performance Prediction System</h1>
        <p class="author-name">Developed by <a href="https://a7x3a.dev" target="_blank">Ahmad Omar</a></p>
    </div>
""", unsafe_allow_html=True)

# Navigation
col_nav1, col_nav2 = st.columns(2)
with col_nav1:
    if st.button("🇬🇧 English", use_container_width=True, key="nav_english"):
        st.session_state.page = "english"
        st.rerun()
with col_nav2:
    if st.button("🇹🇯 کوردی (Kurdish)", use_container_width=True, key="nav_kurdish"):
        st.session_state.page = "kurdish"
        st.rerun()

# Initialize page state
if 'page' not in st.session_state:
    st.session_state.page = "english"

# Load model and dataset
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

@st.cache_data
def load_dataset():
    return pd.read_csv("merged_dataset.csv")

model = load_model()
df = load_dataset()
target_col = "ExamScore"
feature_cols = df.drop([target_col, "FinalGrade"], axis=1).columns.tolist()

# Helper function
def get_unique_values(series):
    return sorted(series.unique().tolist())

# Main content
if st.session_state.page == "kurdish":
    # Kurdish Form
    st.markdown("### 🇹🇯 فۆرمی پێشبینی")
    
    # Kurdish translations
    translations = {
        "gender": {0: "نێر", 1: "مێ"},
        "learning_style": {0: "بینراو", 1: "بیستن", 2: "دەست", 3: "خوێندنەوە/نووسین"},
        "motivation": {0: "نزم", 1: "مامناوەند", 2: "بەرز"},
        "yes_no": {0: "نەخێر", 1: "بەڵێ"},
        "resource": {0: "نزم", 1: "مامناوەند", 2: "بەرز"},
        "stress": {0: "نزم", 1: "مامناوەند", 2: "بەرز"},
    }
    
    user_data = {}
    
    with st.form("prediction_form_kurdish"):
        # Section 1: Demographic Information
        st.markdown("#### 👤 زانیاری دیمۆگرافی")
        col1, col2 = st.columns(2)
        
        with col1:
            gender_selected = st.selectbox(
                "جێندەر:",
                options=list(translations["gender"].keys()),
                format_func=lambda x: translations["gender"][x],
                key="gender_kur"
            )
            user_data['Gender'] = gender_selected
            
            user_data['Age'] = st.number_input(
                "تەمەن:",
                min_value=int(df['Age'].min()),
                max_value=int(df['Age'].max()),
                value=int(df['Age'].mean()),
                step=1,
                key="age_kur"
            )
        
        with col2:
            learning_style_selected = st.selectbox(
                "شێوازی فێربوون:",
                options=get_unique_values(df['LearningStyle']),
                format_func=lambda x: translations["learning_style"].get(x, f"شێواز {x}"),
                key="learning_style_kur"
            )
            user_data['LearningStyle'] = learning_style_selected
            
            motivation_selected = st.selectbox(
                "ئاستی هاندان:",
                options=get_unique_values(df['Motivation']),
                format_func=lambda x: translations["motivation"].get(x, f"ئاست {x}"),
                key="motivation_kur"
            )
            user_data['Motivation'] = motivation_selected
        
        st.markdown("---")
        
        # Section 2: Study Behaviors
        st.markdown("#### 📖 هەڵسوڕانەوە و بەشداری خوێندن")
        col3, col4 = st.columns(2)
        
        with col3:
            user_data['StudyHours'] = st.number_input(
                "کاتژمێرەکانی خوێندن لە هەفتەیەکدا:",
                min_value=int(df['StudyHours'].min()),
                max_value=int(df['StudyHours'].max()),
                value=int(df['StudyHours'].mean()),
                step=1,
                key="study_hours_kur"
            )
            
            user_data['Attendance'] = st.number_input(
                "ڕێژەی بەشداریکردن (%):",
                min_value=int(df['Attendance'].min()),
                max_value=int(df['Attendance'].max()),
                value=int(df['Attendance'].mean()),
                step=1,
                key="attendance_kur"
            )
            
            user_data['AssignmentCompletion'] = st.number_input(
                "ڕێژەی تەواوکردنی ئەرکەکان (%):",
                min_value=int(df['AssignmentCompletion'].min()),
                max_value=int(df['AssignmentCompletion'].max()),
                value=int(df['AssignmentCompletion'].mean()),
                step=1,
                key="assignment_kur"
            )
        
        with col4:
            user_data['OnlineCourses'] = st.number_input(
                "ژمارەی کۆرسە ئۆنلاینەکان:",
                min_value=int(df['OnlineCourses'].min()),
                max_value=int(df['OnlineCourses'].max()),
                value=int(df['OnlineCourses'].mean()),
                step=1,
                key="online_courses_kur"
            )
            
            discussion_selected = st.selectbox(
                "بەشداری لە گفتوگۆکاندا:",
                options=get_unique_values(df['Discussions']),
                format_func=lambda x: translations["yes_no"].get(x, "نەزانراو"),
                key="discussions_kur"
            )
            user_data['Discussions'] = discussion_selected
            
            extracurricular_selected = st.selectbox(
                "بەشداری لە چالاکییەکانی دەرەوە:",
                options=get_unique_values(df['Extracurricular']),
                format_func=lambda x: translations["yes_no"].get(x, "نەزانراو"),
                key="extracurricular_kur"
            )
            user_data['Extracurricular'] = extracurricular_selected
        
        st.markdown("---")
        
        # Section 3: Resources & Technology
        st.markdown("#### 💻 سەرچاوەکان و تەکنەلۆژیا")
        col5, col6 = st.columns(2)
        
        with col5:
            resource_selected = st.selectbox(
                "ئاستی دەستگەیشتن بە سەرچاوەکان:",
                options=get_unique_values(df['Resources']),
                format_func=lambda x: translations["resource"].get(x, f"ئاست {x}"),
                key="resources_kur"
            )
            user_data['Resources'] = resource_selected
            
            internet_selected = st.selectbox(
                "دەستگەیشتن بە ئینتەرنێت:",
                options=get_unique_values(df['Internet']),
                format_func=lambda x: translations["yes_no"].get(x, "نەزانراو"),
                key="internet_kur"
            )
            user_data['Internet'] = internet_selected
        
        with col6:
            edutech_selected = st.selectbox(
                "بەکارهێنانی تەکنەلۆژیای پەروەردەیی:",
                options=get_unique_values(df['EduTech']),
                format_func=lambda x: translations["yes_no"].get(x, "نەزانراو"),
                key="edutech_kur"
            )
            user_data['EduTech'] = edutech_selected
            
            stress_selected = st.selectbox(
                "ئاستی فشاری دەروونی:",
                options=get_unique_values(df['StressLevel']),
                format_func=lambda x: translations["stress"].get(x, f"ئاست {x}"),
                key="stress_kur"
            )
            user_data['StressLevel'] = stress_selected
        
        submitted = st.form_submit_button("🔮 پێشبینی نمرەی تاقیکردنەوە", use_container_width=True, type="primary")
    
    if submitted:
        try:
            # Convert input to DataFrame
            input_df = pd.DataFrame([user_data])
            
            # Ensure all expected columns are present
            for col in feature_cols:
                if col not in input_df.columns:
                    input_df[col] = df[col].mean()
            
            # Reorder columns to match model expectations
            input_df = input_df[feature_cols]
            
            # Make prediction
            prediction = model.predict(input_df)[0]
            exam_score = round(prediction, 2)
            
            # Determine performance level
            if exam_score >= 90:
                level = "نایاب"
            elif exam_score >= 80:
                level = "زۆر باش"
            elif exam_score >= 70:
                level = "باش"
            elif exam_score >= 60:
                level = "مامناوەند"
            else:
                level = "پێویستی بە باشترکردن هەیە"
            
            pass_status = "تێپەڕ" if exam_score >= 60 else "شکست"
            
            # Display result
            st.success(f"### 🎯 ئەنجامی پێشبینی")
            st.metric("نمرە", f"{exam_score:.2f}", "لە ١٠٠")
            st.info(f"**ئاست:** {level} | **دۆخ:** {pass_status}")
            
        except Exception as e:
            st.error(f"❌ هەڵە: {str(e)}")
            st.info("تکایە دڵنیا ببەوە کە هەموو خانەکان بە دروستی پڕکراونەتەوە.")

else:
    # English Form
    st.markdown("### 🇬🇧 Prediction Form")
    
    user_data = {}
    
    with st.form("prediction_form"):
        # Section 1: Demographic Information
        st.markdown("#### 👤 Demographic Information")
        col1, col2 = st.columns(2)
        
        with col1:
            gender_options = {0: "Male", 1: "Female"}
            gender_selected = st.selectbox(
                "Gender:",
                options=list(gender_options.keys()),
                format_func=lambda x: gender_options[x],
                key="gender"
            )
            user_data['Gender'] = gender_selected
            
            user_data['Age'] = st.number_input(
                "Age:",
                min_value=int(df['Age'].min()),
                max_value=int(df['Age'].max()),
                value=int(df['Age'].mean()),
                step=1,
                key="age"
            )
        
        with col2:
            learning_style_options = {0: "Visual", 1: "Auditory", 2: "Kinesthetic", 3: "Reading/Writing"}
            learning_style_selected = st.selectbox(
                "Learning Style:",
                options=get_unique_values(df['LearningStyle']),
                format_func=lambda x: learning_style_options.get(x, f"Style {x}"),
                key="learning_style"
            )
            user_data['LearningStyle'] = learning_style_selected
            
            motivation_options = {0: "Low", 1: "Medium", 2: "High"}
            motivation_selected = st.selectbox(
                "Motivation Level:",
                options=get_unique_values(df['Motivation']),
                format_func=lambda x: motivation_options.get(x, f"Level {x}"),
                key="motivation"
            )
            user_data['Motivation'] = motivation_selected
        
        st.markdown("---")
        
        # Section 2: Study Behaviors
        st.markdown("#### 📖 Study Behaviors & Engagement")
        col3, col4 = st.columns(2)
        
        with col3:
            user_data['StudyHours'] = st.number_input(
                "Study Hours per Week:",
                min_value=int(df['StudyHours'].min()),
                max_value=int(df['StudyHours'].max()),
                value=int(df['StudyHours'].mean()),
                step=1,
                key="study_hours"
            )
            
            user_data['Attendance'] = st.number_input(
                "Attendance Rate (%):",
                min_value=int(df['Attendance'].min()),
                max_value=int(df['Attendance'].max()),
                value=int(df['Attendance'].mean()),
                step=1,
                key="attendance"
            )
            
            user_data['AssignmentCompletion'] = st.number_input(
                "Assignment Completion Rate (%):",
                min_value=int(df['AssignmentCompletion'].min()),
                max_value=int(df['AssignmentCompletion'].max()),
                value=int(df['AssignmentCompletion'].mean()),
                step=1,
                key="assignment"
            )
        
        with col4:
            user_data['OnlineCourses'] = st.number_input(
                "Number of Online Courses:",
                min_value=int(df['OnlineCourses'].min()),
                max_value=int(df['OnlineCourses'].max()),
                value=int(df['OnlineCourses'].mean()),
                step=1,
                key="online_courses"
            )
            
            discussion_options = {0: "No", 1: "Yes"}
            discussion_selected = st.selectbox(
                "Participate in Discussions:",
                options=get_unique_values(df['Discussions']),
                format_func=lambda x: discussion_options.get(x, "Unknown"),
                key="discussions"
            )
            user_data['Discussions'] = discussion_selected
            
            extracurricular_options = {0: "No", 1: "Yes"}
            extracurricular_selected = st.selectbox(
                "Extracurricular Activities:",
                options=get_unique_values(df['Extracurricular']),
                format_func=lambda x: extracurricular_options.get(x, "Unknown"),
                key="extracurricular"
            )
            user_data['Extracurricular'] = extracurricular_selected
        
        st.markdown("---")
        
        # Section 3: Resources & Technology
        st.markdown("#### 💻 Resources & Technology")
        col5, col6 = st.columns(2)
        
        with col5:
            resource_options = {0: "Low", 1: "Medium", 2: "High"}
            resource_selected = st.selectbox(
                "Resource Access Level:",
                options=get_unique_values(df['Resources']),
                format_func=lambda x: resource_options.get(x, f"Level {x}"),
                key="resources"
            )
            user_data['Resources'] = resource_selected
            
            internet_options = {0: "No", 1: "Yes"}
            internet_selected = st.selectbox(
                "Internet Access:",
                options=get_unique_values(df['Internet']),
                format_func=lambda x: internet_options.get(x, "Unknown"),
                key="internet"
            )
            user_data['Internet'] = internet_selected
        
        with col6:
            edutech_options = {0: "No", 1: "Yes"}
            edutech_selected = st.selectbox(
                "Use Educational Technology:",
                options=get_unique_values(df['EduTech']),
                format_func=lambda x: edutech_options.get(x, "Unknown"),
                key="edutech"
            )
            user_data['EduTech'] = edutech_selected
            
            stress_options = {0: "Low", 1: "Medium", 2: "High"}
            stress_selected = st.selectbox(
                "Stress Level:",
                options=get_unique_values(df['StressLevel']),
                format_func=lambda x: stress_options.get(x, f"Level {x}"),
                key="stress"
            )
            user_data['StressLevel'] = stress_selected
        
        submitted = st.form_submit_button("🔮 Predict Exam Score", use_container_width=True, type="primary")
    
    if submitted:
        try:
            # Convert input to DataFrame
            input_df = pd.DataFrame([user_data])
            
            # Ensure all expected columns are present
            for col in feature_cols:
                if col not in input_df.columns:
                    input_df[col] = df[col].mean()
            
            # Reorder columns to match model expectations
            input_df = input_df[feature_cols]
            
            # Make prediction
            prediction = model.predict(input_df)[0]
            exam_score = round(prediction, 2)
            
            # Determine performance level
            if exam_score >= 90:
                level = "Excellent"
            elif exam_score >= 80:
                level = "Very Good"
            elif exam_score >= 70:
                level = "Good"
            elif exam_score >= 60:
                level = "Average"
            else:
                level = "Needs Improvement"
            
            pass_status = "Pass" if exam_score >= 60 else "Fail"
            
            # Display result
            st.success(f"### 🎯 Prediction Result")
            st.metric("Exam Score", f"{exam_score:.2f}", "out of 100")
            st.info(f"**Level:** {level} | **Status:** {pass_status}")
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("Please make sure all fields are filled correctly.")
