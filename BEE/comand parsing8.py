# #part 1:-
# # basic intent and entinty :-
# text=input("User:").lower()
# word=text.split()#gives list
# if word[0]=="open":
#     intent="open_app"
#     app=word[1]
#     print(f"intent={intent}")
#     print(f"app={app}")


# #second session:-
# open_words=["open","launch","start","run"]
# search_words=["search","find","look"]

# word=input("user:").lower().split()

# if word[0] in open_words:
#     intent="open_app"
#     print(f"intent:{intent}")
#     print(f"app:{word[1]}")

# elif word[0] in search_words:
#     intent="search_something"
#     print(f"intent:{intent}")

# session 3:-

# class commandParser:
#     def parse(self,text):
#         word=text.lower().split()
#         if word[0] in ["open","run","start","launch"]:
#             return {"intent":"open_app","app":word[1],"confidence":1.0}
#         else:
#             return{
#                 "intent":"unknown",
#                 "text":text,
#                 "confidence":0.0
#             }


# result=commandParser()
# print(result.parse("open crome"))
# print(result.parse("buy me a coffice"))

#session 4:-
# ragex+parser:-
import re
text = input("User: ").lower()
words = text.split()
for word in words:
    if word in ["pay", "give", "transfer"]:
        amount = re.search(r"\d+", text)
        if amount:
            print({
                "intent": "payment",
                "amount": int(amount.group())
            })
# to find person name in the text:-
            person = re.search(r"to\s+(\w+)", text)


#ragex keys to use :-

# Purpose	Regex
# Number	\d+
# Word	    \w+
# Space	    \s+
# Time	    \d{1,2}:\d{2}
# Date	    \d{2}/\d{2}/\d{4}
# UPI	    \b[\w.-]+@[\w.-]+\b
# Email	    \b[\w.-]+@[\w.-]+\.\w+\b
# Appafteropen	open\s+(\w+)

# re.search() → Find the first match.
# re.findall() → Find all matches.
# re.sub() → Replace text.
# re.finditer()->give the iteration of the found text.
# \d+ → Numbers.
# \w+ → Words.
# \s+ → Spaces.
# () → Capture the part you want.
# group() → Retrieve the captured text.
# re.IGNORECASE → Ignore uppercase/lowercase.
# \ -> to escape metacharecters that holds some meaning in regex.

#for regex we use row stings thing so that python not handle thing like shortcut and all.(r"").


# | Symbol | Meaning                      | Example                     |
# | ------ | ---------------------------- | --------------------------- |
# | `.`    | Any character except newline | `a.c` → `abc`, `a9c`        |
# | `\d`   | One digit (0-9)              | `5`                         |
# | `\D`   | Not a digit                  | `A`, `@`, `b`               |
# | `\w`   | Letter, digit, `_`           | `abc123_`                   |
# | `\W`   | Not a word character         | `@`, `#`, `-`               |
# | `\s`   | Whitespace                   | Space, Tab, Newline         |
# | `\S`   | Not whitespace               | `a`, `5`, `@`               |
# | `\b`   | Word boundary                | Matches start/end of a word |
# | `\B`   | Not a word boundary          | Inside a word               |
# | `^`    | Start of string              | `^hello`                    |
# | `$`    | End of string                | `world$`                    |


# | Pattern        | Meaning                | Example       |
# | -------------- | ---------------------- | ------------- |
# | `[abc]`        | a **or** b **or** c    | `a`, `b`, `c` |
# | `[^abc]`       | Anything except a,b,c  | `d`, `5`, `@` |
# | `[a-z]`        | Lowercase letters      | `m`           |
# | `[A-Z]`        | Uppercase letters      | `M`           |
# | `[0-9]`        | Digits                 | `7`           |
# | `[a-zA-Z]`     | Any letter             | `A`, `z`      |
# | `[a-zA-Z0-9]`  | Letter or digit        | `A`, `8`, `x` |
# | `[a-zA-Z0-9_]` | Word characters (`\w`) | `abc_123`     |


# | Pattern | Meaning                | Example             |
# | ------- | ---------------------- | ------------------- |
# | `+`     | One or more            | `\d+` → `5`, `5000` |
# | `*`     | Zero or more           | `a*`                |
# | `?`     | Zero or one (optional) | `colou?r`           |
# | `{3}`   | Exactly 3              | `\d{3}`             |
# | `{2,5}` | Between 2 and 5        | `\d{2,5}`           |
# | `{2,}`  | At least 2             | `\d{2,}`            |

#indise the charesteset ^ tells that does not have this r"[^a-zA-Z]" means that dont have latter a to z and A to Z.