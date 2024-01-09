import hashlib


def calculate_sha256(api_key, env_id, user_id):
    # Concatenate the decrypted API key, env_id, and user_id
    data_to_hash = f"{api_key}|{env_id}|{user_id}"
    # Calculate the SHA256 hash
    sha256_hash = hashlib.sha256(str(data_to_hash).lower().encode()).hexdigest()
 
    return sha256_hash