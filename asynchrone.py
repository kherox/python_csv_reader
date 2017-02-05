import threading
import solrcloud

class Asynchrone():
    """docstring for Asynchrone."""
    def __init__(self):
        self.threads = []
        self.solr = solrcloud.SolrCloudClient()

    def create_thread(self, row):
        t = threading.Thread(target=self.save_handler, args=(row,))
        self.threads.append(t)
        t.start()

    def save_handler(self, row):
        self.solr.save_handler(row)

    def joiner(self):
        for t in self.threads:
            t.join()
