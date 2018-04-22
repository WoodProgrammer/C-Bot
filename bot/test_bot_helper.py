from bot_helper import run_payload, verify_vars, generate_docker_file
import pytest

payload_name = "docker"

@pytest.mark.skip(reason="Stopped")
def test_run_payload():
    return run_payload(payload_name)


def test_verify_vars():
    verify_vars('docker')

def test_generate_docker_file():
    generate_docker_file(payload_name=payload_name)
