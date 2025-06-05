import streamlit as st
import base64
import os

def resume_page():
    pdf_file_path = r'..\04_personal_site_streamlit\static\docs\刘哲恺-产品简历.pdf'

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # Display the download button
        st.download_button(label="Download Resume",
                        data=PDFbyte,
                        file_name="LIU_Zhekai_Resume.pdf",
                        mime='application/octet-stream')
    else:
        st.warning("Resume PDF file not found")

    st.title("LIU Zhekai")

    st.header("联系方式")
    st.markdown("""
    - **电话:** (+86) 131-2653-0722
    - **邮箱:** [Callus_L@outlook.com](mailto:Callus_L@outlook.com)
    - **地址:** 香港沙田马料水泽祥街12号
    - **GitHub:** [github.com/CallusLiu](https://github.com/CallusLiu)
    """)

    st.header("教育背景")
    st.markdown("""
    **香港中文大学 | 市场学理学硕士**
    - 2024.08 - 至今
    - 相关课程: Marketing Research, Marketing Analytics, Pricing Analytics
    
    **北京化工大学 | 行政管理学士**
    - 2020.09 - 2024.06
    - 平均绩点: 88/100
    - 核心课程: 社会学（95）、市场营销与策划（92）
    """)

    st.header("工作经历")
    st.markdown("""
    **阳狮（北京）文化传播有限公司 | 客户执行实习生**
    - 2024.03 - 2024.05
    - 主导雀巢2024中秋Campaign活动，全平台传播触达20w+
    - 完成20+ KOL商务合作方案，媒介投放覆盖微博/京东/天猫平台
    
    **浙江怡联网络科技股份有限公司 | 产品实习生**
    - 2024.07 - 2024.08
    - 参与开发"招商云"To B项目，推动AR实景看铺功能上线
    """)

    st.header("项目经历")
    st.markdown("""
    **YEAP实习僧 - AI教育平台**
    - 研发基于YOLOv5算法的简历诊断功能
    - 实现用户画像分析与个性化学习规划
    
    **"正大杯"市场调研大赛**
    - 完成10万条微博数据抓取与LDA主题分析
    - 建立SEM结构方程模型分析核心影响因素
    """)

    st.header("专业技能")
    st.markdown("""
    - **数据分析:** Python (Pandas/NLTK), SQL, K-means聚类
    - **市场工具:** A/B测试、用户画像分析
    - **语言能力:** 英语六级605分、雅思7.0
    - **认证证书:** 全国大学生市场调研大赛国家级奖项
    """)
    
    # 移除不需要的Certifications和Languages部分
