# key value pair

conv_factor = {}

conv_factor['dollar'] = 83.5
conv_factor['euro'] = 90 # create
print(conv_factor)

print(conv_factor['euro'])
print(conv_factor.keys())
print(conv_factor.values())
print(conv_factor.items())

conv_factor['euro'] = 100 # update

conv_factor['yen'] = 0.55
print(conv_factor)

del conv_factor['yen']; # deleted the key-value
print(conv_factor)