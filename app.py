import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import tempfile
genai.configure(api_key="AIzaSyDydWxM_3IoML4ZPSe-YAlBQOZvXGCz8PI")
model = genai.GenerativeModel('gemini-1.5-flash')
st.title("🌐 Language Translator using Gemini ✨ + Voice-over 🔊")
input_text = st.text_input("Type the Word or Sentence", "Hello")
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
if st.button("Translate"):
    try:
        prompt = f"Just give the accurate {selected_language} translation for: {input_text}\nDo not explain anything."
        response = model.generate_content(prompt)
        translated_text = response.text.strip()
        st.write("**Translated Output:**", translated_text)
        lang_code = language_code_map.get(selected_language, "hi")
        tts = gTTS(text=translated_text, lang=lang_code)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts.save(fp.name)
            st.audio(fp.name, format="audio/mp3")
    except Exception as e:
        st.error(f"Translation or Voice Error: {e}")
# import streamlit as st
# import google.generativeai as genai
# from gtts import gTTS
# import tempfile

# # Configure API
# genai.configure(api_key="YOUR_API_KEY")
# model = genai.GenerativeModel('gemini-1.5-flash')

# # Page settings
# st.set_page_config(page_title="Heritage Language Translator", layout="centered")

# # Custom CSS
# st.markdown("""
# <style>
# body {
#     background-color: #fffaf0;
#     font-family: 'Georgia', serif;
# }
# h1 {
#     color: #7b3f00;
#     text-align: center;
#     padding: 1rem 0;
# }
# .stTextInput>div>div>input {
#     background-color: #fff6e0;
#     border: 2px solid #cd853f;
#     border-radius: 8px;
#     padding: 10px;
#     font-size: 16px;
# }
# .stSelectbox>div>div>div {
#     background-color: #fff6e0;
#     border: 2px solid #cd853f;
#     border-radius: 8px;
# }
# .stButton>button {
#     background-color: #cd853f;
#     color: white;
#     border: none;
#     border-radius: 8px;
#     padding: 10px 20px;
#     font-weight: bold;
#     font-size: 16px;
#     margin-top: 10px;
# }
# .stButton>button:hover {
#     background-color: #a0522d;
#     transform: scale(1.03);
# }
# .translated {
#     background-color: #fff0d5;
#     padding: 1rem;
#     border-radius: 10px;
#     border-left: 5px solid #008000;
#     font-size: 1.1rem;
#     margin-top: 1rem;
# }
# </style>
# """, unsafe_allow_html=True)

# # Title
# st.markdown("<h1>🌐 Heritage Language Translator 🔊</h1>", unsafe_allow_html=True)

# # Input Text
# input_text = st.text_input("Enter text to translate:", "")

# # Language Dropdown
# indian_languages = [
#     "Hindi", "Telugu", "Tamil", "Kannada", "Malayalam", "Bengali", "Gujarati",
#     "Punjabi", "Marathi", "Odia", "Assamese", "Manipuri", "Sanskrit", "Urdu",
#     "Konkani", "Bodo", "Dogri", "Maithili", "Santali", "Kashmiri", "Sindhi", "Nepali"
# ]
# selected_language = st.selectbox("Choose target language:", indian_languages)

# language_code_map = {
#     "Hindi": "hi", "Telugu": "te", "Tamil": "ta", "Kannada": "kn", "Malayalam": "ml",
#     "Bengali": "bn", "Gujarati": "gu", "Punjabi": "pa", "Marathi": "mr", "Odia": "or",
#     "Assamese": "as", "Urdu": "ur", "Nepali": "ne", "Sanskrit": "sa", "Konkani": "gom",
#     "Dogri": "doi", "Bodo": "brx", "Maithili": "mai", "Sindhi": "sd", "Kashmiri": "ks",
#     "Manipuri": "mni", "Santali": "sat", "English": "en"
# }

# # Translate + Speak
# if st.button("Translate"):
#     if input_text.strip() == "":
#         st.warning("Please enter some text to translate.")
#     else:
#         try:
#             prompt = f"Just give the accurate {selected_language} translation for: {input_text}\nDo not explain anything."
#             response = model.generate_content(prompt)
#             translated_text = response.text.strip()

#             st.markdown(f'<div class="translated"><b>Translated Output:</b> {translated_text}</div>', unsafe_allow_html=True)

#             lang_code = language_code_map.get(selected_language, "hi")
#             tts = gTTS(text=translated_text, lang=lang_code)
#             with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
#                 tts.save(fp.name)
#                 st.audio(fp.name, format="audio/mp3")
#         except Exception as e:
#             st.error(f"Translation or Voice Error: {e}")
