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

# Custom CSS for better UI with indigo theme
st.markdown("""
    <style>
    /* Main Header with Indigo Gradient */
    .main-header {
        text-align: center;
        padding: 30px 20px;
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #6366f1 100%);
        border-radius: 15px;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(79, 70, 229, 0.3);
        border: 1px solid rgba(99, 102, 241, 0.2);
    }
    .main-header h1 {
        color: #ffffff;
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        letter-spacing: -0.5px;
    }
    .author-name {
        text-align: center;
        color: #e0e7ff;
        font-size: 16px;
        font-style: italic;
        margin-top: 15px;
        font-weight: 500;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
    }
    
    /* Section Headers with Indigo Accent */
    .section-header {
        background: linear-gradient(90deg, rgba(79, 70, 229, 0.1) 0%, rgba(99, 102, 241, 0.05) 100%);
        padding: 15px 20px;
        border-radius: 8px;
        margin: 25px 0 15px 0;
        border-left: 5px solid #4f46e5;
        box-shadow: 0 2px 8px rgba(79, 70, 229, 0.1);
    }
    .section-header h3 {
        color: #4f46e5;
        margin: 0;
        font-weight: 600;
        font-size: 1.3rem;
    }
    
    /* Dark theme support */
    @media (prefers-color-scheme: dark) {
        .section-header {
            background: linear-gradient(90deg, rgba(99, 102, 241, 0.2) 0%, rgba(79, 70, 229, 0.1) 100%);
            border-left-color: #818cf8;
        }
        .section-header h3 {
            color: #a5b4fc;
        }
    }
    
    /* Input styling */
    .stSelectbox > div > div {
        border-radius: 8px;
    }
    .stNumberInput > div > div > input {
        border-radius: 8px;
    }
    
    /* Field spacing for better alignment */
    .field-group {
        margin-bottom: 20px;
        min-height: 80px;
    }
    .field-group p {
        margin-bottom: 8px;
        font-size: 14px;
    }
    
    /* Consistent spacing for form elements */
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column"] > div {
        margin-bottom: 1rem;
    }
    
    /* Better column alignment */
    .stColumn {
        padding: 0 10px;
    }
    
    /* Consistent input heights */
    .stSelectbox, .stNumberInput {
        margin-bottom: 1.5rem;
    }
    
    /* Prediction result box */
    .prediction-box {
        text-align: center;
        padding: 40px;
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 50%, #6366f1 100%);
        border-radius: 15px;
        color: white;
        margin: 30px 0;
        box-shadow: 0 15px 35px rgba(79, 70, 229, 0.4);
        border: 1px solid rgba(99, 102, 241, 0.3);
    }
    .prediction-box h2 {
        color: #ffffff;
        margin-bottom: 20px;
        font-weight: 600;
    }
    .prediction-box h1 {
        font-size: 56px;
        margin: 25px 0;
        font-weight: 700;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);
    }
    .prediction-box p {
        font-size: 20px;
        margin-top: 15px;
        opacity: 0.95;
    }
    
    /* General improvements */
    .stForm {
        background-color: transparent;
    }
    </style>
""", unsafe_allow_html=True)

# Load model & encoders
model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")

