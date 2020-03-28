# TODO: set enable_auto_upgrades once avaialable
resource "digitalocean_kubernetes_cluster" "verdun" {
  name   = "verdun"
  region = "fra1"

  # doctl kubernetes options versions
  version = "1.16.6-do.2"

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
}
