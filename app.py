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
