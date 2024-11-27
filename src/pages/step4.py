import streamlit as st

def show_step4():
    st.title("🌟 New Beginning")
    
    # Center all content
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Display message with card style
        st.markdown("""
        <div style='padding: 2rem; background-color: rgba(255, 255, 255, 0.1); border-radius: 1rem; text-align: center;'>
            <h2 style='color: #ff6b6b;'>Farewell and Rebirth</h2>
            <p style='font-size: 1.2rem; margin: 2rem 0;'>
                {} is happy in heaven,<br>
                Now it's time for a new journey.<br>
                Until we meet again ❤️
            </p>
        </div>
        """.format(st.session_state.pet_data['name']), unsafe_allow_html=True)
        
        # Add some space before the button
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Center-aligned button with custom CSS
        st.markdown("""
        <style>
            div[data-testid="column"] {
                text-align: center;
            }
            div[data-testid="column"] > div {
                display: flex;
                justify-content: center;
            }
            div.stButton > button {
                display: inline-flex;
                margin: 0 auto;
            }
        </style>
        """, unsafe_allow_html=True)
        
        if st.button("Start New Memorial"):
            # Clear all data
            st.session_state.pet_data = {
                'photo': None,
                'name': '',
                'comment': '',
                'generated_image': None,
                'next_life_image': None,
                'new_pet_name': '',
                'new_pet_type': ''
            }
            st.session_state.step = 1
            st.rerun()
        
        # Add some space before the footer
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Add decorative elements
        st.markdown("""
        <div style='text-align: center; color: #666;'>
            <p>🌈 May all pets live happily in heaven</p>
            <p>💝 Thank you for the beautiful memories you created together</p>
        </div>
        """, unsafe_allow_html=True) 