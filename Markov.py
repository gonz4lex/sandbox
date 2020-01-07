
# * Dictogram-based Markov model generator.
# * Adapted from https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71.


# TODO: LSTMs and Monte Carlo simulation



import random

class MarkovDict(dict):
    def __init__(self, iterable=None):
        super(MarkovDict, self).__init__()
        self.types = 0
        self.tokens = 0
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        for item in iterable:
            if item in self:
                self[item] += 1
                self.tokens += 1
            else:
                self[item] = 1
                self.types += 1
                self.tokens += 1

    def count(self, item):
        if item in self:
            return self[item]
        return 0

    def get_random_word(self):
        random_key = random.sample(self, 1)
        return random_key[0]

    def get_weighted_set(self):
        random_int = random.randint(0, self.tokens - 1)
        index = 0
        key_list = list(self.keys())

        for i in range(0, self.types):
            index += self[key_list[i]]
            if index > random_int:
                return key_list[i]

    def make_model(self, data):
        model = dict()

        for i in range(0, len(data) - 1):
            if data[i] in model:
                model[data[i]].update([data[i+1]])
            else:
                model[data[i]] = MarkovDict([data[i+1]])
        
        return model

    def make_high_order_model(self, data, order):
        model = dict()

        for i in range(0, len(data) - order):
            window = tuple(data[i:i+order])
            if window in model:
                model[window].update([data[i+order]])
                print('Window IS in model')
                print([data[i+order]])
            else:
                model[window] = MarkovDict([data[i+order]])
                print('Window not in model')
                print([data[i+order]])

        return model

    def random_start(self, model):
        if 'END' in model:
            seed = 'END'
            while seed == 'END':
                seed = model['END'].get_weighted_set()
            return seed
        return random.choice(list(model.keys()))

    def random_set(self, length, model):
        current_item = self.random_start(model)
        itemset = [current_item]
        for i in range(0, length):
            current_dict = model[current_item]
            random_weighted_item = current_dict.get_weighted_set()
            current_item = random_weighted_item
            itemset.append(current_item)
        if all(itemset) is str:
            itemset[0] = itemset[0].capitalize()
        
        return ' '.join(itemset) + ' '
        return itemset

    def process_text(self, data: str):
        data = "START " + data + " END"
        data = data.split()

        return data


