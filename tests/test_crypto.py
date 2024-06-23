from remindme import crypto
from tests.given import Given
from cryptography.fernet import InvalidToken
import pytest

def test_encrypt_decrypt_cycle_maintains_data(given: Given):
    # Given
    password = given.password()
    initial_data = "some Random\n multi line \n\t string with spaces and stuff 💛"

    # When
    encrypted_data = crypto.encrypt(data=initial_data.encode(), password=password)
    result = crypto.decrypt(data=encrypted_data, password=password)

    # Then
    assert str(result, "utf-8") == initial_data

def test_decrypt_with_wrong_password_throws_error_and_logs_message(given: Given, capfd):
    # Given
    initial_data = "some Random\n multi line \n\t string with spaces and stuff 💛"
    encrypted_data = crypto.encrypt(data=initial_data.encode(), password="password1")

    # When
    with pytest.raises(InvalidToken):
        crypto.decrypt(data=encrypted_data, password="a different password")

    # Then
    captured = capfd.readouterr()

    assert "Failed to decrypt love" in captured.out
