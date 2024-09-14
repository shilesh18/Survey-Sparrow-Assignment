from data_collection import get_competitor_data

def test_get_competitor_data():
    data = get_competitor_data("Apple")
    assert data is not None
    assert "name" in data
