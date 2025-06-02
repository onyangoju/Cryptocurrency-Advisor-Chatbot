# 1. Chatbot Personality
bot_name = "CryptoBuddy"
bot_tone = "Hey there! Let’s find you a green and growing crypto! 🌱🚀"

# 2. Predefined Crypto Data
crypto_db = {  
    "Bitcoin": {  
        "price_trend": "rising",  
        "market_cap": "high",  
        "energy_use": "high",  
        "sustainability_score": 3/10  
    },  
    "Ethereum": {  
        "price_trend": "stable",  
        "market_cap": "high",  
        "energy_use": "medium",  
        "sustainability_score": 6/10  
    },  
    "Cardano": {  
        "price_trend": "rising",  
        "market_cap": "medium",  
        "energy_use": "low",  
        "sustainability_score": 8/10  
    }  
}

# 3 & 4. Chatbot Logic & Advice Rules
def crypto_advice(user_query):
    query = user_query.lower()

    if "trending up" in query or "price rising" in query or "long-term growth" in query:
        # Recommend coins with rising price trend and high market cap
        candidates = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising" and data["market_cap"] == "high"]
        if candidates:
            return f"{candidates[0]} is trending up with a strong market cap! 🚀"
        else:
            return "No top-tier rising coins found right now, but Cardano is rising with medium market cap and good sustainability!"
    
    if "most sustainable" in query or "eco-friendly" in query or "green" in query:
        # Recommend coin with highest sustainability score and low energy use
        sustainable_coins = {coin: data["sustainability_score"] for coin, data in crypto_db.items() if data["energy_use"] == "low" and data["sustainability_score"] > 7/10}
        if sustainable_coins:
            best_coin = max(sustainable_coins, key=sustainable_coins.get)
            return f"Invest in {best_coin}! 🌱 It’s eco-friendly and has long-term potential!"
        else:
            return "Currently, no coins meet top sustainability criteria, but Cardano is a good option!"

    if "best overall" in query or "recommend" in query:
        # Prioritize rising trend, high market cap, and sustainability
        best_score = -1
        best_coin = None
        for coin, data in crypto_db.items():
            score = 0
            if data["price_trend"] == "rising":
                score += 2
            if data["market_cap"] == "high":
                score += 2
            if data["energy_use"] == "low":
                score += 1
            if data["sustainability_score"] > 7/10:
                score += 2
            if score > best_score:
                best_score = score
                best_coin = coin
        if best_coin:
            return f"For a balance of growth and sustainability, {best_coin} looks promising! 🚀🌱"
        else:
            return "I don't have a strong recommendation right now."

    return "Sorry, I didn't quite catch that. Can you ask about trending, sustainable, or recommended cryptos?"

# 5. Test the bot
def chat():
    print(f"{bot_name}: {bot_tone}")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print(f"{bot_name}: Bye! Happy investing! 🚀")
            break
        reply = crypto_advice(user_input)
        print(f"{bot_name}: {reply}")

# Run the chatbot
chat()
