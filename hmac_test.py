import hmac

print(hmac.new("key", "msg").hexdigest())
