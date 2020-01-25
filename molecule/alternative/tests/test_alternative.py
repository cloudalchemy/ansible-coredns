import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_directories(host):
    dirs = [
        "/etc/coredns",
        "/etc/coredns/zones",
    ]
    for dir in dirs:
        d = host.file(dir)
        assert d.is_directory
        assert d.exists


def test_service(host):
    s = host.service("coredns")
    assert s.is_running


def test_socket(host):
    sockets = [
        "udp://127.0.0.1:5300"
    ]
    for socket in sockets:
        s = host.socket(socket)
        assert s.is_listening
