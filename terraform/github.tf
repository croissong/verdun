data "github_repository" "verdun" {
  full_name = "croissong/verdun"
}

resource "tls_private_key" "releasewatcher" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "github_repository_deploy_key" "releasewatcher_deploy_key" {
  title      = "Releasewatcher"
  repository = data.github_repository.verdun.name
  key        = tls_private_key.releasewatcher.public_key_openssh
  read_only  = "false"
}
