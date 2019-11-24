variable "do_token" {
}

variable "gh_token" {
}

provider "digitalocean" {
  version           = "~> 1.5"
  token             = var.do_token
  spaces_access_id  = data.sops_file.secrets.data["digitalocean.spaces.accessId"]
  spaces_secret_key = data.sops_file.secrets.data["digitalocean.spaces.secretKey"]
}

provider "sops" {
  version = "~> v0.3.3"
}

data "sops_file" "secrets" {
  source_file = "secrets.yml"
}

provider "drone" {
}

provider "tls" {
  version = "~> 2.1"
}

provider "github" {
  version      = "~> 2.2"
  token        = var.gh_token
  organization = "croissong"
}

