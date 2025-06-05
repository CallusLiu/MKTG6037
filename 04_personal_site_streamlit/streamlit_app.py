import warnings
import streamlit as st

warnings.simplefilter(action="ignore", category=FutureWarning)

# Must be the first Streamlit command
st.set_page_config(page_title="personalsite", layout="wide")

# Import pages from the new directory
from page_content.home import home_page
from page_content.experience import experience_page
from page_content.education import education_page
from page_content.resume import resume_page
from page_content.contact import contact_page

# Import components
from components.footer import display_footer
from components.styles import load_css

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        load_css()
        
        # 恢复主菜单标题
        st.sidebar.markdown("## 主菜单")
        
        # 应用导航交互逻辑
        selected = st.sidebar.radio(
            "",
            self.apps,
            format_func=lambda app: app["title"],
            label_visibility="collapsed"  # 隐藏radio组件默认标签
        )

        st.sidebar.markdown("---")
        selected["function"]()
        display_footer()

# Initialize the app
app = MultiApp()

# Add pages to the app (正确的添加位置)
app.add_app("主页", home_page)
app.add_app("教育背景", education_page)
app.add_app("项目经历", experience_page)
app.add_app("简历下载", resume_page)
app.add_app("联系我", contact_page)

# Run the app
app.run()
