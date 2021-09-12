class Node(object):
    def __init__(self,data):
        self.data=data

    def getData(self):
        return self.data

    def __str__(self):
        return self.data


class Edge(object):
    def __init__(self,src,dest):
        self.src=src
        self.dest=dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self) -> str:
        return f'{self.src}->{self.dest}'


class Digraph(object):
    def __init__(self):
        self.edges={}

    def addNode(self,node):
        if node in self.edges:
            raise ValueError('Node already in graph')
        else:
            self.edges[node]=[]
    
    def addEdge(self,edge):
        src=edge.getSource()
        dest=edge.getDestination()

        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        else:
            self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, data):
        for n in self.edges:
            if n.getData() == data:
                return n
        raise NameError(data)

    def __str__(self):
        result=''
        for src in self.edges:
            for dest in self.edges[src]:
                result=result+src.getData()+'->'+dest.getData()+'\n'
        return result[:-1]

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)


def main():
    graph = Graph()

    graph.addNode(Node('Patiala'))
    graph.addNode(Node('Nabha'))
    graph.addNode(Node('Rajpura'))


    graph.addEdge(Edge(graph.getNode('Patiala'),graph.getNode('Nabha')))
    graph.addEdge(Edge(graph.getNode('Patiala'),graph.getNode('Rajpura')))


    print(graph)



if __name__=='__main__':
    main()