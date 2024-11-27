import streamlit as st
from utils.mistral import MistralAPI
from utils.stable_diffusion import StableDiffusionAPI
from PIL import Image
import io
import random

def generate_pet_message(pet_name: str, comment: str) -> str:
    """Generate response message from pet using Mistral API"""
    mistral = MistralAPI()
    prompt = f"""As {pet_name}, write a deeply emotional and heartfelt response to your owner's message:
    "{comment}"

    Requirements for the response:
    1. Write at least 50 words
    2. Include specific details and memories from their message
    3. Express deep love, gratitude, and emotional connection
    4. Comfort them about your peaceful state in heaven
    5. Mention how you still watch over them
    6. Reference specific moments, habits, or shared experiences
    7. Include sensory details (like the feeling of their touch, your favorite treats, etc.)
    8. End with a reassuring and loving message
    
    Make the message so touching that it brings tears to their eyes, but also gives them comfort.
    Write only the message, without any additional text or quotation marks.
    """
    return mistral.generate_message(pet_name, comment)

def generate_image_prompt(pet_name: str, comment: str) -> str:
    """Generate image prompt based on user's message"""
    return f"""Same pet in heaven, heavenly background with soft glowing lights, 
        golden clouds, rainbow bridge, ethereal atmosphere, angelic surroundings, 
        keep the pet's face and features exactly the same, 
        only modify the background to heavenly scene, photorealistic"""

def show_step2():
    st.title("🌟 Heavenly Conversation")
    
    if 'pet_data' not in st.session_state or not st.session_state.pet_data['photo']:
        st.error("Please upload a pet photo first")
        if st.button("Go Back"):
            st.session_state.step = 1
            st.rerun()
        return

    # Center layout for better presentation
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Generate both message and image at the same time
        if ('pet_message' not in st.session_state.pet_data or 
            'generated_image' not in st.session_state.pet_data):
            with st.spinner("Creating heavenly memories..."):
                try:
                    # Generate message
                    message = generate_pet_message(
                        st.session_state.pet_data['name'],
                        st.session_state.pet_data['comment']
                    )
                    st.session_state.pet_data['pet_message'] = message
                    
                    # Generate image
                    sd_api = StableDiffusionAPI()
                    prompt = generate_image_prompt(
                        st.session_state.pet_data['name'],
                        st.session_state.pet_data['comment']
                    )
                    generated_image = sd_api.image_to_image(
                        st.session_state.pet_data['photo'],
                        prompt
                    )
                    st.session_state.pet_data['generated_image'] = generated_image
                    st.rerun()
                except Exception as e:
                    st.error(f"Error generating content: {str(e)}")
                    return
        
        # Display content
        if (st.session_state.pet_data.get('pet_message') and 
            st.session_state.pet_data.get('generated_image')):
            
            # Display message
            st.markdown("### Message from Your Pet")
            st.info(st.session_state.pet_data['pet_message'])
            
            # Display image
            st.markdown("### In Heaven")
            generated_img = Image.open(io.BytesIO(st.session_state.pet_data['generated_image']))
            st.image(generated_img, caption="Your Pet in Heaven", use_column_width=True)
            
            # Action buttons
            col4, col5 = st.columns(2)
            with col4:
                if st.button("Save Photo", use_container_width=True):
                    buf = io.BytesIO()
                    generated_img.save(buf, format='PNG')
                    st.download_button(
                        label="Download Photo",
                        data=buf.getvalue(),
                        file_name=f"{st.session_state.pet_data['name']}_in_heaven.png",
                        mime="image/png",
                        use_container_width=True
                    )
            
            with col5:
                if st.button("Journey to New World", use_container_width=True):
                    st.session_state.step = 3
                    st.rerun()

            st.markdown("""
            ---
            💫 **Tips**
            - The heavenly photo keeps your pet's appearance while adding divine surroundings
            - Save the photo as a precious memory
            - When ready, continue to the next journey
            """)