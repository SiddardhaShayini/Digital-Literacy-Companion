import re
import string
import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from data.responses import get_responses
from data.topics import get_topics
import streamlit as st

# Download necessary NLTK data
# We use nltk.download with download_dir specified to ensure data is stored in a location
# that the application can access and ensure all necessary data is downloaded
# nltk.download('punkt', download_dir='/home/runner/nltk_data')
# nltk.download('stopwords', download_dir='/home/runner/nltk_data')
# nltk.download('wordnet', download_dir='/home/runner/nltk_data')

# Let NLTK download to its default location by removing the download_dir argument:
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize lemmatizer for word normalization after downloads are complete
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    """Preprocess the text by tokenizing, removing stopwords, and lemmatizing"""
    # Convert to lowercase and remove punctuation
    text = text.lower()
    text = re.sub(r'[{}]'.format(re.escape(string.punctuation)), ' ', text)
    
    # Simple tokenization by splitting on whitespace
    raw_tokens = text.split()
    
    # Remove stopwords and apply lemmatization
    tokens = [lemmatizer.lemmatize(token) for token in raw_tokens if token.isalpha() and token not in stop_words]
    
    return tokens

def calculate_similarity(user_tokens, key_tokens):
    """Calculate similarity score between user tokens and key tokens"""
    # Convert key tokens to a set for faster lookup
    key_set = set(key_tokens)
    
    # Count matching tokens
    matches = sum(1 for token in user_tokens if token in key_set)
    
    # Return similarity score (0 to 1)
    if not user_tokens or not key_tokens:
        return 0
    
    # Calculate Jaccard similarity
    union_size = len(set(user_tokens).union(key_set))
    if union_size == 0:
        return 0
    return matches / union_size

def get_best_response(user_tokens):
    """Get the best response based on similarity to predefined responses"""
    responses = get_responses()
    best_score = 0
    best_response = None
    best_category = None
    
    for category, category_responses in responses.items():
        for pattern, response in category_responses.items():
            # Process pattern
            pattern_tokens = preprocess_text(pattern)
            
            # Calculate similarity
            similarity = calculate_similarity(user_tokens, pattern_tokens)
            
            # Check if this is the best match so far
            if similarity > best_score:
                best_score = similarity
                best_response = response
                best_category = category
    
    # If we found a good match
    if best_score > 0.2:  # Threshold for accepting a match
        return best_response
    
    # Default fallback response
    return get_fallback_response()

def process_query(user_input):
    """Process user query and return appropriate response"""
    # Preprocess the user input
    tokens = preprocess_text(user_input)
    
    # Find the best response
    response = get_best_response(tokens)
    return response

def get_fallback_response():
    """Return a random fallback response when no good match is found"""
    fallback_responses = [
        "Hmm, I'm not quite following that. Could you try rephrasing your question? I'm eager to help! 😊",
        "Oh! I don't have that information in my digital toolkit yet. Let me know if I can help with something else - I know lots about internet basics and online safety!",
        "I'm still learning the digital ropes! Could you ask me about a different tech topic? I'm really good with email, social media, and smartphone tips! 📱",
        "That's a new one for me! Would you like to explore basic internet safety, social media, or email tips instead? Those are some of my favorite topics to chat about!",
        "Oops! That question stumped me. Is there another digital topic I can help with? I'm your buddy for all things tech! 💻"
    ]
    return random.choice(fallback_responses)

def get_initial_message():
    """Return the initial greeting message"""
    topics = get_topics()
    topics_flat = []
    for category, topic_list in topics.items():
        for topic in topic_list[:3]:  # Get only first 3 topics from each category
            topics_flat.append(topic)
    
    random_topics = random.sample(topics_flat, min(3, len(topics_flat)))
    topics_text = ", ".join(random_topics)
    
    return f"""
    Hello there! 👋 I'm DigiBuddy, your friendly tech-savvy pal! I'm here to help you conquer the digital world with confidence and a smile!
    
    You can ask me about anything tech-related like:
    - {topics_text}
    - And so many more digital topics! 💻 📱 🔒
    
    No question is too simple - that's what buddies are for! Type your question below or browse the topics in the sidebar. Let's make technology fun together!
    """
