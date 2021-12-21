# home-vmware-baremetal

Simple collection of ansible plays to kickstart an ESXi homelab to host some other home projects like k3s and monitoring tools for small lab rack.

## Hardware

| Information| Description |
| :---  | :---  |
| ESXi | ESXi-7.0U2a-17867351-standard |
| Vendor | LENOVO |
| CPU | 8 CPUs x Intel(R) Xeon(R) CPU E5-2637 v2 @ 3.50GHz |
| MEM | 103.92 GB |
| OS STORAGE | 1TB Samsung 850 Pro |
| DATASTORE | 2TB Samsung 850 Pro |

## Requirements

Tools to be installed prior to deploy run. Currently using homebrew when on macosx and chocolatey if on windows (not documented here).

    brew install age
    brew install ansible
    brew install pre-commit
    brew install yamllint
    brew install sops
    ansible-galaxy collection install -r requirements.yml
    pip install -r ~/.ansible/collections/ansible_collections/community/vmware/requirements.txt
    source setup-sops.sh age1ExampleRecipientPublicKey1

copy age keys.txt to `/Users/<username>/Library/Application Support/sops/age/keys.txt` for ansible community.sops.load_vars to decrypt secrets.

## Deploy
Once all the tools are installed to work within the repo and deploy run the following:

    ansible-playbook playbooks/esxi.yml --ask-become-pass -b

## Secrets

When required throw any ESXi secrets in a basic [sops](https://github.com/mozilla/sops) file backed by [age](https://github.com/FiloSottile/age) key.

    sops -e -i playbooks/vars/esxi.sops.yml
    sops -d -i playbooks/vars/esxi.sops.yml

## TODO

- Figure out why ansible doesn't like custom keys.txt locations. Moved to default for now.
- Add some mingrammer diagrams.
