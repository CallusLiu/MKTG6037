import streamlit as st
from PIL import Image
import os

def home_page():
    left_col, right_col = st.columns(2)
    left_col.markdown(
        """
        <h4>刘哲恺</h4>
        <p>市场学硕士毕业生<br>
        香港中文大学<br>
        香港沙田马料水泽祥街12号<br>
        <a href="mailto:Callus_L@outlook.com">Callus_L@outlook.com</a></p>
        """,
        unsafe_allow_html=True
    )

    # add a photo to the right column
    image_path = os.path.join(os.path.dirname(__file__), "..", "static", "images", "证件照.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        right_col.image(image, width=200)
    else:
        right_col.warning("Profile image not found")

    st.markdown("---")

    st.markdown(
        """
        ### 关于我
        我是一名应届市场学硕士毕业生，对利用数据洞察驱动产品与市场策略充满热情。在香港中文大学的深造以及在北京化工大学的本科学习期间，我不仅打下了坚实的市场营销、品牌管理和数据分析理论基础，还积极投身于实践，在阳狮集团和安克创新等知名企业积累了宝贵的产品与市场经验。

        我曾深度参与品牌传播、达人营销、竞品分析以及SaaS平台产品的开发与迭代过程。在“YEAP翻谱”和“正大杯”市场调研大赛等项目中，我作为核心成员，负责从需求调研、产品设计到市场推广的全流程工作，成功将AI技术应用于教育辅助平台，并主导完成了大规模的市场调研项目。

        我乐于接受挑战，具备快速学习能力和团队协作精神，并能熟练运用多种分析工具解决实际问题。我期待在一个充满活力的环境中贡献我的专业知识与技能，并与团队共同成长。
        """
    )

    st.markdown(
        """
        ### 专业技能
        - **市场营销与策略**: 品牌传播, 市场调研, 竞品分析, 数字营销, 内容创作, 社群运营
        - **产品管理**: 需求分析, 产品设计, 用户体验优化, 项目管理, SaaS产品
        - **数据分析**: Python (Pandas, NLTK, Selenium), R, SQL, A/B测试, K-means聚类, SEM结构方程模型, 描述性与推断性统计
        - **语言能力**: 英语 (CET-6: 605, IELTS: 7.0), 普通话 (母语)
        - **办公与其他**: Microsoft Office Suite, 调研工具, 良好的沟通与表达能力
        """
    )

    st.markdown("---")
    
    # Interactive component has been moved to the experience page