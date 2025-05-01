import re
import html

def clean_user_input(input_text):
    """
    Clean and sanitize user input to prevent any potential issues.
    """
    if not input_text:
        return ""
    
    # Trim whitespace
    cleaned = input_text.strip()
    
    # Escape HTML to prevent XSS
    cleaned = html.escape(cleaned)
    
    # Limit length to prevent abuse
    max_length = 500
    if len(cleaned) > max_length:
        cleaned = cleaned[:max_length]
    
    # Remove excessive spaces and newlines
    cleaned = re.sub(r'\s+', ' ', cleaned)
    
    return cleaned

def shorten_text(text, max_length=100):
    """
    Shorten text to a maximum length while preserving full words.
    """
    if len(text) <= max_length:
        return text
    
    shortened = text[:max_length].rsplit(' ', 1)[0]
    return shortened + "..."
