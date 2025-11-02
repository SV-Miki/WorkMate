from collections import defaultdict

from .base import Report


class AverageRatingReport(Report):
    name = "average-rating"

    def generate(self, rows):
        sums = defaultdict(float)
        counts = defaultdict(int)

        for row in rows:
            brand = (row.get("brand") or "").strip()
            rating_raw = row.get("rating")

            if not brand or not rating_raw:
                continue

            try:
                rating = float(rating_raw)
            except ValueError:
                continue

            sums[brand] += rating
            counts[brand] += 1

        result = []
        for brand in sums:
            avg = sums[brand] / counts[brand]
            result.append({"brand": brand, "rating": round(avg, 2)})

        result.sort(key=lambda x: (-x["rating"], x["brand"]))
        return result
