class TrainTicket:
    def __init__(self):
        self.__fare = 0
    
    def set_fare(self, fare):
        if(fare >= 0):
            self.__fare = fare
        else:
            print("Invalid amount!")
        
    def get_fare(self):
        return self.__fare
    
