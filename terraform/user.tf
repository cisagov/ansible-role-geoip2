# Create the test user
module "user" {
  source = "github.com/cisagov/molecule-iam-user-tf-module"

  providers = {
    aws                         = aws.users
    aws.images-provisionaccount = aws.images_provisionaccount
    aws.images-ssm              = aws.images_ssm
  }

<<<<<<< HEAD
  entity = "ansible-role-geoip2"
  ssm_parameters = [
    "/cyhy/core/geoip/account_id",
    "/cyhy/core/geoip/license_key",
  ]
=======
  entity = "skeleton-ansible-role-with-test-user"

  # If necessary, provide a list of SSM parameters that the test user needs to
  # be able to read
  # ssm_parameters = ["/example/parameter"]
>>>>>>> 26819a903c52b39dce7b3673f54402d3d281fba3
}
