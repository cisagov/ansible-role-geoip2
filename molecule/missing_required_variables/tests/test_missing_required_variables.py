"""Module containing the tests for the missing_required_variables scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "f", ["/usr/local/share/GeoIP", "/usr/local/share/GeoIP/GeoIP2-City.tar.gz"]
)
def test_files(host, f):
    """Test that the expected files and directories are not present."""
    assert host.file(f).exists is False
