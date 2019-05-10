variable "do_token_get_kubeconf" {}

resource "circleci_environment_variable" "do_token_get_kubeconf" {
  project = "verdun"
  name    = "DO_TOKEN_GET_KUBECONF"
  value   = "${var.do_token_get_kubeconf}"
}

resource "circleci_environment_variable" "k8s_cluster_id" {
  project = "verdun"
  name    = "DO_K8S_CLUSTER_ID"
  value   = "${digitalocean_kubernetes_cluster.verdun.id}"
}
