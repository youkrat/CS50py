from hello2 import hello

def test_argument():
    assert hello("David") == "hello, David"
    
def test_default():
    assert hello()=="hello, World"