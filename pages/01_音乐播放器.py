import streamlit as st

# 1. 页面标题
st.set_page_config(page_title="简易音乐播放器", page_icon="🎵")
st.title("简易音乐播放器")

# 2. 歌曲数据
if 'ind' not in st.session_state:
    st.session_state.ind = 0

playlist = [
    {
        "url": "https://p2.music.126.net/91GNFB15RhD4G_eRRQKaaQ==/109951172214133834.jpg?param=500y500",
        "song": "fiction",
        "artist": "h3R3",
        "duration": "3:54",
        "mp3": "https://music.163.com/song/media/outer/url?id=3311876765.mp3"
    },
    {
        "url": "http://p1.music.126.net/RYIrCEYzgeAD85DJ0rgOQA==/109951169256300966.jpg?param=500y500",
        "song": "碎碎念",
        "artist": "队长",
        "duration": "2:11",
        "mp3": "https://music.163.com/song/media/outer/url?id=2097443876.mp3"
    },
    {
        "url": "http://p2.music.126.net/JBe7AwcGkYHhleOfQvY2hg==/109951169798343077.jpg?param=500y500",
        "song": "再等冬天(Memories)",
        "artist": "h3R3",
        "duration": "2:48",
        "mp3": "https://music.163.com/song/media/outer/url?id=1927693793.mp3"
    }
]

# 3. 当前歌曲
idx = st.session_state.ind
cur = playlist[idx]

# 4. 左右布局：左图 + 专辑封面字样 | 右信息
left, right = st.columns([1, 1.2])
with left:
    st.image(cur["url"], width=250)
    st.caption("专辑封面")   # 图片下方小字

with right:
    st.markdown(f"**歌名：** {cur['song']}")
    st.markdown(f"**歌手：** {cur['artist']}")
    st.markdown(f"**时长：** {cur['duration']}")
    st.audio(cur["mp3"], format="audio/mpeg")

# 5. 切歌按钮
def next_song():
    st.session_state.ind = (st.session_state.ind + 1) % len(playlist)

def prev_song():
    st.session_state.ind = (st.session_state.ind - 1) % len(playlist)

c1, c2 = st.columns(2)
with c1:
    st.button("⏮ 上一曲", on_click=prev_song, use_container_width=True)
with c2:
    st.button("下一曲 ⏭", on_click=next_song, use_container_width=True)
