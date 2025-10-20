# app.py
# AI Tech News Summarizer simulation by Sarfinaz

def summarize_text(text, max_sentences=3):
    """
    Simple simulation: returns first `max_sentences` sentences as summary
    """
    sentences = text.split('. ')
    summary = '. '.join(sentences[:max_sentences])
    if not summary.endswith('.'):
        summary += '.'
    return summary

def extract_keywords(text, max_keywords=5):
    """
    Simple keyword extraction: most frequent words excluding common words
    """
    common_words = {"the","is","and","in","to","a","of","for","on","with","as","by","an","it","this","that"}
    words = [word.strip('.,!?:;').lower() for word in text.split()]
    keywords = {}
    for word in words:
        if word not in common_words and len(word) > 2:
            keywords[word] = keywords.get(word,0)+1
    # Sort by frequency
    sorted_keywords = sorted(keywords.items(), key=lambda x: x[1], reverse=True)
    return [k[0] for k in sorted_keywords[:max_keywords]]

def estimate_reading_time(text):
    """
    Simple reading time estimate: 200 words per minute
    """
    words = text.split()
    minutes = len(words)/200
    return round(minutes,1)

def main():
    print("=== AI Tech News Summarizer by Sarfinaz ===\n")
    text = input("Paste your tech article here: ")
    
    summary = summarize_text(text)
    keywords = extract_keywords(text)
    reading_time = estimate_reading_time(text)
    
    print("\n--- Summary ---")
    print(summary)
    print("\n--- Keywords ---")
    print(', '.join(keywords))
    print(f"\nEstimated reading time: {reading_time} minutes")

if __name__ == "__main__":
    main()
