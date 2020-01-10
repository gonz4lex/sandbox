from random import choice, randint

## Beat poetry

adjectives = "shining radiant bright ecstatic young lithe driving running splitting disarming".split(
)
verbs = "wriggles grows stares saunters drives smiles raps defies sleeps ponders".split()
nouns = "moon pen inkwell willow sky station train pane window sunlight dust warrior".split(
)


def beat_poem():
    print("\n" + "=" * 16 + " a poem " + "=" * 16)
    print()
    for x in range(randint(5, 11)):
        words1 = " ".join([choice(adjectives) + ", ", choice(adjectives)])
        words2 = " ".join([choice(nouns), choice(verbs)])
        words3 = " ".join(
            [choice(nouns),
             choice(nouns),
             choice(adjectives),
             choice(nouns)])

        for i in range(randint(2, 5)):
            words = choice([words1, words2, words3])
            line = " " * randint(0, 40 - len(words)) + words
            print(line)

        if x % 3 == 0:
            print()
            print(" " * 5 + choice(nouns))
            print(" " * 5 + choice(nouns))
            print(" " * 5 + "the " + choice(nouns) + "!")
            print()

        if x % 7 == 0:
            words4 = " ".join(
                ["the " + choice(adjectives),
                 choice(nouns),
                 choice(verbs)])
            print()
            print(" ".join(words4))
            print()


beat_poem()
