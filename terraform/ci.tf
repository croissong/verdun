resource "tls_private_key" "verdun_ci_ssh_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "github_repository_deploy_key" "verdun_ci_deploy_key" {
  title      = "verdun ci"
  repository = "verdun"
  key        = "${tls_private_key.verdun_ci_ssh_key.public_key_openssh}"
  read_only  = "false"
}

resource "drone_secret" "do_token_get_kubeconf" {
  repository = "Croissong/verdun"
  name    = "DO_TOKEN_GET_KUBECONF"
  value   = "${data.sops_file.secrets.data.digitalocean.tokenReadKubeconf}"
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
  value   = "${data.sops_file.secrets.data.helmGpgKeyB64}"
}

resource "drone_secret" "frontend_deploy_key" {
  repository = "Croissong/verdun-frontend"
  name    = "DEPLOY_KEY_B64"
  value   = "${base64encode(tls_private_key.verdun_ci_ssh_key.private_key_pem)}"
}

resource "drone_secret" "frontend_docker_user" {
  repository = "Croissong/verdun-frontend"
  name    = "DOCKER_USER"
  value   = "${data.sops_file.secrets.data.docker.user}"
}

resource "drone_secret" "frontend_docker_password" {
  repository = "Croissong/verdun-frontend"
  name    = "DOCKER_PASSWORD"
  value   = "${data.sops_file.secrets.data.docker.password}"
}

resource "drone_secret" "ci_docker_user" {
  repository = "Croissong/verdun-ci"
  name    = "DOCKER_USER"
  value   = "${data.sops_file.secrets.data.docker.user}"
}

resource "drone_secret" "ci_docker_password" {
  repository = "Croissong/verdun-ci"
  name    = "DOCKER_PASSWORD"
  value   = "${chomp(data.sops_file.secrets.data.docker.password)}"
}
