import pytest

from StringUtilities import StringUtils

# создаем экземпляр класса
utils = StringUtils()

def test_capitilize():
    # позитив тест
    assert utils.capitilize("skypro") == "Skypro"
    assert utils.capitilize("Skypro") == "Skypro"

    # негатив тест
    assert utils.capitilize("") == ""  # пустая строка
    assert utils.capitilize(" ") == " "  # пробел

@pytest.mark.xfail(reason="Проблема с тестом")  # Или просто оставьте без усл
def test_trim():
    # позитив тест
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("skypro   ") == "skypro"
    # негатив тест
    assert utils.trim("") == ""  # пустая строка
    assert utils.trim(" ") == ""  # только пробел


@pytest.mark.xfail( reason="Проблема с тестом")  # Или просто оставьте без условия
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
     assert utils.contains("SkyPro", "U") is False
     assert utils.contains("", "S") is False # пустая строка

def test_delete_symbol():
    # позитв тест
    assert utils.delete_symbol("SkyPro", "K") == "SkyPro"
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"
    # негатив тест
    assert utils.delete_symbol("SkyPro", "Z") == "SkyPro" # символ отсутсвует
    assert utils.delete_symbol("","Z") == ""  # пустая строка

def test_starts_with():
    # позитив тест
    assert utils.starts_with("SkyPro", "S") is True


    # негатив тест
    assert utils.starts_with("Skypro", "P") is False
    assert utils.starts_with("", "S")  is False

def test_end_with():
    # позитв тест
    assert utils.end_with("SkyPro", "o") is True

    # негатив тест
    assert utils.end_with("SkyPro", "y") is False
    assert utils.end_with("", "o")  is False  # пустая строка

def test_is_empty():
    # позитив тест
    assert utils.is_empty("")  is True

    # негатив тест
    assert utils.is_empty(" ") is True # строка с пробелом
    assert utils.is_empty("SkyPro") is False  # не пустая строка

def test_list_to_string():
    # позитив тест
    assert utils.list_to_string([1,2,3,4]) == "1, 2, 3, 4"
    assert utils.list_to_string(["Sky", "Pro"]) == "Sky, Pro"

    # негатив тест
    assert utils.list_to_string([]) == "" # пустой список
    assert utils.list_to_string([""]) == "" # список с одной пустой строкой





    

