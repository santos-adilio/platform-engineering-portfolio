terraform {
  required_providers {
    proxmox = {
      source  = "Telmate/proxmox"
      version = ">=2.9.0"
    }
  }
}

provider "proxmox" {
  pm_api_url      = "https://192.168.0.7:8006/api2/json"
  pm_api_token_id = "root@pam!tofu"
  pm_api_token_secret = "113f3476-9638-4b2e-9cab-a5ff6dcfbb25"
  pm_tls_insecure = true
}

resource "proxmox_vm_qemu" "vm1" {
  name        = "tofu-test"
  target_node = "pve"
  clone       = "ubuntu-template"

  cores  = 2
  memory = 2048

  disk {
    storage = "local-lvm"
    size    = "20G"
  }

  network {
    bridge = "vmbr0"
  }

  full_clone = true


  sshkeys = file("E:/Desktop/ATALHOS/SSH Keys/OCI-JP.pub")
}
