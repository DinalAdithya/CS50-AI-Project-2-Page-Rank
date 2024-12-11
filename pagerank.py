import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages

def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    corpus_dict = {}
    total_pages = len(corpus)
    prob3 = (1 - damping_factor) / total_pages

    # Initialize all pages with base probability
    for Every_page in corpus:
        corpus_dict.update({Every_page: prob3})

    # Adjust prob for linked pages
    if corpus[page]:
        total_pages = len(corpus[page])
        prob2 = damping_factor / total_pages

        for linked_page in corpus[page]:
            corpus_dict[linked_page] += prob2 # Increment by damping prob by

    return corpus_dict


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pageRank = {}

    for page in corpus:
        pageRank.update({page: 0})

    starting_page = random.choice(list(corpus.keys()))

    for sample in range(n):
        pageRank[starting_page] += 1
        prob = transition_model(corpus, starting_page, damping_factor)
        starting_page = random.choices(list(prob.keys()), list(prob.values()))[0]

    for page in pageRank:
        pageRank[page] /= n

    return pageRank

def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pagerank = {}
    page_count = len(corpus)
    value = 1 / page_count
    teleportation_value = (1 - damping_factor) / page_count

    for page in corpus:
        pagerank.update({page: value})

    while True:
        sum_dif = 0
        new_pagerank = pagerank.copy()

        for page in corpus:
            new_val = teleportation_value

            for linked_page in corpus:

                if page in corpus[linked_page]:

                    linked_page_contribution = damping_factor * (pagerank[linked_page] / len(corpus[linked_page]))  # eg:- X page has 2 linked pages x page value is 0.2 so other pages get 0.1 value each

                    new_val += linked_page_contribution

            difference_value = abs(pagerank[page] - new_val) # absolute value (abs) of this difference ensures that we’re measuring only the size of the change, regardless of whether the value increased or decreased.
            sum_dif += difference_value

            new_pagerank.update({page: new_val})

        pagerank = new_pagerank

        if sum_dif < 0.001:
            break
    return pagerank


if __name__ == "__main__":
    main()

