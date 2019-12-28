data "uptimerobot_account" "account" {}

data "uptimerobot_alert_contact" "default_alert_contact" {
  friendly_name = "${data.uptimerobot_account.account.email}"
}


resource "uptimerobot_monitor" "matrix-synapse" {
  friendly_name = "Matrix Synapse"
  type          = "http"
  url           = "https://matrix.patrician.cloud"
  interval      = 300

  alert_contact {
    id = "${data.uptimerobot_alert_contact.default_alert_contact.id}"
  }
}

resource "uptimerobot_monitor" "matrix-riot" {
  friendly_name = "Matrix Riot"
  type          = "http"
  url           = "https://riot.patrician.cloud"
  interval      = 300

  alert_contact {
    id = "${data.uptimerobot_alert_contact.default_alert_contact.id}"
  }
}

resource "uptimerobot_monitor" "hefeteig-app" {
  friendly_name = "Hefeteig App"
  type          = "http"
  url           = "https://hefeteig.io"
  interval      = 300

  alert_contact {
    id = "${data.uptimerobot_alert_contact.default_alert_contact.id}"
  }
}
