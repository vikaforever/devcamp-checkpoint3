#!/usr/bin/python3

test_sentence = "Hello, World!"
test_number = 4
test_list = ["one", "two", "three"]
test_boolean = True

test_sentence_grab = test_sentence[:3]
test_list_grab_first = test_list[0]
test_number_add = test_number + 10
test_list_grab_last = test_list[-1]

names = "harry,alex,susie,jared,gail,conner"
names_list = names.split(",")

test_sentence_first = test_sentence[:5].upper()
test_sentence_new = test_sentence_first + test_sentence[5:]


print(f'test f-string {test_number}')

print(test_sentence)

test_sentence_replace = test_sentence.replace("Hello", "Good bye")
print(test_sentence_replace)