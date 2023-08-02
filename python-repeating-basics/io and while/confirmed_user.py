unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    confirmed_user = unconfirmed_users.pop()

    print("Verifying user:" + confirmed_user.title())
    confirmed_users.append(confirmed_user)

print("\nThe following users have been confirmed:")
for user  in confirmed_users:
    print(user.title())
