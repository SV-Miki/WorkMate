from workmate_rating.workmate_rating.reports.average_rating import AverageRatingReport


def test_average_rating_report():
    rows = [
        {"name": "a", "brand": "apple", "rating": "4.9"},
        {"name": "b", "brand": "apple", "rating": "4.7"},
        {"name": "c", "brand": "samsung", "rating": "4.8"},
    ]

    report = AverageRatingReport()
    result = report.generate(rows)

    assert result[0]["brand"] == "apple"
    assert result[0]["rating"] == 4.8
