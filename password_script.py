import hashlib
import re

HTML_FILE = "/Users/xavieruhrmacher/Documents/Senior Design Labs/Lab3/index.html"


def sha256_hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def update_html_hash(file_path, new_hash):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r'const\s+PASSWORD_HASH\s*=\s*"[^"]*";'
    replacement = f'const PASSWORD_HASH = "{new_hash}";'

    new_content, count = re.subn(pattern, replacement, content)

    if count == 0:
        print("⚠ No PASSWORD_HASH line was updated. Check formatting or regex.")
    else:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("✔ Hash updated successfully!")


if __name__ == "__main__":
    password = input("Enter new password: ").strip()
    hashed = sha256_hash(password)
    print("SHA-256 hash:", hashed)

    update_html_hash(HTML_FILE, hashed)
