import pytest
import os
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("files", [
    "/usr/local/bin/coredns",
    "/etc/coredns/Corefile",
    "/etc/systemd/system/coredns.service"
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file


def test_user(host):
    assert host.group("coredns").exists
    assert host.user("coredns").exists


def test_service(host):
    s = host.service("coredns")
    # assert s.is_enabled
    assert s.is_running


def test_socket(host):
    s = host.socket("tcp://0.0.0.0:53")
    assert s.is_listening
