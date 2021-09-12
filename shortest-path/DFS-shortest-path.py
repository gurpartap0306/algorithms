from graph import Digraph, Node,Edge

def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result 


def DFS(graph,start,end,path,shortest,toPrint=False):

    path=path+[start]

    if toPrint:
        print('Current DFS path:', printPath(path))    
    if start==end:
        return path

    for node in graph.childrenOf(start):
        if node not in path:
            if shortest == None or len(path)<len(shortest):
                newPath=DFS(graph,node,end,path,shortest,toPrint)

                if newPath != None:
                    shortest=newPath

        elif toPrint:
            print('Already visited',node)

        return shortest




def main():
    source='Chicago'
    destination='Phoenix'
    g = Digraph()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'): #Create 7 nodes
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))

    sp=DFS(g, g.getNode(source), g.getNode(destination),[],None,toPrint = True)

    if sp != None:
        print('Shortest path from', source, 'to',
              destination, 'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)

if __name__=='__main__':
    main()




