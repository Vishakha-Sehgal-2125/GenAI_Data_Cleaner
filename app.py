import streamlit as st
import pandas as pd
import os
import io
from dotenv import load_dotenv
from profiler import profile_dataframe
from ask_genai import ask_genai

# Load environment variables
load_dotenv()

st.set_page_config(page_title="GenAI Data Cleaner", layout="wide")
st.title(" GenAI-Powered Data Cleaning Tool")

# 💡 OpenAI key warning
if not os.getenv("OPENAI_API_KEY"):
    st.warning("⚠️ No OpenAI API key found. Offline AI model will be used instead of GPT.")

# 📤 Upload file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, on_bad_lines='warn')
        st.subheader("🔍 Preview of Uploaded Data")
        st.dataframe(df.head())

        st.subheader("📈 Data Summary")
        profile = profile_dataframe(df)

        for col, summary in profile.items():
            with st.expander(f"🔍 Column: {col}"):
                st.markdown(
                    f"- **Data Type**: `{summary['Data Type']}`\n"
                    f"- **Nulls**: `{summary['Nulls']}`\n"
                    f"- **Unique Values**: `{summary['Unique Values']}`\n"
                    f"- **Sample Values**: `{summary['Sample Values']}`\n"
                )
                if "Min" in summary:
                    st.markdown(
                        f"- **Min**: `{summary['Min']}`\n"
                        f"- **Max**: `{summary['Max']}`\n"
                        f"- **Mean**: `{summary['Mean']}`\n"
                        f"- **Std**: `{summary['Std']}`\n"
                    )

                if st.button(f"🤖 Ask GenAI for help with '{col}'", key=col):
                    with st.spinner("Asking GenAI..."):
                        non_null_values = df[col].dropna().astype(str)
                        sample_size = min(5, len(non_null_values))
                        sampled = non_null_values.sample(sample_size).tolist() if sample_size > 0 else []

                        prompt = (
                                    f"I'm cleaning a dataset. Here's a sample of values from the '{col}' column: {sampled}. "
                                    f"Based on these values, suggest relevant data cleaning steps like handling nulls, "
                                    f"removing outliers, fixing formatting, or standardizing values."
                                 )
                        reply = ask_genai(prompt)
                        st.success("GenAI Suggestion:")
                        st.write(reply)

        # 📥 Download button
        csv = df.to_csv(index=False)
        b = io.BytesIO()
        b.write(csv.encode())
        b.seek(0)

        st.subheader("📥 Download Cleaned File")
        st.download_button(
            label="💾 Download Cleaned CSV",
            data=b,
            file_name="cleaned_data.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(f"❌ Error reading file: {e}")
