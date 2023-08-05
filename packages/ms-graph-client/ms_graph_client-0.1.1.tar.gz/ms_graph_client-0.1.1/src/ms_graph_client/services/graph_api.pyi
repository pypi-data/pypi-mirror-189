from ms_graph_client.graph_api_config import GraphAPIConfig as GraphAPIConfig
from ms_graph_client.services.applications import Applications
from ms_graph_client.services.groups import Groups
from ms_graph_client.services.users import Users

class GraphAPI:
    groups: Groups
    applications: Applications
    users: Users
    def __init__(self, config: GraphAPIConfig) -> None: ...
