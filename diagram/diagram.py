from diagrams import Cluster, Diagram
from diagrams.onprem.compute import Server
from diagrams.generic.virtualization import Vmware
from diagrams.generic.os import Ubuntu
from diagrams.onprem.vcs import Github

with Diagram("Simple standalone ESXi homelab with Ubuntu farm", show=False):
    controller = Server("controller")
    ESXi = Vmware("esxi7.0")
    github = Github("repo")

    with Cluster("Ubuntu farm"):
        ubntu_cluster = Ubuntu("ubnt1")
        ubntu_cluster - [Ubuntu("ubnt2"),
                        Ubuntu("ubnt3")]

    github >> controller >> ESXi >> ubntu_cluster
