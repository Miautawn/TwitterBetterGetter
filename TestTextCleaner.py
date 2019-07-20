import re


def filter_text(text):   #will clean the text off hashtags, emojys ect.
    clean_text = text
    for match in re.findall("\#|\@\w+|\W", text):
        if(match != " "):
            clean_text = clean_text.replace(match, " ")
    print(clean_text)
    return clean_text

uniltered_text = "There 123*12 is no cookie-cutter approach to using #AI/#ML to bolster your security infrastructure. You are fine as long as 1 of the goals of your #security posture is to derisk the possibilities of a potential #CyberAttack, #Databreach & #vulnerability.  "

filtered_text = filter_text(uniltered_text)