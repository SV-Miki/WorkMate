import os
import sys
import tempfile

from workmate_rating.main import main


def test_main_average_rating_report(capsys):
    content = (
        "name\tbrand\tprice\trating\niphone\tapple\t999\t4.9\nredmi\txiaomi\t199\t4.5\n"
    )
    path = tempfile.mktemp(suffix=".csv")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

    sys.argv = ["main.py", "--files", path, "--report", "average-rating"]

    main()
    captured = capsys.readouterr().out

    assert "apple" in captured
    assert "xiaomi" in captured
    assert "rating" in captured

    os.remove(path)
