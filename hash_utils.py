def generate_md5(input_string):
    import hashlib
    return hashlib.md5(input_string.encode()).hexdigest()

def generate_sha1(input_string):
    import hashlib
    return hashlib.sha1(input_string.encode()).hexdigest()

def generate_sha256(input_string):
    import hashlib
    return hashlib.sha256(input_string.encode()).hexdigest()

def generate_sha512(input_string):
    import hashlib
    return hashlib.sha512(input_string.encode()).hexdigest()