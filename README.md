# Pet Memorial

A heartwarming application designed to help pet owners memorialize and remember their beloved pets who have crossed the rainbow bridge.

## The Concept & Value Behind Pet Memorial
Every pet owner shares a special bond with their furry friends, and cats, as beloved family members, hold a special place in many hearts. When a pet passes away, the sadness can be overwhelming. That's why we created Pet Memorial—a caring web application designed to help pet owners find comfort and cope with their grief.

## Features

### 1. Upload Memorial (Step 1)
- Upload a pet photo
- Enter pet's name
- Write a message to your pet
![img](https://github.com/litipying/memorialPet/blob/main/1/2.png)

### 2. Heaven Meeting (Step 2)
- Transform pet photos into heavenly images using AI technology
- Receive heartwarming messages from your pet
- Save generated photos
![img](https://github.com/litipying/memorialPet/blob/main/1/3.png)

### 3. Reincarnation Journey (Step 3)
- AI analysis of pet characteristics
- Generate pet's next life appearance
- Create a new name for the next life
![img](https://github.com/litipying/memorialPet/blob/main/1/4.png)

### 4. New Beginning (Step 4)
- Farewell message
- Start a new memorial journey
![img](https://github.com/litipying/memorialPet/blob/main/1/5.png)

## Technology Stack

- **AI Services**
  - Stable Diffusion API - For AI image generation
  - Mistral API - For AI text generation

- **Core Framework**
  - Streamlit - For building the web application interface

- **Image Processing**
  - Pillow (PIL) - For image handling and manipulation
  - OpenCV (cv2) - For image processing operations

- **Development Tools**
  - Docker - For containerization
  - Docker Compose - For multi-container orchestration

## Installation

1. Install Docker and Docker Compose:
   - For Docker: Follow the official Docker installation guide for your operating system:
     https://docs.docker.com/get-docker/
   - For Docker Compose: Follow the official Docker Compose installation guide:
     https://docs.docker.com/compose/install/

2. Get API Keys:
   - Stable Diffusion API Key:
     1. Visit https://platform.stability.ai/
     2. Sign up for an account
     3. Navigate to Account Settings
     4. Generate an API key

   - Mistral API Key:
     1. Visit https://mistral.ai/
     2. Create an account
     3. Go to API Keys section
     4. Generate a new API key

3. Set up environment variables:
   Create a `.env` file in the root directory and add your API keys:
```
STABILITY_API_KEY=your_stability_api_key
MISTRAL_API_KEY=your_mistral_api_key
```

4. Build and run the Docker containers:
```
docker-compose up --build
```

5. Access the application:
   Open your web browser and navigate to `http://localhost:8501`

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments
We thank the authors of the following projects for their excellent contributions!

- [Stable Diffusion API](https://platform.stability.ai/docs/api-reference)
- [Mistral API](https://console.mistral.ai/)
- [Streamlit](https://streamlit.io/)
- [Pillow (PIL)](https://pillow.readthedocs.io/en/stable/)
- [OpenCV (cv2)](https://opencv.org/)

## Our Development Journey
1. **Roles of Members**
   - **Li Tip Ying**: Handled the overall structure of the application using Streamlit, focusing on building the application interface.

   - **Lu Manman**: Integrated the AI functionalities and utilized the Stable Diffusion API for image generation. 

   - **Cho Ka Yan**: Integrated the Mistral API for text generation and implemented features that allow users to upload their pet photos.

2. **Weekly Progress**
   - **Week 1 - Idea development and research:**
   At the first week, our team focused on brainstorming and refining the concept for the Pet Memorial application. We took references from different pet platforms, exploring their features and themes to understand what elements resonate with users.

   - **Week 2 - Technology stack selection and initial setup:**
   We explored various technologies to determine the best stack for our application. After consideration, we chose the Stable Diffusion API for image generation and the Mistral API for text generation. We also set up our core structure using Streamlit and began development of the app's interface.

   - **Week 3 - Development and integration:**
   The third week focused on the development process. We implemented the core functionalities of the application, focusing on user experience.

   - **Week 4 - Testing and final adjustments:**
   The final week focused on continuing the app development and testing the application for functionality and usability. We also finalized the deployment process using Docker and Docker Compose to make our application ready. Happy to see our product and finally done!

3. **Challenges We Encountered:**
   We encountered challenges during the project, particularly due to our limited knowledge of Python, which made the development process more difficult for us. Navigating complex coding tasks, debugging errors, and integrating APIs can be tough without a good understanding of the language. We sought help from our classmates, and they were great at providing tips. We also relied on many online resources and tutorials to learn. Plus, our family and friends who are experienced in coding offered us technical advice, which helped us get through the tough spots. A big thanks to them!

4. **Potential of Pet Memorial for Future Development:**
   This project is our first attempt at creating an application focused on pets, and we see potential for further development. We imagined and discussed adding new features, like letting users upload real photos of their pets to generate cute illustrations or even animations that highlight their pets' unique traits and features. This would further give pet owners special keepsakes to remember their beloved companions (we looked into using ComfyUI, which could be good for the development). We look forward to exploring how we can bring these ideas to life in our future projects.