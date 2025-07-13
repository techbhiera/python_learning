pass_key =input( "write down your pass with alphanumeric ")
pass_strength = len(pass_key)

if pass_strength < 6 :
    strength = "weak"
elif 6<=pass_strength<=10:
    strength = "medium"
else:
    strength="strong"
print(strength)