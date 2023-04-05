# Hero story

story_1 = {
"start": "Once upon a time, there was a boy named Jack who lived in a small village. Jack was fascinated by the stories of ancient heroes who roamed the lands, fighting monsters and saving people from danger. One day, while exploring the nearby forest, he stumbled upon an old map that revealed the location of a hidden treasure. Jack saw this as an opportunity to become a hero himself and set off on a quest to find the treasure.",
"middle": "However, he soon discovered that the treasure was guarded by a fierce dragon. Summoning all his courage, Jack engaged in a fierce battle with the dragon. In the end, Jack emerged victorious, not only gaining the treasure but also earning the respect and admiration of his fellow villagers. Jack's journey had transformed him into a true hero, one who inspired others to be brave and kind-hearted in the face of adversity.",
"end": "From that day on, Jack became known as a hero in his village and beyond. He used his newfound wealth to help those in need and became a mentor to other young adventurers seeking to follow in his footsteps. Jack's journey had not only helped him fulfill his dream of becoming a hero but had also taught him important lessons about life and inspired others to follow in his footsteps."
}

print(story_1)
print((type(story_1)))
print(story_1.keys())
print(story_1.values())

print(story_1["start"])
print(story_1["middle"])
print(story_1["end"])

story_1.update({
"hero": "yourSuperHero"
})
print(story_1)