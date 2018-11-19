variable "do_token" {}

# Configure the DigitalOcean Provider
provider "digitalocean" {
  token = "${var.do_token}"
}

## patrician.gold

### domain

resource "digitalocean_domain" "patrician" {
  name = "patrician.gold"
}

### records

resource "digitalocean_record" "patrician_root" {
  domain  = "${digitalocean_domain.patrician.name}"
  type = "A"
  value = "139.59.145.153"
  name    = "@"
}

resource "digitalocean_record" "patrician_wildcard" {
  domain  = "${digitalocean_domain.patrician.name}"
  type = "A"
  value = "139.59.145.153"
  name    = "*"
}
