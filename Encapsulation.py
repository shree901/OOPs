class InstagramAccount:
    def __init__(self, account_name, password):
        # Public variable
        self.account_name = account_name

        # Protected variable
        self._private_reels = []

        # Private variable
        self.__archived_reels = []

        # Private password
        self.__password = password

    # private reel
    def add_private_reel(self, reel_name):
        self._private_reels.append(reel_name)
        print(f"Private reel '{reel_name}' added.")

    # Display private reels
    def display_private_reels(self, is_follower):
        if is_follower:
            print("Private Reels:")
            for reel in self._private_reels:
                print("-", reel)
        else:
            print("Access Denied! Only followers can view private reels")

    # archived reel
    def add_archived_reel(self, reel_name):
        self.__archived_reels.append(reel_name)
        print(f"Archived reel '{reel_name}' added.")

    # Display archived reels
    def display_archived_reels(self, password):
        if password == self.__password:
            print("Archived Reels:")
            for reel in self.__archived_reels:
                print("-", reel)
        else:
            print("Access Denied! Only account holder can view archived reels")

    # Getter for archived reels
    def get_archived_reels(self, password):
        if password == self.__password:
            return self.__archived_reels
        else:
            return "Access Denied!"

    #Setter to update password
    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Password updated successfully!")
        else:
            print("Wrong password! Cannot update.")
#object
account = InstagramAccount("shreelakshmi_h", "insta123")

#private reels
account.add_private_reel("Friends Trip")
account.add_private_reel("Birthday Celebration")

#archived reels
account.add_archived_reel("Old Dance Reel")
account.add_archived_reel("College Memories")

print("\n--- Private Reels (Follower) ---")
account.display_private_reels(True)

print("\n--- Private Reels (Non-Follower) ---")
account.display_private_reels(False)

print("\n--- Archived Reels (Wrong Password) ---")
account.display_archived_reels("wrong123")

print("\n--- Archived Reels (Correct Password) ---")
account.display_archived_reels("insta123")

print("\n--- Update Password ---")
account.set_password("insta123", "newpass456")

print("\n--- Archived Reels After Password Change ---")
account.display_archived_reels("newpass456")
