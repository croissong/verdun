resource "digitalocean_spaces_bucket" "verdun" {
  name = "verdun"
  region  = "fra1"
  acl = "private"
}
