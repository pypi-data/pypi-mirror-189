import datetime as dt
from typing import Any

from beartype import beartype
from hypothesis.strategies import SearchStrategy, composite, dates, datetimes

from utilities.datetime import UTC
from utilities.hypothesis import lift_draw
from utilities.pandas import (
    TIMESTAMP_MAX_AS_DATE,
    TIMESTAMP_MAX_AS_DATETIME,
    TIMESTAMP_MIN_AS_DATE,
    TIMESTAMP_MIN_AS_DATETIME,
)


@beartype
def dates_pd(
    *,
    min_value: dt.date = TIMESTAMP_MIN_AS_DATE,
    max_value: dt.date = TIMESTAMP_MAX_AS_DATE,
) -> SearchStrategy[dt.date]:
    """Strategy for generating dates which can become Timestamps."""
    return dates(min_value=min_value, max_value=max_value)


@composite
@beartype
def datetimes_pd(
    _draw: Any,
    /,
    *,
    min_value: dt.datetime = TIMESTAMP_MIN_AS_DATETIME,
    max_value: dt.datetime = TIMESTAMP_MAX_AS_DATETIME,
) -> dt.datetime:
    """Strategy for generating datetimes which can become Timestamps."""
    draw = lift_draw(_draw)
    datetime = draw(
        datetimes(
            min_value=min_value.replace(tzinfo=None),
            max_value=max_value.replace(tzinfo=None),
        ),
    )
    return datetime.replace(tzinfo=UTC)
