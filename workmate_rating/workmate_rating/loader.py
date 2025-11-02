import csv
import sys


def load_rows_from_files(paths):
    rows = []
    for path in paths:
        try:
            with open(path, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f, delimiter="\t")
                for row in reader:
                    if any(row.values()):
                        rows.append(row)
        except FileNotFoundError:
            print(f"Ошибка: Файл не найден по пути '{path}'")
            sys.exit(1)
    return rows
