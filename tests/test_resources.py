import os
from yaml import load
from yaml import Loader

def test_validate_yaml_data():
    # Given
    with open(os.path.join(os.getcwd(), "resources/raw_data.yaml")) as f:
        data = load(f, Loader)
    
    # Then
    assert isinstance(data["version"], int)
    assert isinstance(data["last_updated"], str)
    categories = data["catagories"]
    assert isinstance(categories, dict)
    assert len(categories) >= 1

    for key in categories:
        assert isinstance(key, str)
        for value in categories[key]:
            assert isinstance(value, str)