import streamlit as st
from groq import Groq

st.title("🤖 وكيل مزن الذكي")

# نظام كلمة السر
password = st.sidebar.text_input("كلمة السر:", type="password")
if password != "Muzn2026":
    st.warning("أدخلي كلمة السر للبدء")
    st.stop()

# إعداد الوكيل
# ضعي مفتاحك الخاص هنا بين علامتي التنصيص
api_key = "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" 
client = Groq(api_key=api_key)

user_input = st.text_area("ماذا تريدين من الوكيل أن يبحث عنه؟")
if st.button("ابحثي واكتبي"):
    if user_input:
        with st.spinner('جاري البحث والترتيب...'):
            response = client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[{"role": "user", "content": user_input}]
            )
            st.write(response.choices[0].message.content)
