import datetime


d_regex = '%Y-%m-%d'  # format holidays YYYY-MM-DD
holidays = [  # just insert the holidays time in here
    '2017-12-01', '2017-12-25', '2017-12-26'
]


# Trading time
class TradingTime(object):
    ''' Get Trading Time'''
    def __init__(self, date, session):
        # Monday is 0 and Sunday is 6
        mon_thu = [0, 1, 2, 3]
        fri = 4
        if session == 1:
            # same start trading time
            self.start = datetime.time(hour=9)
            if date in mon_thu:
                self.end = datetime.time(hour=12)
            elif date == fri:
                self.end = datetime.time(hour=11, minute=30)
        elif session == 2:
            # same end trading time
            self.end = datetime.time(hour=15, minute=49)
            if date in mon_thu:
                self.start = datetime.time(hour=13, minute=30)
            elif date == fri:
                self.start = datetime.time(hour=14)

    @staticmethod
    def holiday():
        ''' Create holiday time '''
        global holidays, d_regex

        holiday_time = []
        for holiday_ in holidays:
            holiday_time.append(datetime.datetime.strptime(holiday_, d_regex))
        return holiday_time

# list of symbol
code_symbols = [
    'WSKT', 'MYOR', 'BRPT', 'MIKA', 'WIKA', 'SCMA', 'ADRO', 'PGAS', 'BSDE',
    'KLBF', 'LSIP', 'MNCN', 'SSMS', 'ASGR', 'JPFA', 'PTRO', 'BNGA', 'CTRA',
    'MARK', 'ACES', 'TMAS', 'PNBN', 'TELE', 'SMRA', 'MPMX', 'AISA', 'JRPT',
    'TINS', 'NOBU', 'RALS', 'DOID', 'ASMI', 'SMCB', 'ERAA', 'MEDC', 'SHIP',
    'TARA', 'FORZ', 'CLEO', 'BJTM', 'GJTL', 'ANTM', 'INPP', 'MBSS', 'WTON',
    'LPKR', 'BOGA', 'PWON', 'BNLI', 'AGII', 'PANR', 'MPPA', 'OASA', 'BMTR',
    'SAME', 'SSIA', 'AGRO', 'KREN', 'BBKP', 'SIMA', 'SIMP', 'SIDO', 'PBRX',
    'KRAS', 'APIC', 'ALTO', 'OKAS', 'KBLI', 'ASRI', 'INTA', 'WSBP', 'SRIL',
    'GMFI', 'DILD', 'ARNA', 'GIAA', 'CINT', 'MDLN', 'HOKI', 'MDKI', 'KIJA',
    'TRIS', 'ELSA', 'RANC', 'BEST', 'SOCI', 'MTWI', 'SMDR', 'BUMI', 'APLN',
    'BVIC', 'PNLF', 'BWPT', 'ARMY', 'WOOD', 'META', 'MCOR', 'PPRO', 'IIKP',
    'WEHA', 'PSAB', 'WOMF', 'DMAS', 'BELL', 'MLPL', 'ISSP', 'BTEK', 'TRAM',
    'TRIM', 'BULL', 'FINN', 'RBMS', 'SMMT', 'BBHI', 'BKSL', 'BCIP', 'GPRA',
    'HOME', 'DSFI', 'MYRX'
]
