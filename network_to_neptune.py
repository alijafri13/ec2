from __future__  import print_function  # Python 2/3 compatibility
import datetime
from gremlin_python import statics
from gremlin_python.structure.graph import Graph

from gremlin_python.process.graph_traversal import __
from gremlin_python.process.strategies import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.traversal import T
from gremlin_python.process.traversal import Cardinality

graph = Graph()
time = datetime.datetime.now() # @Ali may want to move this into the loop ... your call.

id = T.id
single = Cardinality.single
remoteConn = DriverRemoteConnection('wss://database-test-instance-1.cchiln9n1l8z.us-west-2.neptune.amazonaws.com:8182/gremlin','g')
g = graph.traversal().withRemote(remoteConn)


def CLEAR_ALL_DO_NOT_RUN():
    g.V().drop().iterate()



def add_node(actant_label, ownership = "X", link = "", date_ = time, type_ = "actant"):
    if type_ == "actant":
        try:
            count = int(g.V(actant_label).values('weight').next())
            g.V(actant_label).property(single, 'weight', count+1).next()
            g.V(actant_label).property(single, 'date', date_).next()
        except:
            g.addV(type_). \
                property(id, actant_label). \
                property("name", actant_label). \
                property("ownership", ownership). \
                property("weight", "1"). \
                property("link", link). \
                property("date", date_).next()



def add_edge(edge_label, from_label, to_label, ownership = "X", link = "", date_ = time, type_ = "text_rel"):
    if type_ == "text_rel":
        try:    
            count = int(g.E(edge_label).values('weight').next())
            g.E(edge_label).property('date', date_).next()
            g.E(edge_label).property('weight', count+1).next()
        except:
            g.V(to_label).as_('t').V(from_label).addE(type_). \
                property(id, edge_label). \
                property("name", edge_label). \
                property("date", date_).to("t"). \
                property("weight", "1"). \
                property("ownership", ownership). \
                property("link", link). \
                toList()


# add_node("G")
# add_node("H")
# add_node("I")
# add_node("X")

# add_edge("gh","G","H")
# add_edge("eg","G","I")
# add_edge("ez","X","G")

# #print(g.E().hasLabel('ab').valueMap().next())
# in_nodes = g.V("G","I").in_().valueMap().toList()
# out_nodes = g.V("G").out().valueMap().toList()
from rake_nltk import Rake
import pandas as pd

r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.

def pull_keywords_from_question(question="Is cd38 a good man?"):
    r.extract_keywords_from_text(question)
    return r.get_ranked_phrases()


def pull_database_from_keywords(list_of_keywords=[]):
    full_list_of_graph = g.V(list_of_keywords).bothE().elementMap().dedup().toList()
    full_list_of_graph = g.V(["G","I"]).bothE().elementMap().dedup().toList()

    D = {}
    diction = {"rel":[], "type":[], "source":[], "source_type": [], "target":[], "target_type":[]}
    for logic in full_list_of_graph:

        for key,val in logic.items():
            D[str(key)] = val

        try:
            diction["rel"].append(D["T.id"])
            diction["type"].append(D["T.label"])
            diction["source"].append(D["Direction.IN"][T.id])
            diction["source_type"].append(D["Direction.IN"][T.label])
            diction["target"].append(D["Direction.OUT"][T.id])
            diction["target_type"].append(D["Direction.OUT"][T.label])
        except:
            print("Error retrieving Neptune data. Check config logs.")

    df = pd.DataFrame.from_dict(diction)
    return df

keywords = pull_keywords_from_question("Is G a friend of H?")
print(pull_database_from_keywords(keywords))


#print(g.V("G").emit().toList())
#print(in_nodes)
#print(out_nodes)

#print(g.V('G').both().otherV().valueMap().toList())


