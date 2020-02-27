import pandas as pd


def get_posts():
    f = pd.read_csv("posts.csv")
    names = f.name
    text = f.post
    posts = []
    for i in range(len(names)):
        posts += [{
            'author': {'username': names[i]},
            'body': text[i]
        }]
    return posts


print(get_posts())
