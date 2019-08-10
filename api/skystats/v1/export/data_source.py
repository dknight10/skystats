from typing import Any, Generator, Iterable, Sequence, Tuple, Union


class DataSourceColumn:
    def __init__(self, column):
        if isinstance(column, tuple):
            self.name = column[0]
            self.display = column[1]
        elif isinstance(column, str):
            self.name = column
            self.display = column
        else:
            raise ValueError("Column values should be tuple or str")


class DataSource:
    def __init__(
        self,
        name: str,
        columns: Sequence[Union[str, Tuple[str, str]]],
        data: Iterable[Any],
    ):
        self.name = name
        self.columns = [DataSourceColumn(c) for c in columns]
        self._data = data

    def rows(self) -> Generator[Any, None, None]:
        return (row for row in self._data)

    def data(self) -> Generator[Sequence[str], None, None]:
        yield [c.display for c in self.columns]

        for row in self.rows():
            yield [getattr(row, c.name) for c in self.columns]
