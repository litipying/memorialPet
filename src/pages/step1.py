import streamlit as st
from PIL import Image
import io

def show_step1():
    st.title("🌈 Pet Memorial")
    
    # Using two-column layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Upload Pet Photo")
        uploaded_file = st.file_uploader(
            "Choose your favorite photo",
            type=['png', 'jpg', 'jpeg'],
            help="Supports PNG and JPG formats"
        )
        
        if uploaded_file is not None:
            # Display uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Your Pet's Photo", use_column_width=True)
            
            # Store image in session state
            buf = io.BytesIO()
            image.save(buf, format='PNG')
            st.session_state.pet_data['photo'] = buf.getvalue()
    
    with col2:
        st.markdown("### Pet Information")
        
        # Pet name input
        pet_name = st.text_input(
            "Pet's Name",
            value=st.session_state.pet_data.get('name', ''),
            placeholder="Enter your pet's name",
            help="This name will be used to generate personalized messages"
        )
        
        # Message input
        pet_comment = st.text_area(
            "Message to Your Pet",
            value=st.session_state.pet_data.get('comment', ''),
            placeholder="Write a message to your pet...",
            help="These words will help create special memories",
            height=200
        )
        
        # Update session state
        st.session_state.pet_data['name'] = pet_name
        st.session_state.pet_data['comment'] = pet_comment
        
        # Next step button
        if st.button("Begin Memorial Journey", use_container_width=True):
            if not uploaded_file:
                st.error("Please upload a photo of your pet")
            elif not pet_name:
                st.error("Please enter your pet's name")
            elif not pet_comment:
                st.error("Please write a message to your pet")
            else:
                st.session_state.step = 2
                st.rerun()

    # Add warm tips
    st.markdown("""
    ---
    💝 **Tips**
    - Choose a photo that best shows your pet's characteristics
    - Clearer photos will yield better results
    - Express your feelings with heartfelt words
    """) 