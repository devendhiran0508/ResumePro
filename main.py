import streamlit as st
import os
import io
import PyPDF2
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()

st.set_page_config(page_title="ResumePro", page_icon=":guardsman:", layout="centered")
st.markdown("""
<h2 style="text-align:center;" class="fade-in">🚀 Welcome to <span style='color:#6C63FF'>ResumePro</span></h2>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.fade-in {
    animation: fadeInUp 1s ease-out;
}
@keyframes fadeInUp {
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
}
</style>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align:center;'>Upload your resume and get smart, AI-powered feedback tailored to your job role!</p>", unsafe_allow_html=True)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") 

# Check if API key is loaded
if not GOOGLE_API_KEY:
    st.error("Google API Key not found. Please set the GOOGLE_API_KEY environment variable in your .env file.")
    st.stop()

uploaded_file = st.file_uploader("📄 Upload your resume (PDF or TXT)", type=["pdf","txt"])
job_role = st.text_input("💼 Enter the job role you are applying for")
analyse = st.button("Analyse Resume")

def extract_text_from_pdf(pdf_file):
    
    #Extracts text from a PDF file object.
    
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(uploaded_file):
    
    #Extracts text from an uploaded file, supporting PDF and TXT.
    
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    elif uploaded_file.type == "text/plain":
        return uploaded_file.read().decode("utf-8")
    else:
        st.error("Unsupported file type. Please upload a PDF or TXT file.")
        return ""

if analyse and uploaded_file:
    try:
        # Show a spinner while processing
        with st.spinner('Analyzing your resume...'):
            file_content = extract_text_from_file(uploaded_file)

            if not file_content.strip():
                st.error("The uploaded file is empty or could not be read.")
                st.stop()
            
            # Construct the prompt for the AI model
            prompt = f"""Please analyze this resume and provide constructive feedback.
            Focus on the following aspects:
            1. Content clarity and impact
            2. Skills presentation
            3. Experience descriptions
            4. Specific improvements for {job_role if job_role else 'general applications'}
            Resume content:
            {file_content}
            Please provide your analysis in a clear, structured format with specific recommendations."""
            
            genai.configure(api_key=GOOGLE_API_KEY)
            
            model = genai.GenerativeModel("gemini-2.0-flash") 
            
            response = model.generate_content(prompt)
            
            st.markdown("### Analysis Result")
            st.markdown(response.text)

    except Exception as e:
        st.error(f"An error occurred while processing the resume: {str(e)}")

