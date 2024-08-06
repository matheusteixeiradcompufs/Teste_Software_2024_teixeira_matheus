import unittest


# Exceção personalizada
class PathIsNotAValidOne(Exception):
    pass


# Função que sempre retorna um caminho inválido
def AlwaysSuppliesAnInvalidPath():
    return "/invalid/path"


# Função que sempre retorna um caminho válido
def AlwaysSuppliesAValidPath():
    return "/valid/path"


# Classe que estamos testando
class MyObject:
    def __init__(self, path):
        if path == "/invalid/path":
            raise PathIsNotAValidOne("The provided path is not valid.")


# Classe de teste
class MyObjectTestCase(unittest.TestCase):
    def test_invalid_path_raises_exception(self):
        sInvalidPath = AlwaysSuppliesAnInvalidPath()
        self.assertRaises(PathIsNotAValidOne, MyObject, sInvalidPath)

    def test_valid_path_does_not_raise_exception(self):
        sValidPath = AlwaysSuppliesAValidPath()
        try:
            MyObject(sValidPath)
        except PathIsNotAValidOne:
            self.fail("PathIsNotAValidOne exception raised with a valid path")



