def get_intent_response(text):
    """return a response basedon a detected keywords"""
    if any (word in text for word in ["hello" ,"hi" , "hey", "Aaslema"]):
        return "Aslemaaaa bestieee! How can I help you today?"
    elif any (word in text for word in ["bye" ,"goodbye" , "see you", "Besslama"]):
        return "Besslama! Have a great day!"
    elif any (word in text for word in ["how are you" ,"how's it going" , "what's up"]):
        return "I'm just a bot, but I'm here to help you!"
    elif any (word in text for word in ["thank you" ,"thanks" , "thx"]):
        return "You're welcome! If you have any more questions, feel free to ask."
    elif any (word in text for word in ["help" ,"support" , "assist"]):
        return "Sure! What do you need help with?"
    elif any (word in text for word in ["joke" ,"funny" , "make me laugh"]):
        return "Why did the scarecrow win an award? Because he was outstanding in his field!"
    else:
        return "I'm not sure how to respond to that. Can you please rephrase?"
    
