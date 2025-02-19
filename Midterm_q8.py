def is_valid_url(url):
    """
    Checks if a given string is a valid URL.
    :param url: The string to check
    :return: True if valid, False otherwise
    """
    # Check if URL starts with "http://" or "https://"
    if not (url.startswith("http://") or url.startswith("https://")):
        return False  # Invalid if it does not start correctly
    # Check if URL contains at least one "."
    if "." not in url:
        return False  # Invalid if no dot is found
    # Check if URL contains spaces (not allowed in URLs)
    if " " in url:
        return False  # Invalid if it contains spaces
    # If all checks passed, return True
    return True

print(is_valid_url("https://github.com/Paulina-Torres-H-Mendez/PythonProject11"))#TRUE
print(is_valid_url("httpssssss://github.co.  m/Paulina-Torres-H-Mendez/PythonProject11"))#FALSE
print(is_valid_url("m/Paulina-Torres-H-Mendez/PythonProject11"))#FALSE