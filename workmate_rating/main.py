import argparse

from tabulate import tabulate

from workmate_rating.workmate_rating.loader import load_rows_from_files
from workmate_rating.workmate_rating.reports import REPORTS


def parse_args():
    parser = argparse.ArgumentParser(description="Анализ рейтинга брендов")
    parser.add_argument("--files", nargs="+", required=True, help="пути к CSV-файлам")
    parser.add_argument("--report", required=True, help="название отчета")
    return parser.parse_args()


def main():
    args = parse_args()
    rows = load_rows_from_files(args.files)

    report = REPORTS.get(args.report)
    if not report:
        print(f"Неизвестный отчет: {args.report}")
        print(f"Доступные отчеты: {', '.join(REPORTS.keys())}")
        return

    result = report.generate(rows)

    if not result:
        print("Нет данных для отчета.")
        return

    headers = result[0].keys()
    table = [list(item.values()) for item in result]
    print(
        tabulate(
            table,
            headers=headers,
            showindex=range(1, len(result) + 1),
            tablefmt="github",
        )
    )


if __name__ == "__main__":
    main()
