import pytest
from models import Model
obj = Model()

@pytest.mark.skip(reason='Tested Already')
def test_set_payload():
    payload = {'id':'1','payload':'Committed REPO_URL, branch:staging, job:docker_hub','credentials':{'user':'test','password':'passwd'}}
    obj._set_payload(payload=payload)

@pytest.mark.skip(reason='Tested Already')
def test_payload_detail():
    id = '1'
    print(obj._get_detail(id=id))
