def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}


def parse_cookie(cookie: str) -> dict:
    items = cookie.split(";")
    cookie_dict = {}
    for item in items:
        if '=' not in item and item != '':
            cookie_dict[item] = ''
            continue
        split_item = item.strip().split("=", 1)
        if len(split_item) == 2:
            key, value = split_item
            cookie_dict[key] = value
    return cookie_dict


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie(';name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('name=Dima;age=28;;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;secure') == {'name': 'Dima=User', 'age': '28', 'secure': ''}
    assert parse_cookie('name=Dima=User;age=28;secure=true') == {'name': 'Dima=User', 'age': '28', 'secure': 'true'}
    assert parse_cookie(';name=Dima=User;age=28;secure=true;') == {'name': 'Dima=User', 'age': '28', 'secure': 'true'}
    assert parse_cookie('name=Dima;age="28"') == {'name': 'Dima', 'age': '"28"'}
    assert parse_cookie('name=Dima;age="28";secure=true') == {'name': 'Dima', 'age': '"28"', 'secure': 'true'}
    assert parse_cookie('name=Dima;age="28;secure=true"') == {'name': 'Dima', 'age': '"28', 'secure': 'true"'}
    assert parse_cookie('name=Dima=User;age=28;secure=true;reg=Ttrue;') == {'name': 'Dima=User', 'age': '28', 'secure': 'true', 'reg': 'Ttrue'}
    assert parse_cookie('name=Dima;age=28;secure=;true') == {'name': 'Dima', 'age': '28', 'secure': '', 'true': ''}
    assert parse_cookie('name;Dima;age;28;') == {'name': '', 'Dima': '', 'age': '', '28': ''}
    assert parse_cookie('name=Dima=age=28;') == {'name': 'Dima=age=28'}
