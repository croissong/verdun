provider "digitalocean" {
  version = "~> 1.3"
  token = "${data.sops_file.secrets.data.digitalocean.token}"
  spaces_access_id  = "${data.sops_file.secrets.data.digitalocean.spaces.accessId}"
  spaces_secret_key = "${data.sops_file.secrets.data.digitalocean.spaces.secretKey}"
}

provider "sops" {}

data "sops_file" "secrets" {
  source_file = "secrets.yml"
}
