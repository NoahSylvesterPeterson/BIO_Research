graph = {"v1":{9:"v3",2:"v2"}, "v2":{1:"v1",4:"v4",6:"v3"}, "v3":{8:"v4", 7:"v2"}, "v4":{6:"v1",3:"v2"}}



def OptimalTour(g):
    possible = g.keys()
    possible.remove("v1")

    Actions = g["v1"].keys().sort()
    