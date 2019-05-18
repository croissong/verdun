provider "kubernetes" {
  host    = "${digitalocean_kubernetes_cluster.verdun.kube_config.0.host}"
  version = "~> 1.6"
}

resource "kubernetes_namespace" "tiller" {
  metadata {
    annotations {
      name = "tiller"
    }

    labels {
      verdun = "tiller"
    }

    name = "tiller"
  }
}

resource "kubernetes_service_account" "tiller" {
  metadata {
    name = "tiller"
    namespace = "tiller"
  }
}

resource "kubernetes_cluster_role_binding" "tiller" {
    metadata {
        name = "tiller"
    }
    role_ref {
        api_group = "rbac.authorization.k8s.io"
        kind = "ClusterRole"
        name = "cluster-admin"
    }
    subject {
        kind = "ServiceAccount"
        name = "tiller"
        namespace = "tiller"
    }
}

provider "helm" {
  version = "~> 0.9"
  namespace = "tiller"
  install_tiller  = true
  tiller_image = "gcr.io/kubernetes-helm/tiller:canary"
  service_account = "tiller"
  max_history = "200"
  kubernetes {
    host    = "${digitalocean_kubernetes_cluster.verdun.kube_config.0.host}"
  }
}


# https://github.com/terraform-providers/terraform-provider-helm/issues/134#issuecomment-478580126

data "helm_repository" "incubator" {
  name = "incubator"
  url = "https://kubernetes-charts-incubator.storage.googleapis.com"
}

resource "helm_release" "raw_hello_world" {
  name = "hello-world"
  namespace = "tiller"
  depends_on = ["kubernetes_cluster_role_binding.tiller"]
  repository = "${data.helm_repository.incubator.metadata.0.name}"
  chart = "incubator/raw"
}
