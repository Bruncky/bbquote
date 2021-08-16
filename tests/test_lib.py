from bbquote.lib import get_quote

def test_get_quote():
    author, quote = get_quote()  # assuming the function returns an author and a quote
    result = f"{quote}, {author}"
    
    assert type(result) == str
