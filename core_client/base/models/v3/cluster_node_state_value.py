from enum import Enum


class ClusterNodeStateValue(str, Enum):
    online = "online"
    maintenance = "maintenance"
    leave = "leave"
