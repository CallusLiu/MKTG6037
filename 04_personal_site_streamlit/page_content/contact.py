import streamlit as st

def contact_page():
    st.markdown("## 联系方式")
    
    st.markdown("""
    ### 基本信息
    - **电话**: (+86) 131-2653-0722
    - **邮箱**: [Callus_L@outlook.com](mailto:Callus_L@outlook.com)
    - **地址**: 香港中文大学 | 香港沙田马料水泽祥街12号
    """)

    st.markdown("### 社交媒体")
    st.markdown("""
    - **Instagram**: [instagram/@Callus_L](https://www.instagram.com/callus_liu?igsh=cmEycW5jNHRyeHp5&utm_source=qr)
    - **GitHub**: [github.com/CallusLiu](https://github.com/CallusLiu)
    """)

    st.markdown("### 发送信息")
    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("姓名")
            email = st.text_input("电子邮箱")
            
        with col2:
            subject = st.text_input("主题")
            
        message = st.text_area("留言内容", height=150)
        
        submitted = st.form_submit_button("发送信息")
        
        if submitted:
            st.success("感谢您的留言！我会在24小时内回复。")

    st.markdown("---")
    
    st.markdown("""
    ### 工作时间
    周一至周五 09:00 - 18:00 (GMT+8)
    请提前邮件预约线上会议
    """)
