import openai

openai.api_key = "your-api-key-here"  # Replace with your OpenAI API key

def generate_battlecard(analyzed_data, product_info):
    prompt = f"Create a battlecard comparing {analyzed_data} with {product_info}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    
    battlecard_content = response.choices[0].text
    return battlecard_content
