class PasswordVault:
    def __init__(self, username, password):
        self.username = username
        self._vault_status = "Active"
        self.__password = password

    def verify_password(self, password):
        if password == self.__password:
            print("Access Granted")
        else:
            print("Access Denied")

    def change_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password Changed Successfully")
        else:
            print("Incorrect Old Password")

    def display_status(self):
        print("Username:", self.username)
        print("Vault Status:", self._vault_status)


user = PasswordVault("Ali", "abc123")

user.display_status()
user.verify_password("abc123")
user.change_password("abc123", "newpass")
user.verify_password("newpass")
