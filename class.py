class Factory :

    def __init__(self , material , zips , pockets) :

        self .material = material
        self.zips = zips
        self.pockets = pockets

campus = Factory ("leather",5,2)
skybag = Factory ("waterproff",6,3)

print(campus.pockets)
