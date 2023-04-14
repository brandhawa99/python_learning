# Create a Madlibs game


def getValue(type):
    x = input(f"Enter a {type}: ")
    return x


def get_madlib_values():
    values_needed = [
        "A Job",
        "Noun",
        "Adjective",
        "Noun",
        "Verb",
        "Adjective",
        "Noun",
        "Verb",
        "Noun",
        "Verb",
    ]
    values = []
    for x in values_needed:
        values.append(getValue(x))
    return values


def generate_madlib(words_array):
    string = f"""Today a {words_array[0]} named {words_array[1]} came to our school to talk to us about her job. She said the most important skill you need to know to do her job is to be able to {words_array[2]} around (a) smart {words_array[3]}. She said it was easy for her to learn her job because she loved to {words_array[4]} when she was my age--and that helps a lot! If you're considering her profession, I hope you can be near (a) tall Tree. That's very important! If you get too distracted in that situation you won't be able to jump next to (a) pig!"""

    return string


def main():
    vals = get_madlib_values()
    print(vals)
    print(generate_madlib(vals))


main()
