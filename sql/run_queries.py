"""Run the ten original course queries against the bundled SQL snapshot."""
import csv
from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parents[1]


def load_database():
    import pandas as pd
    connection = sqlite3.connect(":memory:")
    frame = pd.read_csv(ROOT / "data" / "Spacex.csv")
    frame = frame[frame["Date"].notna()]
    frame.to_sql("SPACEXTABLE", connection, index=False)
    return connection


def main():
    import pandas as pd
    with load_database() as connection:
        for query_file in sorted(Path(__file__).parent.glob("[0-9][0-9]_*.sql")):
            print(f"\n{query_file.stem}\n")
            print(pd.read_sql_query(query_file.read_text(), connection).to_string(index=False))


if __name__ == "__main__":
    main()
