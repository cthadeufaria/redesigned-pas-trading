class Model:
    def __init__(self, vpk, dpk, nak, r, pk, uk):
        self.vpk = vpk
        self.dpk = dpk
        self.nak = nak
        self.r = r
        self.pk = pk
        self.uk = uk

    def model(self):
        vpk1 = vpk + dpk*nak + dpk*uk - r*pk*np.absolute(uk)
        return vpk1