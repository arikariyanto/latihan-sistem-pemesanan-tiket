
users = {
    "admin": {"password": "123", "role": "admin"},
    "user": {"password": "123", "role": "user"}
}

def login():
    print("="*40)
    print("          LOGIN SISTEM BIOSKOP         ")
    print("="*40)

    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    if username in users and users[username]["password"] == password:
        print(f"✅ Login berhasil sebagai {users[username]['role'].upper()}")
        return users[username]["role"]
    else:
        print("❌ Username atau password salah!")
        return None
