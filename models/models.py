class Fix:
    """
    Класс для описания любой точки пути
    """
    def __init__(self, id_, freq, trk, dist, xCoord, yCoord, name):
        self.id = id_
        self.freq = freq
        self.trk = trk
        self.dist = dist
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.name = name

    def __repr__(self):
        return str(self.id)
