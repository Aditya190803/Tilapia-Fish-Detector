## 🐟 Tilapia Fish Detector

A simple Streamlit app that uses Google's **Gemini Vision API** to:

* Detect if an uploaded fish image is a **Tilapia**
* Identify whether the **Tilapia is infected** (based on visible signs)

---


### 🚀 Features

* ✅ Upload fish image (JPG, PNG)
* ✅ AI model determines:

  * Is it a Tilapia?
  * Is it infected?
* ✅ Simple Streamlit UI
* ✅ Powered by **Gemini 2.5 Vision API**

---

### 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### 🔑 API Key Setup

1. **Get your Gemini API key from Google AI Studio**
   👉 [AI STUDIO](https://aistudio.google.com/app/apikey)

2. Create a file `.streamlit/secrets.toml`:

```toml
gemini_api_key = "YOUR_GEMINI_API_KEY"
```
### ▶️ Running the App

```bash
streamlit run app.py
```

---

### 🧠 How It Works

* Uses `google-generativeai` to connect to Gemini.
* Sends the **image** with a **prompt** asking:

  * Is the fish a Tilapia?
  * Is it infected? (visible signs like lesions, swelling, parasites)
* Gemini returns one of:

  * `This is not a Tilapia.`
  * `This is a healthy Tilapia.`
  * `This is an infected Tilapia.`

