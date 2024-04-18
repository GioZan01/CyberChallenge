import random
from os import environ
from http import HTTPStatus
from flask import Flask, request, Response, redirect, render_template


app = Flask(__name__)

lipsum = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat
nulla pariatur. Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum.
"""

random.seed(42, version=2)
page_indices = random.sample(range(1, 10000000), 1000)
start_page = random.choice(page_indices)
currently_unreachable = set(page_indices)
currently_unreachable.remove(start_page)
flag_page_index = random.choice(list(currently_unreachable))


def generate_page(i, flag_page=False):
    nlinks = random.randrange(2, 8)
    unreachable_list = list(currently_unreachable)
    linked_pages = set(random.sample(unreachable_list, min(len(unreachable_list), 2)))
    currently_unreachable.difference_update(linked_pages)
    linked_pages.update(random.sample(page_indices, nlinks-len(linked_pages)))

    nparagraphs = 4
    paragraphs = [
        [(word, None) for word in lipsum.split()]
        for _ in range(nparagraphs)
    ]
    words_in_paragraph = len(paragraphs[0])
    tot_words = words_in_paragraph * nparagraphs

    random.shuffle(list(linked_pages))
    link_word_indices = random.sample(range(tot_words), len(linked_pages))
    for linked_page, link_word_index in zip(linked_pages, link_word_indices):
        paragraph_index, word_index = divmod(link_word_index, words_in_paragraph)
        paragraphs[paragraph_index][word_index] = (paragraphs[paragraph_index][word_index][0], linked_page)

    # Final structure:
    # paragraphs = [
    #   [
    #     ("Lorem", None),
    #     ("ipsum", None),
    #     ("dolor", 1337)
    #     ("sit",   None),
    #     ...
    #   ], [
    #     ("Lorem", None),
    #     ("ipsum", 4242)
    #     ("dolor", None),
    #     ...
    #   ]
    # ]

    with app.app_context():
        return render_template(
                "page.html",
                i=i,
                flag_page=flag_page,
                flag=environ["FLAG"],
                paragraphs=paragraphs)


pages = {i: generate_page(i, i==flag_page_index) for i in page_indices}

start_page = f"/page?p={random.choice(page_indices)}"


@app.route("/")
def index():
    return redirect(start_page, code=HTTPStatus.SEE_OTHER)


@app.route("/page")
def page():
    try:
        return pages[int(request.args["p"])]
    except (KeyError, ValueError):
        return Response("Not found", mimetype="text/plain", status=HTTPStatus.NOT_FOUND)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
