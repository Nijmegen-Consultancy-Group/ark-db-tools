from unittest import TestCase


class TestSet_calculation(TestCase):

    def tearDown(self):
        from arkdbtools import config as c
        c.CALCULATION_SETTINGS['BLACKLIST'] = None
        c.CALCULATION_SETTINGS['EXCEPTIONS'] = None
        c.CALCULATION_SETTINGS['MAX'] = None
        c.CALCULATION_SETTINGS['SHARE_FEES'] = None

    def test_set_calculation(self):
        from arkdbtools import config as c
        from arkdbtools.dbtools import set_calculation

        resultset = {
            'BLACKLIST': '1',
            'EXCEPTIONS': '2',
            'MAX': '3',
            'SHARE_FEES': '4',
        }
        set_calculation(
            blacklist=  '1',
            exceptions= '2',
            max=        '3',
            share_fees= '4',)
        self.assertCountEqual(c.CALCULATION_SETTINGS, resultset)