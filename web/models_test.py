import pytest
from models import Model
obj = Model()

@pytest.mark.skip(reason='Tested Already')
def test_set_payload():
    payload = {'test':'payload'}
    obj._set_payload(payload=payload)
