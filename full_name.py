first_name = "ada"
last_name = 'lovelace'

full_name = f"{first_name} {last_name}"

print(full_name)
print("python")
# add a tab
print("\tpython")
# new line
print("languages:\nruby\njavascript\ntypescript\npython")
favorite_language = '   python    '
# remove whitespace to the right side
print(favorite_language.rstrip())
# renove whitespace to the left side
print(favorite_language.lstrip())
# remove wihtespace - both sides
print(favorite_language)
print(favorite_language.strip())

nostarch_url = "https://nostarch.com"
print(nostarch_url.removeprefix("https://"))

notes = "python_notes.txt"
print(notes.removesuffix(".txt"))