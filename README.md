# ansible-role-geoip2 #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-geoip2/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-geoip2/actions)
[![License](https://img.shields.io/github/license/cisagov/ansible-role-geoip2)](https://spdx.org/licenses/)
[![CodeQL](https://github.com/cisagov/ansible-role-geoip2/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-geoip2/actions/workflows/codeql-analysis.yml)

An Ansible role for installing a
[MaxMind GeoIP2 database](https://www.maxmind.com/en/geoip2-databases). Additionally,
it can install the [MaxMind `geoipupdate` tool](https://github.com/maxmind/geoipupdate)
and add a systemd service and timer to run the tool at regular intervals.

## Requirements ##

None.

## Role Variables ##

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| geoip2\_database\_directory | The directory in which to store the database files. | `/usr/local/share/GeoIP/` | No |
| geoip2\_geoipupdate\_auto\_update | Whether to configure automatic updates when `geoipupdate` is installed. | `true` | No |
| geoip2\_geoipupdate\_service\_name | The name to use for the `geoipupdate` systemd service and timer. | `geoipupdate` | No |
| geoip2\_geoipupdate\_service\_timer\_on\_calendar | The calendar expression for the `geoipupdate` systemd timer's `OnCalendar` option. | `Wed,Sat America/New_York` | No |
| geoip2\_geoipupdate\_service\_timer\_randomized\_delay\_sec | The time span value for the `geoipupdate` systemd timer's `RandomizedDelaySec` option. | `3h` | No |
| geoip2\_geoipupdate\_version | The version of `geoipupdate` to install. Note that this value should be quoted and must represent a release available in the maxmind/geoipupdate GitHub repository. | `"7.0.1"` | No |
| geoip2\_install\_geoipupdate | Whether to install the `geoipupdate` tool. | `false` | No |
| geoip2\_install\_geoipupdate\_from\_github | Install the `geoipupdate` tool from GitHub instead of the system package (if available). | `false` | No |
| geoip2\_maxmind\_account\_id | The MaxMind account ID to use when accessing the MaxMind servers. | n/a | Yes |
| geoip2\_maxmind\_editions | The list of database editions to install. | `[GeoIP2-City]` | No |
| geoip2\_maxmind\_license\_key | The MaxMind GeoIP2 license key to use when accessing the MaxMind servers. | n/a | Yes |
| geoip2\_maxmind\_suffix\_checksum | The suffix of the database checksum file to be downloaded. | `tar.gz.sha256` | No |
| geoip2\_maxmind\_suffix\_file | The suffix of the database file to be downloaded. | `tar.gz` | No |
| geoip2\_maxmind\_url\_base | The format of the MaxMind URL, where the first `%s` represents `geoip2_maxmind_edition` and the second `%s` represents `geoip2_maxmind_suffix_file` or `geoip2_maxmind_suffix_checksum`. | `https://download.maxmind.com/geoip/databases/%s/download?suffix=%s` | No |

## Dependencies ##

None.

## Installation ##

This role can be installed via the command:

```console
ansible-galaxy install --role-file path/to/requirements.yml
```

where `requirements.yml` looks like:

```yaml
---
- name: geoip2
  src: https://github.com/cisagov/ansible-role-geoip2
```

and may contain other roles as well.

For more information about installing Ansible roles via a YAML file,
please see [the `ansible-galaxy`
documentation](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#installing-multiple-roles-from-a-file).

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: true
  become_method: sudo
  tasks:
    - name: Download the MaxMind GeoIP2 database
      ansible.builtin.include_role:
        name: geoip2
      vars:
        geoip2_maxmind_account_id: <valid MaxMind account ID>
        geoip2_maxmind_license_key: <valid MaxMind GeoIP2 license key>
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Nicholas McDonnell - <nicholas.mcdonnell@gwe.cisa.dhs.gov>
