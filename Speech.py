

def leet(data):
    swaps = {
        'i': '1',
        'l': '1',
        'z': '2',
        'e': '3',
        'a': '4',
        's': '5',
        'g': '6',
        't': '7',
        '8': '8',
        '9': '9',
        'o': '0',
    }

    result = ""

    for letter in data.lower():
        if letter in swaps.keys():
            letter = swaps[letter]

        result += letter

    return result



def spritz(text, WPM = 140):
    import time

    start = time.time()

    for word in text.split():
        print(word)
        time.sleep(60 / WPM)

    end = time.time()

    ex_time = end - start
    print(f"{len(text.split())} words read at {WPM} WPM.")
    print(f"Time elapsed: {ex_time}")
    print(f"True WPM: {len(text.split()) / (ex_time / 60)}")


TEXT = """
Lorem ipsum dolor amet biodiesel pok pok cronut, pug portland mixtape you probably haven't heard of them drinking vinegar.
Selfies franzen ad, mlkshk biodiesel ramps flannel pour-over. Knausgaard sustainable iceland, dreamcatcher fingerstache freegan hexagon everyday carry art party normcore cornhole neutra.
Heirloom tattooed kickstarter shaman umami.
Lyft gentrify tilde bicycle rights vaporware tumeric enamel pin everyday carry.
Elit pitchfork nulla pickled raclette excepteur kale chips listicle. Taiyaki laborum meditation, shaman pickled aliqua flannel sint.
Farm-to-table irure YOLO ad sunt. Disrupt put a bird on it synth snackwave salvia chambray, yr aute ramps vexillologist.
Crucifix biodiesel polaroid chicharrones in occupy jianbing enamel pin tattooed meditation banjo street art unicorn veniam portland.
Flexitarian eu ex banh mi chillwave marfa wolf echo park austin messenger bag cold-pressed qui chartreuse umami.
Kickstarter marfa quis lyft, etsy jean shorts truffaut typewriter you probably haven't heard of.
"""

spritz(leet(TEXT))