import pytest

from lesson_4.StringUtils import StringUtils

# создаем экземпляр класса
utils = StringUtils.StringUtils()

def test_capitilize():
    # позитив тест
    assert  utils.capitilize("skypro") == "Skypro"
    assert  utils.capitilize("Skypro") == "Skypro"

    # негатив тест
    assert  utilis.capitlize("") == "" # пустая строка
    assert  utils.capitilize(" ") == " " # пробел

def test_trim():
    # позитив тест
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("skypro   ") == "skypro"
    # негатив тест
    assert utils.trim("") == "" # пустая строка
    assert utils.trim(" ") == "" # только пробел

def test_to_list():
    # позитив тест
    assert utils.to_list("a,b,c") == ["a","b","c"]
    assert utils.to_list("1:2:3", ":") == ["1", "2", "3"]
    # негатив тест
    assert utils.to_list("") == [] # пустая строка
    assert utils.to_list(" ", ",") == [" "]  # пробел в строке
     # негативные
    assert  utils.to_list("") == [] # пустая строка
    assert  utils.to_list(" ",",") == [""] # пробел в строке
    assert  utils.to_list("a,,c",",") == ["a","","c"] # пустое значение

def contains():
     # позитв тест
     assert  utils.contains ("SkyPro", "S") is True

     # негатив тест
     assert  utils.contains("SkyPro", "U") is False





    

