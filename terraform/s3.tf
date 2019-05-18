resource "digitalocean_spaces_bucket" "verdun_backup" {
  name = "verdun-backup"
  region  = "fra1"
  acl = "private"
}
