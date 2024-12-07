import streamlit as st
import cv2
import wikipedia
import pytesseract


left, middle, right = st.columns(3)
if middle.button("Start", icon="✳",):
    middle.markdown("Thinking...")

title = st.text_input("ThinkBox","tell me About...")
st.write("Describe Your Problem!", title)