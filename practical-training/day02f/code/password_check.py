def check_password(pwd):
    if len(pwd) < 8:
        return "密码长度至少为8位"

    has_upper = False
    has_lower = False
    has_digit = False

    for char in pwd:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    if not has_upper:
        return "密码缺少: 大写字母"
    if not has_lower:
        return "密码缺少: 小写字母"
    if not has_digit:
        return "密码缺少: 数字"

    return True

print("Abc12345 :", check_password("Abc12345"))      # True
print("abc12345 :", check_password("abc12345"))      # 密码缺少: 大写字母
print("ABC12345 :", check_password("ABC12345"))      # 密码缺少: 小写字母
print("Abcdefgh :", check_password("Abcdefgh"))      # 密码缺少: 数字
print("Ab1      :", check_password("Ab1"))           # 密码长度至少为8位
print("hello    :", check_password("hello"))         # 密码长度至少为8位
print("HelloWorld:", check_password("HelloWorld"))   # 密码缺少: 数字
