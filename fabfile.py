#Fabric
from fabric.api import local


def start():
    "fab start"
    local('foreman run python main.py')
