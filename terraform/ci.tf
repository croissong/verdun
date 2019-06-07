variable "do_token_get_kubeconf" {}
variable "helm_gpg_key_b64" {}
variable "docker_user" {}
variable "docker_password_b64" {}

provider "drone" {}


resource "drone_secret" "do_token_get_kubeconf" {
  repository = "Croissong/verdun"
  name    = "DO_TOKEN_GET_KUBECONF"
  value   = "hi"
}

resource "drone_secret" "k8s_cluster_id" {
  repository = "Croissong/verdun"
  name    = "DO_K8S_CLUSTER_ID"
  value   = "${local.cluster_id}"
}

resource "drone_secret" "k8s_cluster_context" {
  repository = "Croissong/verdun"
  name    = "K8S_CLUSTER_CONTEXT"
  value   = "${local.cluster_context}"
}

resource "drone_secret" "helm_gpg_key_b64" {
  repository = "Croissong/verdun"
  name    = "HELM_GPG_KEY_B64"
  value   = "${var.helm_gpg_key_b64}"
}

resource "drone_secret" "docker_user" {
  repository = "Croissong/verdun"
  name    = "DOCKER_USER"
  value   = "${var.docker_user}"
}

resource "drone_secret" "docker_password_b64" {
  repository = "Croissong/verdun"
  name    = "DOCKER_PASSWORD_B64"
  value   = "${var.docker_password_b64}"
}
