import streamlit as st 
from dotenv import load_dotenv
import os 
#import openai
from diffusers import StableDiffusionPipeline
import torch

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

#function to generate AI based images using OpenAI Dall-E
def generate_images_using_openai(text):
    response = openai.Image.create(prompt= text, n=1, size="512x512")
    image_url = response['data'][0]['url']
    return image_url


#function to generate AI based images using Huggingface Diffusers
def generate_images_using_huggingface_diffusers(text):
    pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
    pipe = pipe.to("cuda")
    prompt = text
    image = pipe(prompt).images[0] 
    return image

#Streamlit Code
choice = st.sidebar.selectbox("Select your choice", ["Home", "DALL-E", "Huggingface Diffusers"])

if choice == "Home":
    st.title("AI Image Generation App")
    with st.expander("About the App"):
        st.write("This is a simple image generation app that uses AI to generates images from text prompt.")

elif choice == "DALL-E":
    st.subheader("Image generation using Open AI's DALL-E")
    input_prompt = st.text_input("Enter your text prompt")
    if input_prompt is not None:
        if st.button("Generate Image"):
            image_url = generate_images_using_openai(input_prompt)
            st.image(image_url, caption="Generated by DALL-E")

elif choice == "Huggingface Diffusers":
    st.subheader("Image generation using Huggingface Diffusers")
    input_prompt = st.text_input("Enter your text prompt")
    if input_prompt is not None:
        if st.button("Generate Image"):
            image_output = generate_images_using_huggingface_diffusers(input_prompt)
            st.info("Generating image.....")
            st.success("Image Generated Successfully")
            st.image(image_output, caption="Generated by Huggingface Diffusers")
