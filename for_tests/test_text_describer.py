from third import *


def test_TextDescriber():
    text_describer = TextDescriber("Somebody write code!")
    assert text_describer.tokens == ['Somebody', 'write', 'code!']
    assert text_describer.word_count == 3
    assert text_describer.vocab == {'Somebody', 'write', 'code!'}
