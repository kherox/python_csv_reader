# -*- coding: utf-8 -*-
import solr
#getting collection

class SolrCloudClient():
    """docstring for SolrCloudClient."""
    def __init__(self):
         self.client = solr.Solr('http://127.0.0.1:8983/solr/gettingstarted')

    def save_handler(self, data):
        self.client.add(data)
