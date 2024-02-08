import streamlit as st
from transformers import pipeline
import requests, time

st.set_page_config(  
    page_title="Copilot Language Translator", 
    page_icon="🧊",
    layout="centered",  
) 

# Global styles  
st.markdown("""  
    <style>  
    .main {background-color: #f0f0f5;}  
    .stButton>button {  
        background-color: #4CAF50; /* Green background */  
        color: #ffffff; /* White text */  
        padding: 10px 24px;  
        border-radius: 5px;  
        border: 2px solid #4CAF50; /* Green border */  
    }  
    .stButton>button:hover {  
        background-color: #45a049; /* Darker green background */  
    }  
    .upload-section {background-color: #e6e6fa; padding: 2rem; margin: 1rem 0; border-radius: 10px;}  
    .result-section {background-color: #f5f5f5; padding: 2rem; margin-top: 1rem; border-radius: 10px; color: #333;}  
    .stTextInput>div>div>input {  
        background-color: #fff;  
        border-radius: 5px;  
        border: 1px solid #ced4da;  
    }  
    .centralized {text-align: center;}  
    </style>  
""", unsafe_allow_html=True)  

# Header  
st.markdown("<h1 style='color: blue; text-align: left;'>Copilot Language Translator</h1>", unsafe_allow_html=True) 

# Upload section  
st.markdown("<div class='upload-section'>", unsafe_allow_html=True)  
uploaded_file = st.file_uploader("Upload a english json file for translation", type=["json"])

# Text box for specifying languages
languages_to_translate = st.text_input("Enter the target langiuage codes using comma-separated", "hi")
st.markdown("</div>", unsafe_allow_html=True)  # End of upload section

st.markdown("<div class='centralized'>", unsafe_allow_html=True)  
translate_button = st.button("Translate")  

def typewriter(text: str, speed: int):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.markdown(curr_full_text)
        time.sleep(1 / speed)
    
# Translate button
if translate_button:
# Result section with custom theme  
    st.markdown("""  
        <div style='background-color: #e0e0ef; padding: 10px; border-radius: 5px; margin-top: 20px;'>  
        <h3 style='color: #262730; text-align: center;'>Translation Result</h3>  
    """, unsafe_allow_html=True) 

    try:
         # Check if a file is uploaded
        if uploaded_file is not None:
            
            # Read the content of the uploaded file
            file_content = uploaded_file.getvalue()
            
            #post call
            # url = "https://euacedcopilotlanguagetranslatorazfunc01.azurewebsites.net/api/CopillotLanguageTranslator"
            url ="https://euacedcopilotlanguagetranslatorazfunc01.azurewebsites.net/api/CopillotLanguageTranslator?code=-EaJrbkiZ0SCKIXvoMN8WNBHBZOfr1jsVEQ7d7qHoKjOAzFu1NSlpg=="
            # url = "http://localhost:7071/api/CopillotLanguageTranslator"

            # define the payload
            payload = {'language':languages_to_translate}
            
            # define the file data
            files=[('file',(uploaded_file.name,file_content,uploaded_file.type))]
            headers = {}
            
            typewriter(text=f"\nThe Translation in progress and it will take a minute time. Please maintain some patience and do not click the translate button again.\n", speed=10)
            # st.write(f"The Translation in progress and it will take a minute time. Please maintain some patience and do not click the translate button again.")
            
            response = requests.request("POST", url, headers=headers, data=payload, files=files)
            
            typewriter(text=f"\nTranslation to '{languages_to_translate}' is succesful. Please download the file below\n", speed=10)
            # st.write(f"Translation to '{languages_to_translate}' is succesful. Please download the file below")        
            
            # download button
            st.download_button(
                label = "{} localization file.json".format(languages_to_translate),
                data = response.content,
                file_name="{} localization file.json".format(languages_to_translate),
                mime=uploaded_file.type,
                on_click=lambda: st.success("Thanks for downloading!") )
            
        else:
            st.warning("Please upload a json file before translating.")
    
    except Exception as e:  
            # Show error message if something goes wrong  
            st.error(f"An error occurred during translation: {e}")  
            
st.markdown("</div>", unsafe_allow_html=True)  # End of result section  



# Footer with copyright information  
st.markdown("---")  
st.markdown("<div style='color:grey; font-size:small'>Copyright © Copilot Language Translator. All rights reserved.</div>", unsafe_allow_html=True)  