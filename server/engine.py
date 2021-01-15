class Engine:
    
    input = None
    algorthim = None
    status = None
    min_match_score = None
    
    
    def __init__(self, input):
        self.input = input
    
    
    # requester - Genome
    def getRecommendation(self, request_genome):
        pass # returns json

    
    def loadGenomes(self):
        pass # Returns void


    # requester - Genome
    def prepareRecommendations(self, requester):
        pass # returns void


    # requester - Genome
    def requestStatus(self, requester):
        pass # returns void

    
    # score: Float
    def updateMinMatchScore(self, score):
        pass # return  void