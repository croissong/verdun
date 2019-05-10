# TODO: set enable_auto_upgrades once avaialable
resource "digitalocean_kubernetes_cluster" "verdun" {
  name    = "verdun"
  region  = "fra1"
  version = "1.13.5-do.1"

  node_pool {
    name       = "worker-pool"
    size       = "s-1vcpu-2gb"
    node_count = 1
    tags = ["verdun"]
  }
}

data "digitalocean_kubernetes_cluster" "verdun" {
  name = "${digitalocean_kubernetes_cluster.verdun.name}"
}

locals {
  node_pool = "${digitalocean_kubernetes_cluster.verdun.node_pool[0]}"
  json = "${jsonencode(local.node_pool)}"
  node_name = "${replace(local.json, "/.*worker-pool-([a-z0-9]+).*/", "worker-pool-$1")}"
}

data "digitalocean_droplet" "verdun_node" {
  name = "${local.node_name}"
}
