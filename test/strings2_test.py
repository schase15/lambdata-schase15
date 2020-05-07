# Doing pytest instead of unit test

# we are using something specific inside the pytest package so we need to import it
import pytest

def test_upper():
    # self.assertEqual('foo'.upper(), 'FOO')
    assert 'foo'.upper() == 'FOO'

def test_isupper():
    # self.assertTrue('FOO'.isupper())
    # self.assertFalse('Foo'.isupper())
    assert 'FOO'.isupper()
    assert 'Foo'.isupper() == False
def test_split():
    s = 'hello world'
    # self.assertEqual(s.split(), ['hello', 'world'])
    assert s.split() == ['hello', 'world']
    
    # check that s.split fails when the separator is not a string
    with pytest.raises(TypeError):
        s.split(2)
