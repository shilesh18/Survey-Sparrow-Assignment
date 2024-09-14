from data_analysis import analyze_data

def test_analyze_data():
    competitor_data = {"abstract": "Apple is a tech company."}
    analysis = analyze_data(competitor_data)
    assert analysis is not None
