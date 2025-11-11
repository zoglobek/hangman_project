import random

word_list = [
"whistle", "crimson", "jungle", "orbit", "flavor", "tumble", "glimmer", "hazard", "quiver", "sizzle",
"plasma", "ripple", "snatch", "velvet", "twinkle", "gadget", "mystic", "puzzle", "flicker", "breeze",
"clover", "sparkle", "echo", "drizzle", "fumble", "glitch", "hollow", "juggle", "knuckle", "latch",
"mumble", "nuzzle", "opaque", "paddle", "quartz", "rubble", "scoff", "trickle", "umpire", "vortex",
"waddle", "yonder", "zephyr", "amber", "blizzard", "cascade", "doodle", "ember", "flick", "gobble",
"hurdle", "ignite", "jigsaw", "kettle", "lunar", "mosaic", "nibble", "ooze", "plunge", "quack",
"riddle", "swoosh", "throttle", "unravel", "vanish", "whisk", "yelp", "zipper", "alchemy", "bramble",
"crackle", "dazzle", "entwine", "fizz", "grumble", "hatch", "inkling", "jolt", "knot", "lurk",
"mirth", "nudge", "obscure", "pounce", "quirk", "rustle", "slither", "tangle", "uplift", "vivid"
]


def word_of_game():
    word_num = random.randrange(90)
    chosen_word = word_list[word_num]
    gamedata = {
            "chosen_number": word_num,
            "picked_word": chosen_word}
    return gamedata


def dotted_line(word):
    dot = len(word)
    print(dot * "_")




word_and_place = word_of_game()
guessing_line = dotted_line(word_and_place.get("picked_word"))