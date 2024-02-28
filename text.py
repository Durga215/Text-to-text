import streamlit as st
from googletrans import Translator
st.title('Text Translator')
text=st.text_area('Enter the Text to Translate in English')
if st.button('Translate'):
    if text:
        translator = Translator()
        translated_text = translator.translate(text, src='auto', dest='en')
        st.success(translated_text.text)
    else:
        st.warning('enter your text')