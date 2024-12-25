def validate_intent_payload(payload: dict) -> bool:

    required_keys_map = {

        "Combination metrics": ["buyer_name", "target_name"],
        "Target identification": ["buyer_name", "acquisition_strategy", "target_size", "geography"],
        "Target characteristics": ["target_name"],
        "Precedent synergies for a combination": ["buyer_name", "target_name"],
        "Detail for specific precedents": ["precedent_transaction_buyer", "precedent_transaction_target"]

    }

    intent = payload.get("Intent")

    if not intent:
        print("Validation failed: 'Intent' key is missing in the payload.")
        return False

    if intent not in required_keys_map:
        print(f"Validation failed: Intent '{intent}' is not recognized.")
        return False

    required_keys = required_keys_map[intent]

    missing_keys = [key for key in required_keys if key not in payload]
    if missing_keys:
        print(f"Validation failed: Missing required keys {missing_keys} for intent '{intent}'.")
        return False

    print(f"Validation successful for intent '{intent}' with payload {payload}.")
    return True

payload = {
    "Intent": "Combination metrics",
    "Buyer name": "Company A",
    "Target name": "Company B"
}

is_valid = validate_intent_payload(payload)
print(is_valid)