from main import add
from main import multiply

def test_add():
    result = add(4,2)
    assert result == 6
    print("success the add numbers")

def test_multiply():
    result = multiply(4,2)
    assert result == 8
    print("success the multiply numbers")



if __name__ == "__main__" :
    test_add()
    test_multiply()
      

