from sqlalchemy.exc import DatabaseError

from app.models import TestTable
from app import sentry


def test_query():
    try:
        rows = TestTable.query.all()
        return rows
    except DatabaseError:
        sentry.captureException()
        return None
    except Exception as e:
        sentry.captureMessage(e)
        return None
