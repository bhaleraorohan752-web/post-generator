from cohere import Client

# Initialize Cohere client with your API key
co = Client("9rzL8PAdVTkFlVdclSQ8MMS0uNzF8KO4UJsG2rMg")

def generate_post(topic, tone="casual"):
    prompt = f"Write a {tone} social media post about {topic}. Make it short and engaging. Include emojis if possible."
    response = co.chat(
        model="command-r-plus",
        message=prompt   # ✅ use message instead of messages
    )
    post = response.text.strip()
    return post

def generate_hashtags(topic):
    hashtag_prompt = f"""
    Suggest 5 relevant and trending hashtags for a social media post about "{topic}".
    Keep them short, no spaces, and avoid very generic ones like #love or #life.
    """
    response = co.chat(
        model="command-r-plus",
        message=hashtag_prompt   # ✅ fixed here too
    )
    hashtags = response.text.strip()
    return hashtags

# ---- Run the script ----
if __name__ == "__main__":
    print("🚀 File is running")
    print("✅ Inside main block")

    topic = input("Enter your post topic: ")
    tone = input("Choose tone (casual, funny, professional): ")

    print("⚡ Generating post...")
    post = generate_post(topic, tone)

    print("⚡ Generating hashtags...")
    hashtags = generate_hashtags(topic)

    print("\nGenerated Post:\n", post)
    print("\nSuggested Hashtags:\n", hashtags)