corpus = '''
I could tell how much I had changed by my grandfather’s visits. He came to Zurich only when he knew I was alone. The tension between him and Mother must have grown; for several years he avoided her, but they corresponded regularly. During the war, he received postcards telling him our new addresses; later, they exchanged formal and impersonal letters.
No sooner did he know that I was at the Yalta than he showed up in Zurich. He got a room at the Hotel Central and asked me to come by. His hotel rooms, whether in Vienna or Zurich, all looked alike, the same smell prevailed in all of them. He was wrapped up in his phylacteries, reciting the evening prayers, when I arrived; while kissing me and bathed in tears, he continued praying. He pointed to a drawer, which I was to open in his stead; inside lay a thick envelope of stamps, which he had gathered for me. I emptied the envelope on the lower bureau and examined them, some I had, some I didn’t have, he kept a watchful eye on the expressions of my face, which revealed delight or disappointment to him in rapid alternation. Unwilling to interrupt his prayer, I said nothing, he couldn’t stand it and interrupted the solemn tone of his Hebrew words himself with an interrogative: “Well?” I emitted a few inarticulate, enthusiastic sounds; that satisfied him, and he went on with his prayers. They took a fairly long time, everything was established, he skipped nothing and shortened nothing; since it proceeded at maximum speed anyhow, nothing could be accelerated. Then he was done, he tested me to see whether I knew the countries from which the stamps came, and he showered me with praise for every right answer. It was as if I were still in Vienna and only ten years old, I found it as bothersome as his tears of joy, which were flowing again. He wept as he spoke to me, he was overwhelmed at finding me still alive, his grandson and namesake, grown a bit more, and perhaps he was also overwhelmed at being still alive himself and being able to have this experience.
As soon as he was done testing me and had wept himself out, he took me to a non-alcoholic restaurant, where “restaurant daughters” waited on tables. He had an eager eye for them and it was impossible for him to order anything without a detailed conversation. He began by pointing to me and saying: “My little grandson.” Then he totted up all the languages he knew, there were still seventeen. The “restaurant daughter,” who had things to do, listened impatiently to the tally, which didn’t include Swiss German; as soon as she tried to get away, he put a propitiating hand on her hip and let it lie there. I was embarrassed for him, but the girl stood still; when he was done with his languages and I raised my bowed head again, his hand was still in the same place. He took it away only when he started ordering, he had to confer with the “restaurant daughter,” which required both hands; after a long procedure, he wound up ordering the same as always, a yogurt for himself and coffee for me. When the waitress was gone, I tried talking to him: I said this wasn’t Vienna, Switzerland was different, he couldn’t act like that, some day a waitress might slap him. He didn’t answer, he felt he knew better. When the waitress returned with yogurt and coffee, she gave him a friendly smile, he thanked her emphatically, put his hand on her hip again, and promised to stop by on his next visit to Zurich. I wolfed down my coffee just to get away as fast as possible, convinced, all appearances notwithstanding, that he had insulted her.
I was incautious enough to tell him about the Yalta, he insisted on visiting me there and announced his coming. Fräulein Mina wasn’t at home, Fräulein Rosy received him. She took him through the house and the garden, he was interested in everything and asked countless questions. At every fruit tree, he asked how much it yielded. He asked about the girls who lived here, their names, backgrounds, and ages. He counted them up, there were nine, and he said that more could be put up in the house. Fräulein Rosy said that almost each one had her own room, and now he wanted to see the rooms. She, carried away by his cheeriness and his questions, innocently took him into each room. The girls were in town or in the hall, Fräulein Rosy saw nothing wrong with showing him the empty bedrooms, which I had never seen. He admired the view and tested the beds. He estimated the size of each room and felt that a second bed could easily be added. He had retained the countries of the girls and he wanted to know where the French girl, the Dutch girl, the Brazilian girl, and especially the two Swedish girls slept. Finally he asked about the sparrow’s nest, Fräulein Mina’s studio. I had forewarned him that he would have to look at the paintings very carefully and praise some of them. He did that in his way: like a connoisseur, he first halted at some distance from a picture, then approached it and attentively studied the brush strokes. He shook his head at so much expertise and then broke into enthusiastic superlatives, while having enough cunning to use Italian words, which Fräulein Rosy understood, instead of Ladino words. He knew some of the flowers from his garden at home, tulips, carnations, and roses, and he asked Fräulein Rosy to convey his congratulations to the painter on her expertise: he had never seen anything like it before, he said, which was true, and he asked whether she also painted fruit trees and fruit. He regretted that none were to be seen and he ardently recommended an expansion of her repertoire. He thus stunned both of us, neither Fräulein Rosy nor I had ever thought of it. When he began asking about the cost of the paintings, I glared at him, but futilely. He stuck to his guns, Fräulein Rosy drew out a list from the last exhibition and informed him of the prices. There were a few that had been sold for several hundred francs, smaller ones were less, he had her give him all the prices in a row, instantly added them up in his head, and surprised us with the handsome sum, which neither of us had known. Then he grandly threw in that it didn’t matter, the important thing was the beauty, la hermosura, of the paintings, and when Fräulein Rosy shook her head because she didn’t understand the word, he swiftly interrupted me before I could translate it and he said in Italian: “La bellezza, la bellezza, la bellezza!“.
Then he wanted to see the garden again, this time more thoroughly. In the tennis court, he asked how large the grounds belonging to the house were. Fräulein Rosy was embarrassed, for she didn’t know; he was already measuring the tennis court with his paces, the length and the width, he had already computed the number of square meters, blurted it out, and: reflected a bit. He compared the size of the tennis court with the size of the garden and also with the size of the adjacent meadow, made a shrewd face, and told us how big the lot was. Fräulein Rosy was overwhelmed, the visit, which I had so feared, was a triumph. For the early evening, he took me to a performance in the Waldtheater over the Dolder. When I came home, the ladies were waiting for me in their room. Fräulein Mima couldn’t forgive herself for being away, for an hour I heard them sing Grandfather’s praises. He had even figured out the size of the grounds correctly, a true sorcerer.
'''

txt = """
This hall is choked with corpses. The bodies of orcs and ogres lie in tangled heaps where they died, and the floor is sticky with dried blood. It looks like the orcs and ogres were fighting. Some side was the victor but you're not sure which one. The bodies are largely stripped of valuables, but a few broken weapons jut from the slain or lie discarded on the floor.
A cluster of low crates surrounds a barrel in the center of this chamber. Atop the barrel lies a stack of copper coins and two stacks of cards, one face up. Meanwhile, atop each crate rests a fan of five face-down playing cards. A thin layer of dust covers everything. Clearly someone meant to return to their game of cards.
Neither light nor darkvision can penetrate the gloom in this chamber. An unnatural shade fills it, and the room's farthest reaches are barely visible. Near the room's center, you can just barely perceive a lump about the size of a human lying on the floor. (It might be a dead body, a pile of rags, or a sleeping monster that can take advantage of the room's darkness.)
You round the corner to see a ghastly scene. A semitranslucent figure hangs in the air, studded with crossbow bolts and with blood pouring from every wound. It reaches toward you in a pleading gesture, points to the walls on either side of the room, and then vanishes. Once it has gone, you notice small holes in the walls, each just large enough for a bolt to pass through.
"""

import requests as rq
from bs4 import BeautifulSoup

url = 'https://www.thievesguild.cc/generators/dungeon-room-generator'

descriptions = []

for i in range(5):
    page = rq.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    div = soup.find('div',{"class": "box"})
    text = div.text.strip()
    # remove dm notes
    text = text.split(" DM Note:", 1)[0]
    print(text)
    descriptions.append(text)

def main():

    mk = MarkovDict()

    gen = mk.random_set(140,
            mk.make_model(
                mk.process_text(txt)
            )

        )

    print(gen)

# mk.random_set(140,
#     mk.make_high_order_model(
#         mk.process_text(txt),
#         3
#     )
# )

if __name__ == "__main__":
    main()