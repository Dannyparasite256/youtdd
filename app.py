import streamlit as st
from pytube import YouTube

def main():
    st.title("YouTube Video Downloader")

    # Custom text input field with text color changed to red
    st.markdown(
        """<style>
            div.stTextInput>div>div>input { color: black }
        </style>
        """, unsafe_allow_html=True
    )
    video_url = st.text_input("Enter YouTube Video URL")

    if video_url:
        try:
            yt = YouTube(video_url)
            st.subheader("Video Information")
            st.write(f"Title: {yt.title}")
            st.write(f"Description: {yt.description}")
            st.image(yt.thumbnail_url)

            # Video quality selection
            available_streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
            stream_quality = st.selectbox("Select Video Quality", available_streams.all())
            if stream_quality:
                st.write("Download:")
                st.markdown(f"[Download Video ({stream_quality.resolution})]({stream_quality.url})")
        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
