import requests

def get_competitor_data(competitor_name):
    url = f"https://api.duckduckgo.com/?q={competitor_name}&format=json"
    response = requests.get(url)
    data = response.json()
    
    # Example of extracting useful competitor data
    competitor_info = {
        "name": competitor_name,
        "abstract": data.get('Abstract', 'No data available'),
        "related_topics": data.get('RelatedTopics', [])
    }
    
    return competitor_info
