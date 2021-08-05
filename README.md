# ansible-role-geoip2 #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-geoip2/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-geoip2/actions)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/cisagov/ansible-role-geoip2.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-geoip2/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/cisagov/ansible-role-geoip2.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-geoip2/context:python)

An Ansible role for installing a
[MaxMind GeoIP2 database](https://www.maxmind.com/en/geoip2-databases).

## Pre-requisites (Ignore Until the COOL Migration) ##

In order to execute the Molecule tests for this Ansible role in GitHub
Actions, a build user must exist in AWS. The accompanying Terraform
code will create the user with the appropriate name and
permissions. This only needs to be run once per project, per AWS
account. This user can also be used to run the Molecule tests on your
local machine.

Before the build user can be created, the following profile must exist in
your AWS credentials file:

- `cool-terraform-backend`

The easiest way to set up that profile is to use our
[`aws-profile-sync`](https://github.com/cisagov/aws-profile-sync)
utility. Follow the usage instructions in that repository before
continuing with the next steps. Note that you will need to know where
your team stores their remote profile data in order to use
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

The majority of the variables defined in
[`defaults/main.yml`](defaults/main.yml) are fine as provided, but this role
requires the following variables:

* `maxmind_license_key` - The MaxMind GeoIP2 license key to use when
  accessing the MaxMind servers.

Additionally, the following variables may be useful to override:

* `maxmind_edition` - The database edition to install.
* `geoip_local_path` - The directory to extract the database into.
* `geoip_local_file` - The filename used to store the downloaded database.

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: yes
  become_method: sudo
  roles:
    - geoip2
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

Nicholas McDonnell - <nicholas.mcdonnell@trio.dhs.gov>
