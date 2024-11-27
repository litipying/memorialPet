import streamlit as st
from utils.mistral import MistralAPI
from utils.stable_diffusion import StableDiffusionAPI
from PIL import Image
import io
import random

def generate_new_name() -> str:
    """Generate new pet name"""
    prefixes = ["Little", "Big", "Sweet", "Happy", "Lucky", "Lovely"]
    names = ["Joy", "Hope", "Star", "Angel", "Blessing", "Fortune"]
    return random.choice(prefixes) + " " + random.choice(names)

def generate_new_pet_prompt(characteristics: dict) -> str:
    """Generate new pet image prompt based on characteristics"""
    return f"""A new pet with following characteristics: 
        {characteristics['characteristics']}, 
        showing {characteristics['personality']}, 
        but as a different type of pet, 
        high quality, photorealistic, detailed texture, 
        warm lighting, professional photography"""

def show_step3():
    st.title("🌈 Reincarnation Journey")
    
    if 'pet_data' not in st.session_state or not st.session_state.pet_data['photo']:
        st.error("Please complete previous steps first")
        if st.button("Go Back"):
            st.session_state.step = 1
            st.rerun()
        return

    # Center layout for better presentation
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### Next Life")
        
        # Automatically generate new life if not already generated
        if 'next_life_image' not in st.session_state.pet_data:
            with st.spinner("Creating new life form..."):
                try:
                    mistral = MistralAPI()
                    characteristics = mistral.analyze_pet_characteristics(
                        st.session_state.pet_data['comment']
                    )
                    
                    sd_api = StableDiffusionAPI()
                    prompt = generate_new_pet_prompt(characteristics)
                    new_image = sd_api.text_to_image(prompt)
                    
                    new_name = generate_new_name()
                    
                    st.session_state.pet_data['next_life_image'] = new_image
                    st.session_state.pet_data['new_pet_name'] = new_name
                    st.session_state.pet_data['new_pet_type'] = characteristics['pet_type']
                    
                    st.rerun()
                except Exception as e:
                    st.error(f"Error generating new form: {str(e)}")
        
        if st.session_state.pet_data.get('next_life_image'):
            new_image = Image.open(io.BytesIO(st.session_state.pet_data['next_life_image']))
            st.image(new_image, caption="New Beginning", use_column_width=True)
            
            st.success(f"In the next life, {st.session_state.pet_data['name']} will be a {st.session_state.pet_data['new_pet_type']} named {st.session_state.pet_data['new_pet_name']}")
            
            col4, col5 = st.columns(2)
            with col4:
                if st.button("Stay in Heaven", use_container_width=True):
                    st.session_state.step = 2
                    st.rerun()
            
            with col5:
                if st.button("Send to New World", use_container_width=True):
                    st.session_state.step = 4
                    st.rerun()

        st.markdown("""
        ---
        🌟 **Tips**
        - Each life is unique
        - Reincarnation is a new beginning
        - You can choose to let your pet stay in heaven or start a new life
        """) 