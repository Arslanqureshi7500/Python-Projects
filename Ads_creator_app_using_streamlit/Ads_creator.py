import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
import tiktoken

# Load environment variables
load_dotenv()

api_key = "Your API Key"
base_url = "https://api.openai.com/v1"
model = 'gpt-3.5-turbo'
st.title('Real Estate Ads Creator')
st.header('To Create Ads for your profolio')

class ConversationBot:
    def __init__(self, api_key,
                 base_url=base_url,
                 model=model,
                 system_message="""You are a helpful marketing assistant for DigiTech Synergy.""",
                 max_history=5,
                 token_budget=4096,
                 ):
        self.client = OpenAI(api_key=api_key)
        self.client.base_url = base_url
        self.model = model
        self.system_message = system_message
        self.conversation_history = [{"role": "system", "content": self.system_message}]
        self.max_history = max_history
        self.token_budget = token_budget

    def enforce_history_limit(self):
        while len(self.conversation_history) > self.max_history:
            self.conversation_history.pop(1)

    def chat_completion(self, prompt, temperature=0.7, max_tokens=500):
        self.conversation_history.append({"role": "user", "content": prompt})
        response = self.client.chat.completions.create(model=self.model, messages=self.conversation_history)
        ai_response = response.choices[0].message.content
        self.conversation_history.append({"role": "assistant", "content": ai_response})
        self.enforce_history_limit()
        return ai_response

system_message = """
You are a post or advertisement creator for real estate properties agencies.
Title
I'm a real estate agency my name is Patriot Real Estate looking to create captivating and effective advertising materials for my agency. Can you help me brainstorm and generate persuasive ad copy that resonates with both buyers and sellers?

Specific details to include:
bedroom specification:
washrooms:
price
location
ownership status
mention property facilities in villa or apartment or townhouse.
enlist key properties detail
enlist feature/amenities i.e. features, health and fitness, RECREATION AND FAMILY,CLEANING AND MAINTENANCE, business and security, laundry, technology.

Target audience: Be specific about demographics and interests for dubai UAE location audience.
Unique selling proposition (USP): Highlight Patriot real estate strengths and expertise.
Desired tone and style: the society to be informative, playful, luxurious, or something else?

Additional tips:
Be clear for your dream house.
Don't be afraid to experiment and try different approaches.
Call to action (CTA): What do you want people to do after seeing your ad? 
Visit our website, schedule a consultation, patriort.ae Company name: Patriot Real Estate RERA 
ORN: 17286 Address: Office 1401, Damac Executive Heights, Barsha Heights, Dubai 
Office phone no: View Contact Detail Office fax no: View Contact Detail Primary 
email: Send e-mail Website: www.patriot.ae

For More Details Or Viewing, Call Us -
"""

agency_name = st.text_input("Agency Name", value="Patriot Real Estate")
project_name = st.text_input("Project Name", value="Project X")
Nos_room = st.text_input("Number of Rooms", value="3")
Nos_washrooms = st.text_input("Number of Washrooms", value="2")
area = st.text_input("Area (sqft)", value="2000")
bua = st.text_input("Built-up Area", value="1800")
price = st.text_input("Price", value="1000000")
location = st.text_input("Location", value="Dubai")

conv_manager = ConversationBot(api_key=api_key, system_message=system_message)

if st.button("Submit"):
    prompt1 = f"Please write a selling post/advertisement with an eye-catching title with the following details, and introduction detail at least 5 lines {agency_name}, {project_name}, {Nos_room}, {Nos_washrooms}, {area}, {bua}, {price}, {location}"

    response = conv_manager.chat_completion(prompt1)
    st.write(f'{response}')
