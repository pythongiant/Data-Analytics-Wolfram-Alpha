import wolframalpha

client = wolframalpha.Client('5L4TR5-3QRQ88JWA3')
userIn=input("What do you want to find out:")
print(' ')
res = client.query(userIn)
for pod in res.pods:
    for sub in pod.subpods:
		print(sub.plaintext)