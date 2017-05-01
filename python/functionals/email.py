'''
Validating Email Addresses With a Filter

Sample Input

3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

Sample Output

['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
'''

import string

def fun(s):
    alphanum = set(string.ascii_letters + string.digits)

    try:
        username, domain = s.split('@')
        website, extension = domain.split('.')

    except ValueError:
        return False

    if not len(username) or not len(website) or not len(extension) or len(extension) > 3:
        return False

    for c in username:
        if not (c in alphanum or c == '-' or c == '_'):
            return False

    for c in website:
        if c not in alphanum:
            return False

    return True
