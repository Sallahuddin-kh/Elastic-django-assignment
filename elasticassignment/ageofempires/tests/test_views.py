from django.test import SimpleTestCase
from django.urls import reverse

class TestViews(SimpleTestCase):

    def test_civilizations(self):
        """
        Test if only civilization data exists in civilization index
        """
        response_data = self.client.get(reverse('civilizations'))
        civilization_list = response_data.context['civilization_list']
        flag = True
        msg = "CORRECT DATA BEING SHOWN"
        for civilization in civilization_list:
            if civilization["_index"] != 'civilizations':
                flag = False
                msg = "IRRELEVANT DATA ALSO BEING SHOWN"
        self.assertTrue(flag , msg = msg)

    def test_units(self):
        """
        Test if only unit data exists in units index
        """
        response_data = self.client.get(reverse('units'))
        units_list = response_data.context['units_list']
        flag = True
        msg = "CORRECT DATA BEING SHOWN"
        for unit in units_list:
            if unit["_index"] != 'units':
                flag = False
                msg = "IRRELEVANT DATA ALSO BEING SHOWN"
        self.assertTrue(flag , msg = msg)

    def test_structures(self):
        """
        Test if only structures data exists in structures index
        """
        response_data = self.client.get(reverse('structures'))
        structures_list = response_data.context['structures_list']
        flag = True
        msg = "CORRECT DATA BEING SHOWN"
        for structure in structures_list:
            if structure["_index"] != 'structures':
                flag = False
                msg = "IRRELEVANT DATA ALSO BEING SHOWN"
        self.assertTrue(flag , msg = msg)

    def test_technologies(self):
        """
        Test if only technologies data exists in technologies index
        """
        response_data = self.client.get(reverse('technologies'))
        technologies_list = response_data.context['technologies_list']
        flag = True
        msg = "CORRECT DATA BEING SHOWN"
        for technology in technologies_list:
            if technology["_index"] != 'technologies':
                flag = False
                msg = "IRRELEVANT DATA ALSO BEING SHOWN"
        self.assertTrue(flag , msg = msg)
