from app.handlers import BaseHandler
from app.models.test_query import test_query


class TestHandler(BaseHandler):
    def get(self):
        try:
            pass
        except:
            return self.bad_response('Bad request.')

        rows = test_query()
        if rows is None:
            return self.bad_response('Internal error.')
        test_rows = []
        for row in rows:
            test_rows.append({
                "id": row.id,
                "title": row.title,
                "price": row.price
            })
        return self.success_response({"test_rows": test_rows})
