"""Module containing the tests for the install_geoipupdate scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "f,m", [("/usr/bin/geoipupdate", 0o755), ("/etc/GeoIP.conf", 0o644)]
)
def test_files(host, f, m):
    """Test that the expected files are present."""
    assert host.file(f).exists
    assert host.file(f).is_file
    assert host.file(f).mode == m
    assert host.file(f).user == "root"
    assert host.file(f).group == "root"


def test_geoipupdate_binary(host):
    """Test that geoipupdate runs successfully."""
    cmd = host.run("/usr/bin/geoipupdate --verbose")
    assert cmd.rc == 0
    assert (
        "geoipupdate version 7.0.1" in cmd.stderr
    ), "Missing expected geoipupdate version"
    assert (
        "Using config file /etc/GeoIP.conf" in cmd.stderr
    ), "Missing expected config file"
    assert (
        "Using database directory /usr/local/share/GeoIP" in cmd.stderr
    ), "Missing expected database directory"
    assert (
        "Database GeoIP2-City up to date" in cmd.stderr
    ), "Missing expected database update"
