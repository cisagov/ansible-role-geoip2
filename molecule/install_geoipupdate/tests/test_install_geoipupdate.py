"""Module containing the tests for the install_geoipupdate scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_package(host):
    """Test that the package was installed."""
    # There is no system package available for Debian Buster
    if not (
        host.system_info.distribution == "debian"
        and host.system_info.codename == "buster"
    ):
        assert host.package("geoipupdate").is_installed


@pytest.mark.parametrize("f,m", [("/etc/GeoIP.conf", 0o644)])
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
        "Using config file /etc/GeoIP.conf" in cmd.stderr
    ), "Missing expected config file"
    assert (
        "Using database directory /usr/local/share/GeoIP" in cmd.stderr
    ), "Missing expected database directory"
    assert (
        "Database GeoIP2-City up to date" in cmd.stderr
    ), "Missing expected database update"
