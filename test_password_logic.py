
from password_logic import check_password, generate_secure_password


def test_empty_password():
    assert check_password("")[0] == 0


def test_common_password():
    assert check_password("password")[1] == "VERY WEAK"


def test_common_password_with_suffix():
    assert check_password("Password123!")[1] == "VERY WEAK"


def test_leetspeak_password():
    assert check_password("P@ssw0rd!")[1] == "VERY WEAK"


def test_strong_password():
    assert check_password("k8#Vq2!mZx9$Lp4T")[1] == "VERY STRONG"


def test_repeated_characters():
    assert check_password("Abcdefg1!xxx")[0] < check_password("Abcdefg1!xyz")[0]


def test_generated_password_length():
    password = generate_secure_password(16)
    assert len(password) == 16


def test_generated_password_has_all_character_types():
    password = generate_secure_password(16)

    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(not c.isalnum() for c in password)


def test_invalid_length():
    try:
        generate_secure_password(4)
        assert False
    except ValueError:
        assert True
