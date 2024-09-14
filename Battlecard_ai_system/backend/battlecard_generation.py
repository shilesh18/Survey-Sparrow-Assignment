import openai

openai.api_key = "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"  # Replace with your OpenAI API key

def generate_battlecard(analyzed_data, product_info):
    prompt = f"Create a battlecard comparing {analyzed_data} with {product_info}"
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    
    battlecard_content = response.choices[0].text
    return battlecard_content
