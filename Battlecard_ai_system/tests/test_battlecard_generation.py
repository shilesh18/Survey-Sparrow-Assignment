from battlecard_generation import generate_battlecard

def test_generate_battlecard():
    analyzed_data = {"entities": [("Apple", "ORG")]}
    product_info = "Our product is better."
    result = generate_battlecard(analyzed_data, product_info)
    assert result is not None
