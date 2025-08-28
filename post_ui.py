import streamlit as st
import cohere
import random
import pandas as pd

# Initialize Cohere client
co = cohere.Client("9rzL8PAdVTkFlVdclSQ8MMS0uNzF8KO4UJsG2rMg")

def generate_post(topic, tone="casual"):
    prompt = f"Write a {tone} social media post about {topic}. Make it short and engaging. Include emojis if possible."

    response = co.chat(
        model="command-r-plus",
        message=prompt
    )
    post = response.text

    hashtags_list = [
        "#trending", "#instadaily", "#fun", "#style", "#tech",
        "#love", "#motivation", "#life", "#happy", "#social"
    ]
    hashtags = " ".join(random.sample(hashtags_list, 3))

    return post, hashtags

# ---- Streamlit UI ----
st.title("📱 AI Social Media Post Generator")

topic = st.text_input("Enter your post topic:")
tone = st.selectbox("Choose tone", ["casual", "funny", "professional"])

if st.button("Generate Post"):
    with st.spinner("⚡ Generating post..."):
        post, hashtags = generate_post(topic, tone)

        st.subheader("✨ Generated Post:")
        st.write(post)

        st.subheader("🔖 Suggested Hashtags:")
        st.write(hashtags)

        # --- Export Options ---
        st.download_button(
            label="💾 Download as TXT",
            data=f"{post}\n\nHashtags: {hashtags}",
            file_name="post.txt",
            mime="text/plain"
        )

        df = pd.DataFrame([{"Post": post, "Hashtags": hashtags}])
        st.download_button(
            label="📂 Download as CSV",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="post.csv",
            mime="text/csv"
        )