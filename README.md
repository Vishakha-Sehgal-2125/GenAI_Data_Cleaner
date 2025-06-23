# 🧠 GenAI Data Cleaner & Profiler

An interactive app to upload a messy CSV, get column-wise profiling, and receive **AI-powered suggestions** for cleaning — powered by OpenAI *or* a free offline model. 

> ⚡ Built with beginner-friendliness, real-world relevance, and future-readiness in mind.

---

## 🚀 Features

- 📂 Upload any `.csv` file
- 📊 See summary of each column (nulls, types, sample values, etc.)
- 🤖 Ask GenAI (or offline AI) how to clean a column
- 💾 Download the cleaned version

---

## 🛠️ Tech Stack

- **Python** (3.9+)
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [OpenAI API](https://platform.openai.com/) *(optional)*
- [HuggingFace Transformers](https://huggingface.co/transformers/) *(fallback)*
- `python-dotenv`

---

## 🧩 How It Works

| With OpenAI API Key | Without Key |
|---------------------|-------------|
| Uses GPT-3.5 via API | Uses offline T5 model |
| Smarter suggestions | Slower but still usable |
| Requires `.env` setup | No setup needed |

---

## ⚙️ Setup Instructions

### 🔹 Step 1: Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/genai-data-cleaner.git
cd genai-data-cleaner
