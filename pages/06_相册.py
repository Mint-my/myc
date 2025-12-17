import streamlit as st

# 页面标题
st.set_page_config(page_title="相册", page_icon="")
st.title("我的相册")

# 初始化索引
if 'ind' not in st.session_state:
    st.session_state.ind = 0

# 图片列表（注意：字典键用引号，列表元素之间用逗号，不要多打大括号）
images = [
    {"url": "https://img95.699pic.com/photo/60063/8518.jpg_wh860.jpg", "text": "小猫"},
    {"url": "https://ts1.tc.mm.bing.net/th/id/R-C.df5f588d3f260330db71df3740a97bdb?rik=mx3Olcy5IAID6A&riu=http%3a%2f%2fwww.quazero.com%2fuploads%2fallimg%2f140412%2f1-140412005948.jpg&ehk=UVmH2F4NdtSlAldhUocNyGGBcIvrIMzndOzSgvqqveY%3d&risl=&pid=ImgRaw&r=0", "text": "小狗"},
    {"url": "https://img95.699pic.com/photo/60060/9056.jpg_wh860.jpg", "text": "小兔子"}
]

# 显示当前图片
idx = st.session_state.ind
st.image(images[idx]['url'], caption=images[idx]['text'])

# 切换函数
def next_img():
    st.session_state.ind = (st.session_state.ind + 1) % len(images)

def prev_img():
    st.session_state.ind = (st.session_state.ind - 1) % len(images)

# 按钮
c1, c2 = st.columns(2)
with c1:
    st.button("上一张", on_click=prev_img, use_container_width=True)
with c2:
    st.button("下一张", on_click=next_img, use_container_width=True)
