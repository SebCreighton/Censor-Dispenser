import re

# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


def censor_word(email, word):
    pattern = r"\b" + re.escape(word) + r"\b"
    return re.sub(pattern, "*" * len(word), email)


print(censor_word(email_one, "learning algorithms"))


def censor_list_or_phrases(email, word_list):
    email_update = email

    for word in word_list:
        email_update = censor_word(email_update, word)

    return email_update


proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her",
                     "herself"]

print(censor_list_or_phrases(email_two, proprietary_terms))


def censor_negative_words(email, list):
    email_split = email.split()
    pattern = re.compile("/[^a-zA-Z0-9'-]+/")
    email_split_cha = [pattern.sub('', cha) for cha in email_split]
    censor_list = []
    neg_count = 0
    for email_split_word in email_split_cha:
        if email_split_word in list and neg_count >= 1:
            censor_list.append(email_split_word)
            neg_count += 1

        elif email_split_word in list:
            neg_count += 1

    for word in list:
        if ' ' in word:
            censor_list.append(word)

    for word in censor_list:
        email = censor_word(email, word)

    return email


negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help",
                  "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                  "distressing", "concerning", "horrible", "horribly", "questionable"]

print(censor_negative_words(email_three, negative_words))


def censor_multi_list_words(email, lists):
    email_updated = censor_list_or_phrases(email, lists[1])
    email_updated = censor_negative_words(email_updated, lists[0])

    email_updated_find = re.findall("\*+[a-zA-Z'-]+", email_updated)
    index_list = []
    email_updated_split = email_updated.split()
    pattern = re.compile("/[^a-zA-Z0-9'-]+/")
    email_updated_split_cha = [pattern.sub('', cha) for cha in email_updated_split]
    for item in email_updated_find:
        index = email_updated_split_cha.index(item)
        index_list.append(index)

    email_split = email.split()
    email_split_cha = [pattern.sub('', cha) for cha in email_split]
    for index in index_list:
        email_updated = email_updated.replace(email_updated_split_cha[index], email_split_cha[index + 1])

    email_updated_censored = re.findall("\*+", email_updated)

    index_list_two = []
    index_list_two_deduct_one = []
    index_list_two_add_one = []
    email_updated_split_second = email_updated.split()

    for i in range(len(email_updated_split_second)):
        alphanumeric = ''
        for character in email_updated_split_second[i]:
            if character.isalnum() or character == "*":
                alphanumeric += character
        if alphanumeric == email_updated_censored[0] and len(email_updated_censored) > 1:
            index_list_two.append(i)
            email_updated_censored = email_updated_censored[1:]
        elif len(email_updated_censored) == 1:
            str_one_remain = ''.join(email_updated_censored)
            if alphanumeric == str_one_remain:
                index_list_two.append(i)
                email_updated_censored.clear()
                break

    for i in index_list_two:
        index_list_two_deduct_one.append(i - 1)
        index_list_two_add_one.append(i + 1)

    for i in index_list_two_deduct_one:
        email_updated = censor_word(email_updated, email_updated_split_second[i])

    for i in index_list_two_add_one:
        email_updated = censor_word(email_updated, email_updated_split_second[i])

    return email_updated


print(censor_multi_list_words(email_four, [negative_words, proprietary_terms]))
