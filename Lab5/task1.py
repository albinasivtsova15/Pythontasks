import re

def is_domain(url):
    pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    return bool(re.match(pattern, url))

def get_domain(url):
    if not is_domain(url):
        raise ValueError("Некорректный URL")
    domain = re.search(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', url).group(0)
    return domain

n=input()
print(is_domain(n))  # True


try:
    print(get_domain(n))

except ValueError as e:
    print(e)
