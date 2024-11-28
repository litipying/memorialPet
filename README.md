# Pet Memorial

A heartwarming application designed to help pet owners memorialize and remember their beloved pets who have crossed the rainbow bridge.

## Features

### 1. Upload Memorial (Step 1)
- Upload a pet photo
- Enter pet's name
- Write a message to your pet
![img](https://github.com/litipying/memorialPet/blob/main/1/pet%20meorial%20page.png)

### 2. Heaven Meeting (Step 2)
- Transform pet photos into heavenly images using AI technology
- Receive heartwarming messages from your pet
- Save generated photos
![img](https://github.com/litipying/memorialPet/blob/main/1/2.png](https://github.com/litipying/memorialPet/blob/main/1/3.png)

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

- Frontend: Streamlit
- AI Services:
  - Stable Diffusion API (Image Generation)
  - Mistral API (Text Generation)
- Containerization: Docker & Docker Compose

## Installation

1. Install Docker and Docker Compose:
   - For Docker: Follow the official Docker installation guide for your operating system:
     https://docs.docker.com/get-docker/
   - For Docker Compose: Follow the official Docker Compose installation guide:
     https://docs.docker.com/compose/install/

2. Set up environment variables:
   Create a `.env` file in the root directory and add your API keys:
```
STABILITY_API_KEY=your_stability_api_key
MISTRAL_API_KEY=your_mistral_api_key
```

3. Build and run the Docker containers:
```
docker-compose up --build
```

4. Access the application:
   Open your web browser and navigate to `http://localhost:8501`

## Acknowledgments

- Thanks to Stability AI for their Stable Diffusion API
- Thanks to Mistral for their Mistral API
- Special thanks to all pet owners who inspire us to create this memorial application
