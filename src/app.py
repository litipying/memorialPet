import streamlit as st
from config import check_env_variables

# 檢查環境變數
try:
    check_env_variables()
except EnvironmentError as e:
    st.error(str(e))
    st.stop()

st.set_page_config(
    page_title="Pet Memorial",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 設定全域樣式
st.markdown("""
<style>
    /* Hide menu and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Container max-width and responsive padding */
    .main > div {
        max-width: 1200px !important;
        margin: 0 auto;
        padding: 1rem;
    }
    
    /* Responsive padding for mobile */
    @media (max-width: 768px) {
        .main > div {
            padding: 0.5rem;
        }
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #ff6b6b;
        color: white;
        border-radius: 15px;
        padding: 0.3rem 1.5rem;
        border: none;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        width: 100%;
        max-width: 300px;
    }
    .stButton > button:hover {
        background-color: #ff5252;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* Card styling */
    .card {
        background-color: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    /* Title styling */
    h1 {
        color: #ff6b6b;
        font-size: clamp(1.8rem, 4vw, 2.2rem);
        text-align: center;
        margin-bottom: 1.5rem;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    h2, h3 {
        color: #2c3e50;
        margin-bottom: 1rem;
        font-size: clamp(1.2rem, 3vw, 1.5rem);
    }
    
    /* Info box styling */
    .stAlert {
        border-radius: 10px;
        border: none;
        padding: 0.8rem;
    }
    
    /* File uploader styling */
    .uploadedFile {
        border-radius: 10px;
        border: 2px dashed #ff6b6b;
        padding: 1rem;
        max-width: 100%;
    }
    
    /* Image styling */
    .stImage {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        max-width: 100%;
        height: auto;
    }
    
    /* Text input and text area styling */
    .stTextInput > div > div {
        border-radius: 10px;
        max-width: 100%;
    }
    .stTextArea > div > div {
        border-radius: 10px;
        max-width: 100%;
    }
    
    /* Spinner styling */
    .stSpinner > div {
        border-color: #ff6b6b;
    }
    
    /* Column responsiveness */
    @media (max-width: 768px) {
        [data-testid="column"] {
            width: 100% !important;
            margin-bottom: 1rem;
        }
    }
    
    /* Container spacing */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 1200px;
    }
    
    /* Message box styling */
    .stSuccess, .stInfo {
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        max-width: 100%;
    }
</style>
""", unsafe_allow_html=True)

def main():
    if 'step' not in st.session_state:
        st.session_state.step = 1
    
    if 'pet_data' not in st.session_state:
        st.session_state.pet_data = {
            'photo': None,
            'name': '',
            'comment': '',
            'generated_image': None,
            'new_pet_type': '',
            'new_pet_name': ''
        }
    
    if st.session_state.step == 1:
        from pages.step1 import show_step1
        show_step1()
    elif st.session_state.step == 2:
        from pages.step2 import show_step2
        show_step2()
    elif st.session_state.step == 3:
        from pages.step3 import show_step3
        show_step3()
    else:
        from pages.step4 import show_step4
        show_step4()

if __name__ == "__main__":
    main() 