from django.test import TestCase
from .models import Minter
from .models import Ark

# Create your tests here.
class MinterModelTest(TestCase):
    def test_ark_exists(self): 
        minter = Minter(name='test_ark_exists', prefix='1234', template='eeddeeddk')
        minter.save()
        pass

    def test_mint(self): 
        minter = Minter(name='test_mint', prefix='1234', template='eeddeeddk')
        minter.save()
        pass

class ArkTestCase(TestCase): 
    def test_bind(self):
        pass
		