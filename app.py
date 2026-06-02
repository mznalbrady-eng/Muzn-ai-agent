import streamlit as st
from googleapiclient.discovery import build
from google.oauth2 import service_account
import json

# إعداد الربط مع جوجل درايف
def get_drive_service():
    creds_info = st.secrets["connections"]["gcloud"]["gcp_service_account_info"]
    creds_dict = json.loads(creds_info)
    creds = service_account.Credentials.from_service_account_info(creds_dict, 
            scopes=["https://www.googleapis.com/auth/drive.readonly"])
    return build("drive", "v3", credentials=creds)

st.title("🤖 وكيل مزن الذكي")
st.write("أنا جاهز لقراءة ملفاتك والبحث فيها!")

query = st.text_input("وش تبين تبحثين عنه في ملفاتك؟")

if st.button("ابحثي لي"):
    if query:
        with st.spinner("جاري البحث في ملفاتك..."):
            try:
                service = get_drive_service()
                # البحث عن الملفات
                results = service.files().list(q=f"name contains '{query}' and trashed=false", 
                                             fields="files(id, name)").execute()
                files = results.get("files", [])
                
                if files:
                    st.write("لقيت لكِ هذه الملفات:")
                    for file in files:
                        st.write(f"- {file['name']}")
                else:
                    st.write("للأسف ما لقيت ملف بهذا الاسم.")
            except Exception as e:
                st.error(f"حدث خطأ أثناء الاتصال: {e}")
    else:
        st.warning("الرجاء كتابة اسم الملف للبحث عنه.")
