import schemathesis

from app.web import app


schema = schemathesis.openapi.from_wsgi("/openapi.yaml", app)


@schema.parametrize()
def test_api_cumple_contrato(case):
    case.call_and_validate()