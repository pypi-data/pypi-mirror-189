import datetime as dt
from collections.abc import Iterator
from decimal import Decimal
from typing import Any

from beartype import beartype
from pandas import DataFrame, NaT, Series
from sqlalchemy.engine import Engine

from utilities.numpy import datetime64ns, has_dtype
from utilities.pandas import (
    Int64,
    boolean,
    string,
    timestamp_to_date,
    timestamp_to_datetime,
)
from utilities.sqlalchemy import get_column_names, get_columns, get_table


@beartype
def insert_dataframe(
    df: DataFrame,
    table_or_model: Any,
    engine: Engine,
    /,
) -> None:
    """Insert a DataFrame into a database."""
    names = get_column_names(table_or_model)
    columns = get_columns(table_or_model)
    all_names_to_columns = dict(zip(names, columns))
    names_to_columns = {
        name: col
        for name, col in all_names_to_columns.items()
        if (df.columns == name).any()
    }
    nativized = (
        _nativize_column(df[name], column)
        for name, column in names_to_columns.items()
    )
    rows = zip(*nativized)
    dicts = [dict(zip(names_to_columns, row)) for row in rows]
    if len(dicts) >= 1:
        table = get_table(table_or_model)
        with engine.begin() as conn:
            _ = conn.execute(table.insert(), list(dicts))


@beartype
def _nativize_column(series: Series, column: Any, /) -> Iterator[Any]:
    py_type = column.type.python_type
    as_list = series.tolist()
    if (
        (has_dtype(series, (bool, boolean)) and (py_type in {bool, int}))
        or (has_dtype(series, float) and (py_type is float))
        or (has_dtype(series, (int, Int64)) and (py_type is int))
        or (has_dtype(series, string) and (py_type is str))
    ):
        values = as_list
    elif has_dtype(series, datetime64ns) and (py_type is dt.date):
        values = [None if t is NaT else timestamp_to_date(t) for t in as_list]
    elif has_dtype(series, datetime64ns) and (py_type is dt.datetime):
        values = [
            None if t is NaT else timestamp_to_datetime(t) for t in as_list
        ]
    else:
        msg = f"Invalid types: {series}, {py_type}"
        raise TypeError(msg)
    for is_null, native in zip(series.isna(), values):
        yield None if is_null else native


@beartype
def read_dataframe(sel: Any, engine: Engine, /) -> DataFrame:
    """Read a table from a database into a DataFrame."""
    with engine.begin() as conn:
        rows = conn.execute(sel).all()
    sel = {col.name: _get_dtype(col) for col in sel.selected_columns}
    return DataFrame(rows, columns=list(sel)).astype(sel)


@beartype
def _get_dtype(column: Any, /) -> Any:
    py_type = column.type.python_type
    if py_type is bool:
        return boolean
    if (py_type is float) or (py_type is Decimal):
        return float
    if py_type is int:
        return Int64
    if py_type is str:
        return string
    if issubclass(py_type, dt.date):
        return datetime64ns
    msg = f"Invalid type: {py_type}"  # pragma: no cover
    raise TypeError(msg)  # pragma: no cover
