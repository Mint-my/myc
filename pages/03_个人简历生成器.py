import streamlit as st
from PIL import Image
import os
from datetime import datetime, time

st.set_page_config(page_title="个人简历生成器",page_icon="😊",layout="wide")

st.title("🎨个人简历生成器")
st.text("使用Streamlit创建您的个性化简历")

c_left, c_right = st.columns([1, 2])

# 左侧
with c_left:
    st.subheader("个人信息表单")
    st.divider()

    name = st.text_input('姓名', '')
    work = st.text_input('职位', '')
    phone = st.text_input('电话', '')
    postcode = st.text_input('邮编', '')
    date = st.date_input("出生日期")

    def sex_format_func(gender):
        return f'{gender}'
    sex = st.radio('性别', ['男', '女'], format_func=sex_format_func)

    def my_format_func(option):
        return f'{option}'
    study = st.selectbox('学历', ['小学', '初中', '高中', '大专', '本科', '研究生', '博士'], format_func=my_format_func, index=2)

    st.subheader('语言能力')
    option_1 = st.multiselect(
        '选择你最擅长的语言',
        ['英语', '汉语', '日语', '俄语', '阿拉伯语', '泰语', '韩语'],
        format_func=my_format_func,
    )

    st.subheader('技能')
    options_1 = st.multiselect(
        '选择你最擅长的技能',
        ['python', 'java', 'C++', 'ppt', 'excel'],
        format_func=my_format_func,
    )

    st.subheader("工作经验（年）")
    age = st.slider('工作经验', 0, 60, 3)
    

    st.subheader("期望薪资范围（元）")
    values = st.slider('选择薪资范围', 0.0, 100000.0, (7000.0, 10000.0))
    
    st.subheader("个人简介")
    intro = st.text_area(label='个人简介：', placeholder='请简要介绍您的专业背景、职业目标和个人特点...')

    st.subheader("每日最佳联系时间段")
    col1, col2 = st.columns(2)
    with col1:
        t_start = st.time_input("开始时间", value=time(9, 0))
    with col2:
        t_end = st.time_input("结束时间", value=time(18, 0))
   

    st.subheader("📷 请上传您的个人照片")
    uploaded = st.file_uploader(
        label="选择图片",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=False
    )

# 右侧
with c_right:
    st.subheader('简历实时预览')
    st.divider()
    b_left, b_right = st.columns(2)

    with b_left:
        st.write(name)

        if uploaded is not None:                     
            img = Image.open(uploaded)            
            st.image(img, width='stretch')
        
        st.write('职位：', work)
        st.write('电话', phone)
        st.write('邮编', postcode)
        st.write('出生日期', date)

    with b_right:
        st.write('性别：', sex)
        st.write('学历：', study)
        st.write("我有 ", age, '年的工作经验')
        st.write('我的期望薪资范围是：', values)
        st.write("你选择的每日最佳联系时间段是：", t_start, " 到 ", t_end)
        st.write('语言能力：', '、'.join(option_1) if option_1 else '未选择')

    st.divider()

    st.subheader('个人简介')
    st.write(intro if intro else '神秘外星人......')

    st.subheader('专业技能')
    st.write('专业技能：', '、'.join(options_1) if options_1 else '未选择')
