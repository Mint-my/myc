import streamlit as st

video_file = [
    {"url": "https://mp-17ef04d6-62a6-4add-9709-6c80be8c52ce.cdn.bspapp.com/1.mp4",
     "title": "熊出没第一季第1集", "episode": 1},
    {"url": "https://mp-17ef04d6-62a6-4add-9709-6c80be8c52ce.cdn.bspapp.com/2.mp4",
     "title": "熊出没第一季第2集", "episode": 2},
    {"url": "https://mp-17ef04d6-62a6-4add-9709-6c80be8c52ce.cdn.bspapp.com/3.mp4",
     "title": "熊出没第一季第3集", "episode": 3},
    {"url": "https://mp-17ef04d6-62a6-4add-9709-6c80be8c52ce.cdn.bspapp.com/4.mp4",
     "title": "熊出没第一季第4集", "episode": 4},
    {"url": "https://mp-17ef04d6-62a6-4add-9709-6c80be8c52ce.cdn.bspapp.com/5.mp4",
     "title": "熊出没第一季第5集", "episode": 5},
    {"url": "https://mp-17ef04d6-62a6-4add-9709-6c80be8c52ce.cdn.bspapp.com/6.mp4",
     "title": "熊出没第一季第6集", "episode": 6},
]

if "ind" not in st.session_state:
    st.session_state.ind = 0  # 默认第 1 集

def play(i: int):
    st.session_state.ind = i

st.set_page_config(page_title="熊出没第一季", layout="centered")


st.title(f"熊出没第一季 第{st.session_state.ind + 1}集")

st.video(video_file[st.session_state.ind]["url"], autoplay=True)

st.markdown(
    """
**简介：**  
宁静祥和的东北原始森林，空气清新，万物复苏。熊大和熊二两兄弟在林间追逐奔跑，非常快乐。正在此时，发动机的轰鸣打破了森林的宁静，来者是一个伐木队的小老板，他叫光头强。光头强带着老板的重托，竟来到风景优美的东北原始森林里采伐原木！看着森林被毁，熊兄弟决定要保护森林，保护家园，与光头强斗智斗勇！但是伐木工光头强可没那么容易就离开。于是，一场旷日持久的家园保卫战开始了……
"""
)

st.write("**选集：**")
row1, row2 = st.columns(3), st.columns(3)

for c, i in enumerate(range(0, 3)):          
    with row1[c]:
        st.button(
            f"第{i+1}集",
            use_container_width=True,
            on_click=play,
            args=[i],
        )

for c, i in enumerate(range(3, 6)):         
    with row2[c]:
        st.button(
            f"第{i+1}集",
            use_container_width=True,
            on_click=play,
            args=[i],
        )
