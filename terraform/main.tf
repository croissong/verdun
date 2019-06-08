variable "do_token" {}
variable "gh_token" {}

provider "digitalocean" {
  version = "~> 1.3"
  token = "${var.do_token}"
  spaces_access_id  = "${data.sops_file.secrets.data.digitalocean.spaces.accessId}"
  spaces_secret_key = "${data.sops_file.secrets.data.digitalocean.spaces.secretKey}"
}

provider "sops" {}

data "sops_file" "secrets" {
  source_file = "secrets.yml"
}

provider "drone" {}

provider "github" {
  token        = "${var.gh_token}"
  organization = "croissong"
}
