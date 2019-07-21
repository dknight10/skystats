from typing import Any, Generator, Iterable, Sequence


class DataSource:
    def __init__(self, name: str, columns: Sequence[str], data: Iterable[Any]):
        self.name = name
        self.columns = columns
        self._data = data

    def rows(self) -> Generator[Any, None, None]:
        return (row for row in self._data)

    def data(self) -> Generator[Sequence[str], None, None]:
        yield self.columns

        for row in self.rows():
            yield [row[c] for c in self.columns]
