"""Functions for wiritng datetime intervals."""

import datetime as dt
import uuid

from sqlalchemy import orm as sa_orm

from pvsite_datamodel.sqlmodels import DatetimeIntervalSQL
from pvsite_datamodel.write.upsert import upsert
from pvsite_datamodel.write.utils import FORECAST_TIMESPAN, WrittenRow


def get_or_else_create_datetime_interval(
    session: sa_orm.Session, start_time: dt.datetime, end_time: dt.datetime | None = None
) -> tuple[DatetimeIntervalSQL, list[WrittenRow]]:
    """Gets/creates a DatetimeInterval from the DB depending on existence.

    :param session: The SQLAlchemy session used for performing db updates
    :param start_time: The start time of the datetime interval
    :param end_time: The end time of the datetime interval. Optional, defaults to the start_time
    + FORECAST_TIMESPAN
    :return tuple(DatetimeIntervalSQL, list[WrittenRow]): A tuple containing the existing
    or created DatetimeIntervalSQL object, and a list of WrittenRow objects dictating what was
    written to the DB
    """
    # End time defaults to the start time + FORECAST_TIMESPAN timedelta
    if end_time is None:
        end_time = start_time + FORECAST_TIMESPAN

    # Check if a datetime interval exists for the input times
    query = session.query(DatetimeIntervalSQL)
    query = query.filter(DatetimeIntervalSQL.start_utc == start_time)
    query = query.filter(DatetimeIntervalSQL.end_utc == end_time)
    existing_interval: DatetimeIntervalSQL = query.first()

    # If it does, fetch it's uuid
    if existing_interval is not None:
        return existing_interval, []

    # If it doesn't, create a new one
    else:
        datetime_interval: DatetimeIntervalSQL = DatetimeIntervalSQL(
            datetime_interval_uuid=uuid.uuid4(),
            start_utc=start_time,
            end_utc=end_time,
            created_utc=dt.datetime.now(tz=dt.timezone.utc),
        )
        written_rows = upsert(session, DatetimeIntervalSQL, [datetime_interval.__dict__])
        return datetime_interval, written_rows
