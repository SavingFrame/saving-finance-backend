from babel.numbers import get_currency_symbol as _get_currency_symbol

COMMON_CURRENCY_SYMBOLS: dict[str, str] = {
    'USD': '$',
    'EUR': '€',
    'UAH': '₴',
}


def get_currency_symbol(currency_code: str) -> str:
    return COMMON_CURRENCY_SYMBOLS.get(currency_code, _get_currency_symbol(currency_code, ))
