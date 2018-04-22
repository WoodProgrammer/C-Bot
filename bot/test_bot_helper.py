from bot_helper import run_payload, get_vars
import pytest

payload_name = "docker_registry"

def test_run_payload():
    run_payload(payload_name)

def test_get_vars():
    get_vars(payload_name='docker_registry')
