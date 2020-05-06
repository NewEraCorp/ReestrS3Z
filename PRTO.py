class PRTO():
    #номер БС, владелец, адрес, антенны
    def __init__(self, bs_num, bs_own, bs_addr, *antennas):
        self.bs_num, self.bs_own, bs_addr, self.antennas = bs_num, bs_own, \
        bs_addr, antennas

    def __repr__(self):
        return "PRTO ('%s', '%s', '%s')" % (self.bs_num, self.bs_own, bs_addr)


class Antenna():
    #фирма, модель, частота, азимут, угол наклона, коэф усиления, ширина ДН
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def __repr__(self):
        return super().__repr__()


class BaseStation():
    #фирма, модель, {стандарт:(кол-во передатчиков, мощность)}
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def __repr__(self):
        return super().__repr__()
