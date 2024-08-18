# hashtag

user_string = input("Enter your text without punctuation: ")
user_string = user_string.title()
user_string = user_string.replace(' ', '')
user_string = ''.join([c for c in user_string if c.isalnum()])
if len(user_string) <= 140:
    hashtag = "#{}"
    print(hashtag.format(user_string))
elif len(user_string) > 140:
    hashtag = "#{}"
    print(hashtag.format(user_string)[: 141])
