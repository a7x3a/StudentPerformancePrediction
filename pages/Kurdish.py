import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
    page_title="سیستەمی پێشبینی کارایی قوتابی",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better UI with improved spacing and styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Kurdish:wght@400;600;700&display=swap');
    
    * {
        font-family: 'Noto Sans Kurdish', Arial, sans-serif;
    }
    
    /* Main Header with Indigo Gradient */
    .main-header {
        text-align: center;
        padding: 25px 20px;
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #6366f1 100%);
        border-radius: 15px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(79, 70, 229, 0.3);
        border: 1px solid rgba(99, 102, 241, 0.2);
    }
    .main-header h1 {
        color: #ffffff;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        letter-spacing: -0.5px;
    }
    .author-name {
        text-align: center;
        color: #e0e7ff;
        font-size: 14px;
        font-style: italic;
        margin-top: 10px;
        font-weight: 500;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
    }
    .author-name a {
        transition: all 0.3s ease;
    }
    .author-name a:hover {
        color: #ffffff !important;
        text-shadow: 0 0 8px rgba(255, 255, 255, 0.5);
    }
    
    /* Section Headers */
    .section-header {
        background: linear-gradient(90deg, rgba(79, 70, 229, 0.1) 0%, rgba(99, 102, 241, 0.05) 100%);
        padding: 12px 18px;
        border-radius: 8px;
        margin: 15px 0 10px 0;
        border-left: 4px solid #4f46e5;
        box-shadow: 0 2px 6px rgba(79, 70, 229, 0.1);
    }
    .section-header h3 {
        color: #4f46e5;
        margin: 0;
        font-weight: 600;
        font-size: 1.2rem;
    }
    
    /* Improved column spacing */
    .stColumn {
        padding: 0 8px;
    }
    
    /* Reduced spacing for form elements */
    .stSelectbox, .stNumberInput {
        margin-bottom: 0.8rem;
    }
    
    /* Field labels */
    .field-label {
        margin-bottom: 5px;
        font-size: 14px;
        font-weight: 600;
        color: #374151;
    }
    
    /* Custom predict button */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #6366f1 100%);
        color: white;
        font-weight: 700;
        font-size: 18px;
        padding: 15px 30px;
        border-radius: 12px;
        border: none;
        box-shadow: 0 8px 20px rgba(79, 70, 229, 0.4);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 25px rgba(79, 70, 229, 0.5);
    }
    
    /* Improved prediction result box */
    .prediction-box {
        text-align: center;
        padding: 35px 30px;
        background: linear-gradient(135deg, #10b981 0%, #059669 50%, #047857 100%);
        border-radius: 20px;
        color: white;
        margin: 25px 0;
        box-shadow: 0 20px 40px rgba(16, 185, 129, 0.3);
        border: 2px solid rgba(255, 255, 255, 0.2);
    }
    .prediction-box h2 {
        color: #ffffff;
        margin-bottom: 15px;
        font-weight: 600;
        font-size: 1.5rem;
    }
    .prediction-box h1 {
        font-size: 64px;
        margin: 20px 0;
        font-weight: 800;
        text-shadow: 3px 3px 10px rgba(0, 0, 0, 0.3);
    }
    .prediction-box p {
        font-size: 18px;
        margin-top: 12px;
        opacity: 0.95;
    }
    
    /* General improvements */
    .stForm {
        background-color: transparent;
    }
    
    /* Remove extra spacing */
    div[data-testid="stVerticalBlock"] > div[style*="flex-direction: column"] > div {
        margin-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header with author name
st.markdown("""
    <div class="main-header">
        <h1>🎓 سیستەمی پێشبینی کارایی قوتابی</h1>
        <p class="author-name">دروستکراوە لەلایەن <a href="https://a7x3a.dev" target="_blank" style="color: #e0e7ff; text-decoration: none; font-weight: 600;">ئەحمەد عومەر</a></p>
    </div>
""", unsafe_allow_html=True)

# Navigation buttons
col_nav1, col_nav2, col_nav3 = st.columns([1, 1, 1])
with col_nav1:
    if st.button("🇬🇧 English", use_container_width=True, key="nav_english_kur"):
        st.switch_page("app")
with col_nav2:
    if st.button("📚 Academic Info", use_container_width=True, key="nav_academic_kur"):
        st.session_state.page = "academic"
with col_nav3:
    st.markdown("")  # Empty column for spacing

# Initialize page state
if 'page' not in st.session_state:
    st.session_state.page = "kurdish"

# Load model and dataset
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

@st.cache_data
def load_dataset():
    df = pd.read_csv("merged_dataset.csv")
    return df

model = load_model()
df = load_dataset()
target_col = "ExamScore"
feature_cols = df.drop([target_col, "FinalGrade"], axis=1).columns.tolist()

# Helper function to get unique values for selectboxes
def get_unique_values(series):
    return sorted(series.unique().tolist())

# Kurdish translations
translations = {
    "gender": {0: "نێر", 1: "مێ"},
    "learning_style": {0: "بینراو", 1: "بیستن", 2: "دەست", 3: "خوێندنەوە/نووسین"},
    "motivation": {0: "نزم", 1: "مامناوەند", 2: "بەرز"},
    "yes_no": {0: "نەخێر", 1: "بەڵێ"},
    "resource": {0: "نزم", 1: "مامناوەند", 2: "بەرز"},
    "stress": {0: "نزم", 1: "مامناوەند", 2: "بەرز"},
    "levels": {
        "Excellent": "نایاب",
        "Very Good": "زۆر باش",
        "Good": "باش",
        "Average": "مامناوەند",
        "Needs Improvement": "پێویستی بە باشترکردن هەیە"
    },
    "pass_fail": {"Pass": "تێپەڕ", "Fail": "شکست"}
}

st.markdown("---")
user_data = {}

# Create a single form with all fields
with st.form("prediction_form_kurdish"):
    # Section 1: Demographic Information
    st.markdown('<div class="section-header"><h3>👤 زانیاری دیمۆگرافی</h3></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<p class="field-label">جێندەرەکەت چییە؟</p>', unsafe_allow_html=True)
        gender_selected = st.selectbox(
            "هەڵبژاردن:",
            options=list(translations["gender"].keys()),
            format_func=lambda x: translations["gender"][x],
            key="gender_kur",
            label_visibility="collapsed"
        )
        user_data['Gender'] = gender_selected
        
        st.markdown('<p class="field-label">تەمەنت چەندە؟</p>', unsafe_allow_html=True)
        user_data['Age'] = st.number_input(
            "تەمەن بنووسە:",
            min_value=int(df['Age'].min()),
            max_value=int(df['Age'].max()),
            value=int(df['Age'].mean()),
            step=1,
            key="age_kur",
            label_visibility="collapsed"
        )
    
    with col2:
        st.markdown('<p class="field-label">شێوازی فێربوونت چییە؟</p>', unsafe_allow_html=True)
        learning_style_selected = st.selectbox(
            "هەڵبژاردن:",
            options=get_unique_values(df['LearningStyle']),
            format_func=lambda x: translations["learning_style"].get(x, f"شێواز {x}"),
            key="learning_style_kur",
            label_visibility="collapsed"
        )
        user_data['LearningStyle'] = learning_style_selected
        
        st.markdown('<p class="field-label">ئاستی هاندانت چەندە؟</p>', unsafe_allow_html=True)
        motivation_selected = st.selectbox(
            "هەڵبژاردن:",
            options=get_unique_values(df['Motivation']),
            format_func=lambda x: translations["motivation"].get(x, f"ئاست {x}"),
            key="motivation_kur",
            label_visibility="collapsed"
        )
        user_data['Motivation'] = motivation_selected
    
    st.markdown("---")
    
    # Section 2: Study Behaviors & Engagement
    st.markdown('<div class="section-header"><h3>📖 هەڵسوڕانەوە و بەشداری خوێندن</h3></div>', unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown('<p class="field-label">چەند کاتژمێر لە هەفتەیەکدا دەخوێنیتەوە؟</p>', unsafe_allow_html=True)
        user_data['StudyHours'] = st.number_input(
            "کاتژمێر بنووسە:",
            min_value=int(df['StudyHours'].min()),
            max_value=int(df['StudyHours'].max()),
            value=int(df['StudyHours'].mean()),
            step=1,
            key="study_hours_kur",
            label_visibility="collapsed"
        )
        st.markdown('<p class="field-label">ڕێژەی بەشداریکردنت چەندە؟</p>', unsafe_allow_html=True)
        user_data['Attendance'] = st.number_input(
            "ڕێژەی بەشداری (%):",
            min_value=int(df['Attendance'].min()),
            max_value=int(df['Attendance'].max()),
            value=int(df['Attendance'].mean()),
            step=1,
            key="attendance_kur",
            label_visibility="collapsed"
        )
        st.markdown('<p class="field-label">ڕێژەی تەواوکردنی ئەرکەکانت چەندە؟</p>', unsafe_allow_html=True)
        user_data['AssignmentCompletion'] = st.number_input(
            "ڕێژەی تەواوکردن (%):",
            min_value=int(df['AssignmentCompletion'].min()),
            max_value=int(df['AssignmentCompletion'].max()),
            value=int(df['AssignmentCompletion'].mean()),
            step=1,
            key="assignment_kur",
            label_visibility="collapsed"
        )
    
    with col4:
        st.markdown('<p class="field-label">چەند کۆرسی ئۆنلاین وەردەگریت؟</p>', unsafe_allow_html=True)
        user_data['OnlineCourses'] = st.number_input(
            "ژمارە بنووسە:",
            min_value=int(df['OnlineCourses'].min()),
            max_value=int(df['OnlineCourses'].max()),
            value=int(df['OnlineCourses'].mean()),
            step=1,
            key="online_courses_kur",
            label_visibility="collapsed"
        )
        st.markdown('<p class="field-label">بەشداری لە گفتوگۆکاندا دەکەیت؟</p>', unsafe_allow_html=True)
        discussion_selected = st.selectbox(
            "هەڵبژاردن:",
            options=get_unique_values(df['Discussions']),
            format_func=lambda x: translations["yes_no"].get(x, "نەزانراو"),
            key="discussions_kur",
            label_visibility="collapsed"
        )
        user_data['Discussions'] = discussion_selected
        st.markdown('<p class="field-label">بەشداری لە چالاکییەکانی دەرەوەدا دەکەیت؟</p>', unsafe_allow_html=True)
        extracurricular_selected = st.selectbox(
            "هەڵبژاردن:",
            options=get_unique_values(df['Extracurricular']),
            format_func=lambda x: translations["yes_no"].get(x, "نەزانراو"),
            key="extracurricular_kur",
            label_visibility="collapsed"
        )
        user_data['Extracurricular'] = extracurricular_selected
    
    st.markdown("---")
    
    # Section 3: Resources & Technology
    st.markdown('<div class="section-header"><h3>💻 سەرچاوەکان و تەکنەلۆژیا</h3></div>', unsafe_allow_html=True)
    col5, col6 = st.columns(2)
    
    with col5:
        st.markdown('<p class="field-label">ئاستی دەستگەیشتنت بە سەرچاوەکان چەندە؟</p>', unsafe_allow_html=True)
        resource_selected = st.selectbox(
            "هەڵبژاردن:",
            options=get_unique_values(df['Resources']),
            format_func=lambda x: translations["resource"].get(x, f"ئاست {x}"),
            key="resources_kur",
            label_visibility="collapsed"
        )
        user_data['Resources'] = resource_selected
        st.markdown('<p class="field-label">دەستگەیشتن بە ئینتەرنێتت هەیە؟</p>', unsafe_allow_html=True)
        internet_selected = st.selectbox(
            "هەڵبژاردن:",
            options=get_unique_values(df['Internet']),
            format_func=lambda x: translations["yes_no"].get(x, "نەزانراو"),
            key="internet_kur",
            label_visibility="collapsed"
        )
        user_data['Internet'] = internet_selected
    
    with col6:
        st.markdown('<p class="field-label">تەکنەلۆژیای پەروەردەیی بەکاردەهێنیت؟</p>', unsafe_allow_html=True)
        edutech_selected = st.selectbox(
            "هەڵبژاردن:",
            options=get_unique_values(df['EduTech']),
            format_func=lambda x: translations["yes_no"].get(x, "نەزانراو"),
            key="edutech_kur",
            label_visibility="collapsed"
        )
        user_data['EduTech'] = edutech_selected
        st.markdown('<p class="field-label">ئاستی فشاری دەروونیت چەندە؟</p>', unsafe_allow_html=True)
        stress_selected = st.selectbox(
            "هەڵبژاردن:",
            options=get_unique_values(df['StressLevel']),
            format_func=lambda x: translations["stress"].get(x, f"ئاست {x}"),
            key="stress_kur",
            label_visibility="collapsed"
        )
        user_data['StressLevel'] = stress_selected
    
    # Submit button
    st.markdown("---")
    submitted = st.form_submit_button("🔮 پێشبینی نمرەی تاقیکردنەوە", use_container_width=True, type="primary")

if submitted:
    try:
        # Convert input to DataFrame
        input_df = pd.DataFrame([user_data])
        
        # Ensure all expected columns are present in the correct order
        for col in feature_cols:
            if col not in input_df.columns:
                # Add missing columns with default values (mean for numeric)
                input_df[col] = df[col].mean()
        
        # Reorder columns to match model expectations
        input_df = input_df[feature_cols]

        # Make prediction (no encoding needed as all features are already numeric)
        prediction = model.predict(input_df)[0]
        exam_score = round(prediction, 2)
        
        # Determine performance level based on exam score (0-100 scale)
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
        
        # Determine pass/fail status
        pass_status = "تێپەڕ" if exam_score >= 60 else "شکست"
        
        # Display result with improved styling
        st.markdown("---")
        st.markdown(f"""
            <div class="prediction-box">
                <h2>🎯 ئەنجامی پێشبینی</h2>
                <h1>{exam_score:.2f}</h1>
                <p style="font-size: 24px; margin: 15px 0;"><strong>{level}</strong></p>
                <p style="font-size: 20px; margin-top: 15px;">دۆخ: <strong>{pass_status}</strong></p>
                <p style="font-size: 16px; margin-top: 12px; opacity: 0.95;">نمرەی پێشبینیکراو (لە ١٠٠)</p>
            </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"❌ هەڵە لە پێشبینی کردندا: {str(e)}")
        st.info("تکایە دڵنیا ببەوە کە هەموو خانەکان بە دروستی پڕکراونەتەوە.")
        st.exception(e)

# Show academic info if requested
if st.session_state.get('page') == "academic":
    st.markdown("---")
    st.markdown("""
        <div style="background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%); border-left: 5px solid #0ea5e9; padding: 20px; border-radius: 10px; margin: 20px 0;">
            <h4 style="color: #0369a1; margin-top: 0; font-weight: 700;">📊 زانیاری کارایی ئەکادیمی</h4>
            <p style="color: #0c4a6e; margin: 8px 0; line-height: 1.6;"><strong>پێوەری نمرە:</strong> نمرەی پێشبینیکراو لە ٤٠ بۆ ١٠٠ خاڵ دەگۆڕێت.</p>
            <p style="color: #0c4a6e; margin: 8px 0; line-height: 1.6;"><strong>ئاستەکانی کارایی:</strong></p>
            <ul style="color: #0c4a6e; margin: 10px 0; padding-left: 20px;">
                <li><strong>نایاب (٩٠-١٠٠):</strong> کارایی نایاب، دەستکەوتنی بەرز</li>
                <li><strong>زۆر باش (٨٠-٨٩):</strong> کارایی بەهێز، لەسەروەی مامناوەند</li>
                <li><strong>باش (٧٠-٧٩):</strong> کارایی بەپێی چاوەڕوانی</li>
                <li><strong>مامناوەند (٦٠-٦٩):</strong> کارایی بەپێی پێویست، تێپەڕبوون</li>
                <li><strong>پێویستی بە باشترکردن هەیە (کەمتر لە ٦٠):</strong> لە خوار پێوەری تێپەڕبوون، پێویستی بە سەرنج</li>
            </ul>
            <p style="color: #0c4a6e; margin: 8px 0; line-height: 1.6;"><strong>پێوەری تێپەڕ/شکست:</strong> نمرەی ٦٠ یان زیاتر وەک تێپەڕبوون دادەنرێت.</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("← گەڕانەوە بۆ پێشبینی", use_container_width=True):
        st.session_state.page = "kurdish"
        st.rerun()

