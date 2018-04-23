from bot_helper import run_payload
import pytest

payload_name = "docker_registry,asd,asd,asd"

def test_run_payload():
    run_payload(payload_name)
