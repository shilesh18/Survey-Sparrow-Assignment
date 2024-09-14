import spacy

nlp = spacy.load("en_core_web_sm")

def analyze_data(competitor_data):
    text = competitor_data.get("abstract", "")
    doc = nlp(text)
    
    # Extract named entities (e.g., competitors, products)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return {
        "entities": entities,
        "related_topics": competitor_data.get("related_topics", [])
    }
