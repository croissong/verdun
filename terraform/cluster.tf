# TODO: set enable_auto_upgrades once avaialable
resource "digitalocean_kubernetes_cluster" "verdun" {
  name   = "verdun"
  region = "fra1"

  # curl -s -H "Authorization: Bearer $do_token" "https://api.digitalocean.com/v2/kubernetes/options" | jq '.options.versions'
  version = "1.15.5-do.0"

  node_pool {
    name       = "worker-pool"
    size       = "s-2vcpu-4gb"
    node_count = 1
    tags       = ["verdun"]
  }
}

locals {
  cluster_id = digitalocean_kubernetes_cluster.verdun.id
  node_pool  = jsonencode(digitalocean_kubernetes_cluster.verdun.node_pool[0])
  node_name = replace(
    local.node_pool,
    "/.*worker-pool-([a-z0-9]+).*/",
    "worker-pool-$1",
  )
  kube_config = jsonencode(
    digitalocean_kubernetes_cluster.verdun.kube_config[0].raw_config,
  )
  cluster_context = replace(
    local.kube_config,
    "/.*current-context: ([a-z0-9-]+).*/",
    "$1",
  )
}

data "digitalocean_droplet" "verdun_node" {
  name = local.node_name
}

resource "digitalocean_firewall" "verdun_infra" {
  name = "verdun-infra"

  droplet_ids = [data.digitalocean_droplet.verdun_node.id]

  inbound_rule {
    protocol         = "icmp"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  inbound_rule {
    protocol         = "tcp"
    port_range       = "1-65535"
    source_addresses = ["10.0.0.0/8", "172.16.0.0/20", "192.168.0.0/16"]
  }

  inbound_rule {
    protocol         = "udp"
    port_range       = "1-65535"
    source_addresses = ["10.0.0.0/8", "172.16.0.0/20", "192.168.0.0/16"]
  }

  inbound_rule {
    protocol         = "tcp"
    port_range       = "30000-32767"
    source_addresses = ["0.0.0.0/0"]
  }

  inbound_rule {
    protocol         = "udp"
    port_range       = "30000-32767"
    source_addresses = ["0.0.0.0/0"]
  }

  inbound_rule {
    protocol         = "tcp"
    port_range       = "80"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  inbound_rule {
    protocol         = "tcp"
    port_range       = "443"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  # mumble

  inbound_rule {
    protocol         = "tcp"
    port_range       = "64738"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  inbound_rule {
    protocol         = "udp"
    port_range       = "64738"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  # rtmp
  inbound_rule {
    protocol         = "tcp"
    port_range       = "1935"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  outbound_rule {
    protocol              = "tcp"
    port_range            = "1-65535"
    destination_addresses = ["0.0.0.0/0", "::/0"]
  }

  outbound_rule {
    protocol              = "udp"
    port_range            = "1-65535"
    destination_addresses = ["0.0.0.0/0", "::/0"]
  }

  outbound_rule {
    protocol              = "icmp"
    destination_addresses = ["0.0.0.0/0", "::/0"]
  }
}

output "cluster_context" {
  value = local.cluster_context
}

output "cluster_id" {
  value = local.cluster_id
}

