# TODO: set enable_auto_upgrades once avaialable
resource "digitalocean_kubernetes_cluster" "verdun" {
  name    = "verdun"
  region  = "fra1"
  version = "1.14.1-do.2"

  node_pool {
    name       = "worker-pool"
    size       = "s-1vcpu-2gb"
    node_count = 1
    tags = ["verdun"]
  }
}

locals {
  cluster_id = "${digitalocean_kubernetes_cluster.verdun.id}"
  node_pool = "${jsonencode(digitalocean_kubernetes_cluster.verdun.node_pool[0])}"
  node_name = "${replace(local.node_pool, "/.*worker-pool-([a-z0-9]+).*/", "worker-pool-$1")}"
  kube_config = "${jsonencode(digitalocean_kubernetes_cluster.verdun.kube_config.0.raw_config)}"
  cluster_context = "${replace(local.kube_config, "/.*current-context: ([a-z0-9-]+).*/", "$1")}"
}

data "digitalocean_droplet" "verdun_node" {
  name = "${local.node_name}"
}

output "cluster_context" {
  value = "${local.cluster_context}"
}

output "cluster_id" {
  value = "${local.cluster_id}"
}
