def generate_bio(name, profession, interests, city, vibe):
    instagram_bio = f"""
✨ {name} ✨
📍 {city}
💼 {profession}
❤️ {interests}
{vibe} 😎
"""

    twitter_bio = f"{name} | {profession} | {interests} | {city} | {vibe}"

    print("\n📸 Instagram Bio:")
    print(instagram_bio)

    print("🐦 Twitter (X) Bio:")
    print(twitter_bio)


# ---- User Inputs ----
name = input("Enter your name: ")
profession = input("Enter your profession: ")
interests = input("Enter your interests (comma separated): ")
city = input("Enter your city: ")
vibe = input("Enter your vibe (e.g. Dream big | Hustle | Learning daily): ")

generate_bio(name, profession, interests, city, vibe)
