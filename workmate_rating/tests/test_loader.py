import os
import tempfile

from workmate_rating.workmate_rating.loader import load_rows_from_files


def test_load_rows_from_files():
    content = "name\tbrand\tprice\trating\niphone\tapple\t999\t4.9\n"
    path = tempfile.mktemp(suffix=".csv")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    rows = load_rows_from_files([path])
    assert len(rows) == 1
    assert rows[0]["brand"] == "apple"

    os.remove(path)
