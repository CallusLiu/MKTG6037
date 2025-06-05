import streamlit as st

def education_page():
    st.markdown("## 教育背景") # Changed title to Chinese
    
    st.markdown("""
    ### 香港中文大学
    - **学位**: 市场学理学硕士
    - **时间**: 2024.08 - 至今
    - **专业**: 市场学
    - **GPA**: 3.7/4.0
    - **相关课程**: Marketing Research, Marketing Analytics, Pricing Analytics, Strategic Brand Management

    ---

    ### 北京化工大学
    - **学位**: 本科
    - **时间**: 2020.09 - 2024.06
    - **专业**: 公共管理系 行政管理专业
    - **平均绩点**: 88/100
    - **相关课程**: 社会学（95）、市场营销与策划（92）、大学计算机基础（A+）、行政文书写作（88）
    """)
    
    st.markdown("---") # Keep one separator for structure if needed, or remove if no further sections
    
    # Certifications and Academic Projects sections are removed as per resume content.
    # If you have certifications or specific academic projects to add, please provide the details.

if __name__ == "__main__":
    education_page()