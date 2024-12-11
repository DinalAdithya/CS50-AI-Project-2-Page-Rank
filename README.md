# PageRank Project

This project implements the PageRank algorithm, a foundational concept in web search technology, to rank webpages based on their relative importance. By simulating a random surfer and applying iterative calculations, the program generates rankings similar to those used by modern search engines.

## Features

- **Random Surfer Model**: Simulates a user randomly navigating between links.
- **Iterative Algorithm**: Computes PageRank values through repeated updates until convergence.
- Handles complex hyperlink structures in directed graphs.

## How It Works

1. **Crawl a corpus of webpages** to extract links between pages.
2. Use two algorithms to calculate PageRank:
   - **Random Surfer Model**: Simulates random navigation based on transition probabilities.
   - **Iterative Algorithm**: Adjusts ranks iteratively until reaching a stable state.
3. Outputs a dictionary with the PageRank values for each page.

## Project Files

- `pagerank.py`: Main script containing the implementation of the PageRank algorithm.
- `corpus/`: A sample set of HTML pages to test the algorithm.
- `README.md`: Project documentation.

