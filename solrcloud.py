from solrcloudpy.connection import SolrConnection
#getting collection

class SolrCloudClient():
    """docstring for SolrCloudClient."""
    def __init__(self):
        self.conn = SolrConnetion()
        self.node = self.conn['primary_node']

    def save_handler(self, data):
        self.node.add(data)
