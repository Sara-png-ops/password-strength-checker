
import pytest

from password_logic import check_password, generate_secure_password


def test_empty_password():
    assert check_password("")[1] == "EMPTY"


def test_common_password():
    assert check_password("password")[1] == "VERY WEAK"


def test_common_password_with_suffix():
    assert check_password("Password123!")[1] == "VERY WEAK"


def test_leetspeak_password():
    assert check_password("P@ssw0rd!")[1] == "VERY WEAK"


def test_strong_password():
    assert check_password("k8#Vq2!mZx9$Lp4T")[1] == "VERY STRONG"


def test_repeated_characters():
    assert check_password("AAAAaaaa1111!!!!")[1] != "VERY STRONG"


def test_generated_password_length():
    assert len(generate_secure_password(16)) == 16


def test_generated_password_has_all_character_types():
    password = generate_secure_password(16)

    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(not c.isalnum() for c in password)


def test_invalid_length():
    with pytest.raises(ValueError):
        generate_secure_password(5)