# Header with author name
st.markdown("""
    <div class="main-header">
        <h1>🎓 Student Performance Prediction System</h1>
        <p class="author-name">Developed by Ahmad Omar</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# Load dataset to detect columns
df = pd.read_excel("Students_Performance_data_set.xlsx")
target_col = "What is your current CGPA?"
cols = df.drop(target_col, axis=1).columns

user_data = {}

# Helper function to safely get sorted unique values (handles NaN)
def get_sorted_options(series):
    unique_vals = series.dropna().unique().tolist()
    try:
        return sorted([val for val in unique_vals if pd.notna(val)])
    except TypeError:
        return sorted([str(val) for val in unique_vals if pd.notna(val)])

# Create a single form with all fields
with st.form("prediction_form"):
    # Section 1: Basic Information
    st.markdown('<div class="section-header"><h3>👤 Basic Information</h3></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**What is your gender?**")
        user_data['Gender'] = st.selectbox(
            "Select one:",
            get_sorted_options(df['Gender']),
            key="gender",
            label_visibility="collapsed"
        )
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.write("**How old are you?**")
        user_data['Age'] = st.number_input(
            "Enter age:",
            min_value=int(df['Age'].min()),
            max_value=int(df['Age'].max()),
            value=int(df['Age'].mean()),
            step=1,
            key="age",
            label_visibility="visible"
        )
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.write("**What year did you get admitted to university?**")
        user_data['University Admission year'] = st.number_input(
            "Enter year:",
            min_value=int(df['University Admission year'].min()),
            max_value=int(df['University Admission year'].max()),
            value=int(df['University Admission year'].mean()),
            step=1,
            key="admission_year",
            label_visibility="visible"
        )
    
    with col2:
        st.write("**What year did you pass H.S.C?**")
        user_data['H.S.C passing year'] = st.number_input(
            "Enter year:",
            min_value=int(df['H.S.C passing year'].min()),
            max_value=int(df['H.S.C passing year'].max()),
            value=int(df['H.S.C passing year'].mean()),
            step=1,
            key="hsc_year",
            label_visibility="visible"
        )
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.write("**What program are you studying?**")
        user_data['Program'] = st.selectbox(
            "Select one:",
            get_sorted_options(df['Program']),
            key="program",
            label_visibility="collapsed"
        )
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.write("**What is your current semester?**")
        user_data['Current Semester'] = st.number_input(
            "Enter semester:",
            min_value=int(df['Current Semester'].min()),
            max_value=int(df['Current Semester'].max()),
            value=int(df['Current Semester'].mean()),
            step=1,
            key="semester",
            label_visibility="visible"
        )
    
    st.markdown("---")
    
    # Section 2: Academic Information
    st.markdown('<div class="section-header"><h3>📚 Academic Information</h3></div>', unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    
    with col3:
        st.write("**Do you have a meritorious scholarship?**")
        user_data['Do you have meritorious scholarship ?'] = st.selectbox(
            "Select one:",
            get_sorted_options(df['Do you have meritorious scholarship ?']),
            key="scholarship",
            label_visibility="collapsed"
        )
        st.write("**What is your English language proficiency status?**")
        user_data['Status of your English language proficiency'] = st.selectbox(
            "Select one:",
            get_sorted_options(df['Status of your English language proficiency']),
            key="english_proficiency",
            label_visibility="collapsed"
        )
        st.write("**What is your average attendance in class?**")
        user_data['Average attendance on class'] = st.selectbox(
            "Select one:",
            get_sorted_options(df['Average attendance on class']),
            key="attendance",
            label_visibility="collapsed"
        )
        st.write("**What was your previous SGPA?**")
        user_data['What was your previous SGPA?'] = st.number_input(
            "Enter SGPA (0-4):",
            min_value=0.0,
            max_value=4.0,
            value=float(df['What was your previous SGPA?'].mean()),
            step=0.01,
            key="previous_sgpa",
            label_visibility="visible"
        )
    
    with col4:
        st.write("**Did you ever fall in probation?**")
        user_data['Did you ever fall in probation?'] = st.selectbox(
            "Select one:",
            get_sorted_options(df['Did you ever fall in probation?']),
            key="probation",
            label_visibility="collapsed"
        )
        st.write("**Did you ever get suspension?**")
        user_data['Did you ever got suspension?'] = st.selectbox(
            "Select one:",
            get_sorted_options(df['Did you ever got suspension?']),
            key="suspension",
            label_visibility="collapsed"
        )
        st.write("**Do you attend teacher consultancy for academic problems?**")
        user_data['Do you attend in teacher consultancy for any kind of academical problems?'] = st.selectbox(
            "Select one:",
            get_sorted_options(df['Do you attend in teacher consultancy for any kind of academical problems?']),
            key="consultancy",
            label_visibility="collapsed"
        )
        st.write("**How many credits have you completed?**")
        user_data['How many Credit did you have completed?'] = st.number_input(
            "Enter credits:",
            min_value=int(df['How many Credit did you have completed?'].min()),
            max_value=int(df['How many Credit did you have completed?'].max()),
            value=int(df['How many Credit did you have completed?'].mean()),
            step=1,
            key="credits",
            label_visibility="visible"
        )
    
    st.markdown("---")
    
    # Section 3: Study Habits
    st.markdown('<div class="section-header"><h3>📖 Study Habits</h3></div>', unsafe_allow_html=True)
    col5, col6 = st.columns(2)
    
    with col5:
        st.write("**How many hours do you study daily?**")
        user_data['How many hour do you study daily?'] = st.number_input(
            "Enter hours:",
            min_value=int(df['How many hour do you study daily?'].min()),
            max_value=int(df['How many hour do you study daily?'].max()),
            value=int(df['How many hour do you study daily?'].mean()),
            step=1,
            key="study_hours",
            label_visibility="visible"
        )
        st.write("**How many times do you sit for study in a day?**")
        user_data['How many times do you seat for study in a day?'] = st.number_input(
            "Enter number:",
            min_value=int(df['How many times do you seat for study in a day?'].min()),
            max_value=int(df['How many times do you seat for study in a day?'].max()),
            value=int(df['How many times do you seat for study in a day?'].mean()),
            step=1,
            key="study_sessions",
            label_visibility="visible"
        )
        st.write("**What is your preferable learning mode?**")
        user_data['What is your preferable learning mode?'] = st.selectbox(
            "Select one:",
            get_sorted_options(df['What is your preferable learning mode?']),
            key="learning_mode",
            label_visibility="collapsed"
        )
    
    with col6:
        st.write("**How many hours do you spend daily on skill development?**")
        user_data['How many hour do you spent daily on your skill development?'] = st.number_input(
            "Enter hours:",
            min_value=int(df['How many hour do you spent daily on your skill development?'].min()),
            max_value=int(df['How many hour do you spent daily on your skill development?'].max()),
            value=int(df['How many hour do you spent daily on your skill development?'].mean()),
            step=1,
            key="skill_hours",
            label_visibility="visible"
        )
        st.write("**What skills do you have?**")
        user_data['What are the skills do you have ?'] = st.selectbox(
            "Select one:",
            get_sorted_options(df['What are the skills do you have ?']),
            key="skills",
            label_visibility="collapsed"
        )
        st.write("**What is your interested area?**")
        user_data['What is you interested area?'] = st.selectbox(
            "Select one:",
            get_sorted_options(df['What is you interested area?']),
            key="interested_area",
            label_visibility="collapsed"
        )
    
    st.markdown("---")
    
    # Section 4: Technology & Transportation
    st.markdown('<div class="section-header"><h3>💻 Technology & Transportation</h3></div>', unsafe_allow_html=True)
    col7, col8 = st.columns(2)
    
    with col7:
        st.write("**Do you use a smartphone?**")
        user_data['Do you use smart phone?'] = st.selectbox(
            "Select one:",
            get_sorted_options(df['Do you use smart phone?']),
            key="smartphone",
            label_visibility="collapsed"
        )
        st.write("**Do you have a personal computer?**")
        user_data['Do you have personal Computer?'] = st.selectbox(
            "Select one:",
            get_sorted_options(df['Do you have personal Computer?']),
            key="computer",
            label_visibility="collapsed"
        )
    
    with col8:
        st.write("**Do you use university transportation?**")
        user_data['Do you use University transportation?'] = st.selectbox(
            "Select one:",
            get_sorted_options(df['Do you use University transportation?']),
            key="transportation",
            label_visibility="collapsed"
        )
        st.write("**How many hours do you spend daily on social media?**")
        user_data['How many hour do you spent daily in social media?'] = st.number_input(
            "Enter hours:",
            min_value=int(df['How many hour do you spent daily in social media?'].min()),
            max_value=int(df['How many hour do you spent daily in social media?'].max()),
            value=int(df['How many hour do you spent daily in social media?'].mean()),
            step=1,
            key="social_media_hours",
            label_visibility="visible"
        )
    
    st.markdown("---")
    
    # Section 5: Personal & Lifestyle
    st.markdown('<div class="section-header"><h3>👥 Personal & Lifestyle</h3></div>', unsafe_allow_html=True)
    col9, col10 = st.columns(2)
    
    with col9:
        st.write("**What is your relationship status?**")
        user_data['What is your relationship status?'] = st.selectbox(
            "Select one:",
            get_sorted_options(df['What is your relationship status?']),
            key="relationship",
            label_visibility="collapsed"
        )
        st.write("**Are you engaged with any co-curriculum activities?**")
        user_data['Are you engaged with any co-curriculum activities?'] = st.selectbox(
            "Select one:",
            get_sorted_options(df['Are you engaged with any co-curriculum activities?']),
            key="co_curriculum",
            label_visibility="collapsed"
        )
        st.write("**With whom are you living?**")
        user_data['With whom you are living with?'] = st.selectbox(
            "Select one:",
            get_sorted_options(df['With whom you are living with?']),
            key="living_with",
            label_visibility="collapsed"
        )
    
    with col10:
        st.write("**Do you have any health issues?**")
        user_data['Do you have any health issues?'] = st.selectbox(
            "Select one:",
            get_sorted_options(df['Do you have any health issues?']),
            key="health_issues",
            label_visibility="collapsed"
        )
        st.write("**Do you have any physical disabilities?**")
        user_data['Do you have any physical disabilities?'] = st.selectbox(
            "Select one:",
            get_sorted_options(df['Do you have any physical disabilities?']),
            key="disabilities",
            label_visibility="collapsed"
        )
        st.write("**What is your monthly family income?**")
        user_data['What is your monthly family income?'] = st.number_input(
            "Enter income:",
            min_value=int(df['What is your monthly family income?'].min()),
            max_value=int(df['What is your monthly family income?'].max()),
            value=int(df['What is your monthly family income?'].mean()),
            step=1000,
            key="income",
            label_visibility="visible"
        )
    
    # Submit button at the bottom
    st.markdown("---")
    submitted = st.form_submit_button("🔮 Predict Performance Accuracy", use_container_width=True, type="primary")

if submitted:
    try:
        # Convert input to DataFrame
        input_df = pd.DataFrame([user_data])
        
        # Get all columns that the model expects (all columns except target)
        expected_cols = df.drop(target_col, axis=1).columns.tolist()
        
        # Ensure all expected columns are present in the correct order
        for col in expected_cols:
            if col not in input_df.columns:
                # Add missing columns with default values
                if df[col].dtype == 'object':
                    input_df[col] = df[col].mode()[0] if len(df[col].mode()) > 0 else ''
                else:
                    input_df[col] = df[col].mean()
        
        # Reorder columns to match model expectations
        input_df = input_df[expected_cols]

        # Encode categorical
        for col, enc in encoders.items():
            if col in input_df:
                input_df[col] = enc.transform(input_df[col].astype(str))

        prediction = model.predict(input_df)[0]
        
        # Convert CGPA (0-4.0) to percentage (0-100%)
        percentage = (prediction / 4.0) * 100
        cgpa_value = prediction
        
        # Determine performance level
        if percentage >= 90:
            level = "Excellent"
        elif percentage >= 80:
            level = "Very Good"
        elif percentage >= 70:
            level = "Good"
        elif percentage >= 60:
            level = "Average"
        else:
            level = "Needs Improvement"
        
        # Display result with indigo styling
        st.markdown("---")
        st.markdown(f"""
            <div class="prediction-box">
                <h2>🎯 Prediction Result</h2>
                <h1>{percentage:.2f}%</h1>
                <p style="font-size: 22px; margin: 10px 0;"><strong>{level}</strong></p>
                <p style="font-size: 18px; margin-top: 15px;">Predicted CGPA: {cgpa_value:.2f} / 4.0</p>
                <p style="font-size: 16px; margin-top: 10px; opacity: 0.9;">This represents the student's expected academic performance level</p>
            </div>
        """, unsafe_allow_html=True)
        
    except Exception as e:
        st.error(f"❌ Error making prediction: {str(e)}")
        st.info("Please check that all fields are filled correctly.")
        st.exception(e)
