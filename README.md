
# 🧠 ResumePro – AI Resume Analyzer with Streamlit + Gemini

ResumePro is a simple yet powerful AI-driven resume analyzer that helps job seekers get instant, constructive feedback on their resumes. Upload your resume (PDF or TXT), specify the job role you're targeting, and get intelligent suggestions using Google's Gemini AI.

---

## 🚀 Features

- 📄 Upload resume in `.pdf` or `.txt` format  
- 🧠 AI-powered analysis using **Gemini Pro (Google Generative AI)**  
- 💬 Focused feedback on:  
  - Content clarity & tone  
  - Skills & experience alignment  
  - Job role targeting  
  
---

## 📦 Tech Stack

- **Python**  
- **Streamlit** – For the web interface  
- **Google Generative AI SDK (`google-generativeai`)**  
- **PyPDF2** – To extract text from PDF resumes  
- **python-dotenv** – For environment variable handling

---

## 🔧 Setup Instructions

### 1. Clone this Repository
```bash
git clone https://github.com/devendhiran0508/ResumePro.git
cd ResumePro
```

### 2. Install Dependencies
```bash
pip install google-generativeai pypdf2 python-dotenv streamlit
```

> 💡 You can use `uv` instead of `pip` if preferred.

### 3. Set Up Environment Variables
Create a `.env` file in the project root and add your Gemini API key:
```env
GOOGLE_API_KEY=your_google_api_key_here
```

> 🔐 `.env` is safely ignored from Git using `.gitignore`.

### 4. Run the App
```bash
streamlit run main.py
```

> Or, if you're using `uv`, run:
```bash
uv run streamlit run main.py
```

---

## 🖼️ Preview (Optional)

_Add screenshots or demo GIFs here to show how it works._

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 👨‍💻 Author

Made with ❤️ by [Devendhiran](https://github.com/devendhiran0508)
