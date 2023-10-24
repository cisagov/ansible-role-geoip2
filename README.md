# ansible-role-geoip2 #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-geoip2/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-geoip2/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-geoip2/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-geoip2/actions/workflows/codeql-analysis.yml)

An Ansible role for installing a
[MaxMind GeoIP2 database](https://www.maxmind.com/en/geoip2-databases).

## Pre-requisites (Ignore Until the COOL Migration) ##

In order to execute the Molecule tests for this Ansible role in GitHub
Actions, a build user must exist in AWS. The accompanying Terraform
code will create the user with the appropriate name and
permissions. This only needs to be run once per project, per AWS
account. This user can also be used to run the Molecule tests on your
local machine.

Before the build user can be created, you will need a profile in your
AWS credentials file that allows you to read and write your remote
Terraform state.  (You almost certainly do not want to use local
Terraform state for this long-lived build user.)  If the build user is
to be created in the CISA COOL environment, for example, then you will
need the `cool-terraform-backend` profile.

The easiest way to set up the Terraform remote state profile is to
make use of our
[`aws-profile-sync`](https://github.com/cisagov/aws-profile-sync)
utility. Follow the usage instructions in that repository before
continuing with the next steps, and note that you will need to know
where your team stores their remote profile data in order to use
[`aws-profile-sync`](https://github.com/cisagov/aws-profile-sync).

To create the build user, follow these instructions:

```console
cd terraform
terraform init --upgrade=true
terraform apply
```

Once the user is created you will need to update the [repository's
secrets](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets)
with the new encrypted environment variables. This should be done
using the
[`terraform-to-secrets`](https://github.com/cisagov/development-guide/tree/develop/project_setup#terraform-iam-credentials-to-github-secrets-)
tool available in the [development
guide](https://github.com/cisagov/development-guide). Instructions for
how to use this tool can be found in the ["Terraform IAM Credentials
to GitHub Secrets"
section](https://github.com/cisagov/development-guide/tree/develop/project_setup#terraform-iam-credentials-to-github-secrets-).
of the Project Setup README.

If you have appropriate permissions for the repository you can view
existing secrets on the [appropriate
page](https://github.com/cisagov/ansible-role-geoip2/settings/secrets)
in the repository's settings.

## Requirements ##

None.

## Role Variables ##

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| geoip2_local_file | The filename used to store the downloaded database. | `GeoIP2-City.tar.gz` | No |
| geoip2_local_path | The directory to extract the database into. | `/usr/local/share/GeoIP/` | No |
| geoip2_maxmind_edition | The database edition to install. | `GeoIP2-City` | No |
| geoip2_maxmind_license_key | The MaxMind GeoIP2 license key to use when accessing the MaxMind servers. | n/a | Yes |
| geoip2_maxmind_suffix_checksum | The suffix of the database checksum file to be downloaded. | `tar.gz.md5` | No |
| geoip2_maxmind_suffix_file | The suffix of the database file to be downloaded. | `tar.gz` | No |
| geoip2_maxmind_url_base | The base URL for MaxMind. | `https://download.maxmind.com/app/geoip_download` | No |
| geoip2_maxmind_url_format | The format of the MaxMind URL, where the first `%s` represents `geoip2_maxmind_url_base`, the second `%s` represents `geoip2_maxmind_edition`, the third `%s` represents `geoip2_maxmind_suffix_file` or `geoip2_maxmind_suffix_checksum`, and the fourth `%s` represents `geoip2_maxmind_license_key`. | `%s?edition_id=%s&suffix=%s&license_key=%s` | No |

## Dependencies ##

None.

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
