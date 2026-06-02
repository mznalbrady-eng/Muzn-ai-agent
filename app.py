import streamlit as st
from groq import Groq

# عنوان الوكيل
st.title("وكيل مزن الذكي 🤖")

# تصميم الألوان للحواف
st.markdown("""
    <style>
    .stTextInput input, .stTextArea textarea {
        border: 2px solid #007BFF !important;
        border-radius: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# نظام كلمة السر
password = st.sidebar.text_input("كلمة السر", type="password")
if password != "Muzn2026":
    st.warning("أدخلي كلمة السر للبدء.")
    st.stop()

# إعداد الوكيل باستخدام الخزنة الآمنة
client = Groq(api_key="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")

# واجهة البحث
user_input = st.text_area("ماذا تريدين من الوكيل أن يبحث عنه؟")
if st.button("ابحثي واكتبي"):
    if user_input:
        with st.spinner('جاري البحث والترتيب...'):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": user_input}]
            )
            st.write(response.choices[0].message.content)
