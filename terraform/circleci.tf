variable "circleci_token" {}
variable "do_token_get_kubeconf" {}

provider "circleci" {
  api_token    = "${var.circleci_token}"
  vcs_type     = "github"
  organization = "Croissong"
}

resource "circleci_environment_variable" "do_token_get_kubeconf" {
  project = "verdun"
  name    = "DO_TOKEN_GET_KUBECONF"
  value   = "${var.do_token_get_kubeconf}"
}

resource "circleci_environment_variable" "k8s_cluster_id" {
  project = "verdun"
  name    = "DO_K8S_CLUSTER_ID"
  value   = "${local.cluster_id}"
}

resource "circleci_environment_variable" "k8s_cluster_context" {
  project = "verdun"
  name    = "K8S_CLUSTER_CONTEXT"
  value   = "${local.cluster_context}"
}
