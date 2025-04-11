# import streamlit as st
# import google.generativeai as genai
# from gtts import gTTS
# import tempfile
# genai.configure(api_key="AIzaSyDydWxM_3IoML4ZPSe-YAlBQOZvXGCz8PI")
# model = genai.GenerativeModel('gemini-1.5-flash')
# st.title("🌐 Language Translator using Gemini ✨ + Voice-over 🔊")
# input_text = st.text_input("Type the Word or Sentence", "Hello")
# indian_languages = [
#     "Hindi", "Telugu", "Tamil", "Kannada", "Malayalam", "Bengali", "Gujarati",
#     "Punjabi", "Marathi", "Odia", "Assamese", "Manipuri", "Sanskrit", "Urdu",
#     "Konkani", "Bodo", "Dogri", "Maithili", "Santali", "Kashmiri", "Sindhi", "Nepali"
# ]
# selected_language = st.selectbox("Choose the language to translate into:", indian_languages)
# language_code_map = {
#     "Hindi": "hi", "Telugu": "te", "Tamil": "ta", "Kannada": "kn", "Malayalam": "ml",
#     "Bengali": "bn", "Gujarati": "gu", "Punjabi": "pa", "Marathi": "mr", "Odia": "or",
#     "Assamese": "as", "Urdu": "ur", "Nepali": "ne", "Sanskrit": "sa", "Konkani": "gom",
#     "Dogri": "doi", "Bodo": "brx", "Maithili": "mai", "Sindhi": "sd", "Kashmiri": "ks",
#     "Manipuri": "mni", "Santali": "sat", "English": "en"
# }
# if st.button("Translate"):
#     try:
#         prompt = f"Just give the accurate {selected_language} translation for: {input_text}\nDo not explain anything."
#         response = model.generate_content(prompt)
#         translated_text = response.text.strip()
#         st.write("**Translated Output:**", translated_text)
#         lang_code = language_code_map.get(selected_language, "hi")
#         tts = gTTS(text=translated_text, lang=lang_code)
#         with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
#             tts.save(fp.name)
#             st.audio(fp.name, format="audio/mp3")
#     except Exception as e:
#         st.error(f"Translation or Voice Error: {e}")
import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import tempfile

# Gemini API key
genai.configure(api_key="AIzaSyDydWxM_3IoML4ZPSe-YAlBQOZvXGCz8PI")
model = genai.GenerativeModel('gemini-1.5-flash')

# Page title and layout
st.set_page_config(page_title="Heritage Translator", layout="centered")
st.markdown(
    """
    <style>
    body {
        background-color: #fff8e7;
    }
    .title {
        font-family: 'Georgia', serif;
        color: #8B0000;
        text-align: center;
        font-size: 2.5rem;
        padding: 1rem 0;
    }
    .stTextInput > div > div > input {
        background-color: #fff5da;
        border: 2px solid #ff9933;
        border-radius: 8px;
        padding: 0.5rem;
    }
    .stSelectbox > div > div > div {
        background-color: #fff5da;
        border: 2px solid #ff9933;
        border-radius: 8px;
    }
    .stButton button {
        background-color: #ff9933;
        color: white;
        border: None;
        border-radius: 10px;
        padding: 0.5rem 1rem;
        font-weight: bold;
        transition: 0.3s ease-in-out;
    }
    .stButton button:hover {
        background-color: #d46a00;
        transform: scale(1.05);
    }
    .translated {
        background-color: #fef4dc;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #008000;
        font-size: 1.2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown('<div class="title">Language Translator + Voice-over 🔊</div>', unsafe_allow_html=True)

# Input
input_text = st.text_input("Type the Word or Sentence", "Hello")

# Language options
indian_languages = [
    "Hindi", "Telugu", "Tamil", "Kannada", "Malayalam", "Bengali", "Gujarati",
    "Punjabi", "Marathi", "Odia", "Assamese", "Manipuri", "Sanskrit", "Urdu",
    "Konkani", "Bodo", "Dogri", "Maithili", "Santali", "Kashmiri", "Sindhi", "Nepali"
]
selected_language = st.selectbox("Choose the language to translate into:", indian_languages)

language_code_map = {
    "Hindi": "hi", "Telugu": "te", "Tamil": "ta", "Kannada": "kn", "Malayalam": "ml",
    "Bengali": "bn", "Gujarati": "gu", "Punjabi": "pa", "Marathi": "mr", "Odia": "or",
    "Assamese": "as", "Urdu": "ur", "Nepali": "ne", "Sanskrit": "sa", "Konkani": "gom",
    "Dogri": "doi", "Bodo": "brx", "Maithili": "mai", "Sindhi": "sd", "Kashmiri": "ks",
    "Manipuri": "mni", "Santali": "sat", "English": "en"
}

# Translate
if st.button("Translate"):
    try:
        prompt = f"Just give the accurate {selected_language} translation for: {input_text}\nDo not explain anything."
        response = model.generate_content(prompt)
        translated_text = response.text.strip()
        st.markdown(f'<div class="translated"><b>Translated Output:</b> {translated_text}</div>', unsafe_allow_html=True)

        lang_code = language_code_map.get(selected_language, "hi")
        tts = gTTS(text=translated_text, lang=lang_code)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            st.audio(fp.name, format="audio/mp3")
    except Exception as e:
        st.error(f"Translation or Voice Error: {e}")
