import unittest

from fn_add_guest import calculate_for_add_guests
from fn_allot_water import calculate_for_allot_water

class UnitTestCase(unittest.TestCase):

    def test_ALLOT_WATER(self):
        consumption,cost = calculate_for_allot_water(2,0.5)
        self.assertEqual(consumption,900)
        self.assertEqual(int(cost),1200)
        
        consumption,cost = calculate_for_allot_water(3,2.0)
        self.assertEqual(consumption,1500)
        self.assertEqual(cost,1750)
        
    def test_ADD_GUEST(self):
        consumption,cost = calculate_for_add_guests(5)
        self.assertEqual(consumption,1500)
        self.assertEqual(cost,4000)
        
        consumption,cost = calculate_for_add_guests(1)
        self.assertEqual(consumption,300)
        self.assertEqual(cost,600)
     