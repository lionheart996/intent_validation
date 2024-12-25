import pytest
from intent_validation import validate_intent_payload

@pytest.mark.parametrize("payload,expected", [

    ({"Intent": "Combination metrics", "buyer_name": "Company A", "target_name": "Company B"},
     True),

    ({"buyer_name": "Company A", "target_name": "Company B"},
     False),

    ({"Intent": "Unknown intent", "buyer_name": "Company A", "target_name": "Company B"},
     False),

    ({"Intent": "Combination metrics", "buyer_name": "Company A"},
     False),

    ({"Intent": "Combination metrics", "buyer_name": "Company A", "target_name": "Company B", "extra_key": "value"},
     True)
])
def test_validate_intent_payload(payload, expected):
    assert validate_intent_payload(payload) == expected