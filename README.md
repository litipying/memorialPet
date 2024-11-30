# Pet Memorial

A heartwarming application designed to help pet owners memorialize and remember their beloved pets who have crossed the rainbow bridge.

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