def allowed_dating_age(may_age):
    girls_age = may_age/2 + 7
    return girls_age

subhos_limit = allowed_dating_age(25)
debos_limit = allowed_dating_age(29)

print("Subho can date girls", subhos_limit, "or older")
print("Debo can date girls", debos_limit, "or older")