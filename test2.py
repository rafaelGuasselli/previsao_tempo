from model.user_repository import UserRepository

repo = UserRepository()
user = repo.getUser("rafael")
print(user)

print(repo.login("rafael", "12345"))