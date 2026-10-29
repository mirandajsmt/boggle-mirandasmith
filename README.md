# Boggle Game

## Overview

This project implements a generalized version of **Boggle**, a word game in which players identify words formed by connecting adjacent letters on a grid. The game is written in Python and explores recursive algorithms, efficient dictionary lookup, and search optimization.

The board is randomly generated from lettered cubes, and players receive points for identifying valid words. A computer player searches for additional words that the human player missed.

## Features

- **Board generation:** Create a randomized Boggle board of a specified size using lettered cubes.
- **Word validation:** Check whether submitted words meet the game's rules, exist in the dictionary, and can be formed on the board.
- **Recursive search:** Explore adjacent letters horizontally, vertically, and diagonally while ensuring that each cube is used at most once per word.
- **Trie-based dictionary:** Store dictionary words in a Trie data structure to support word lookup and prefix checking.
- **Computer word discovery:** Search for valid words that the human player has not already identified.
- **Scoring:** Calculate scores based on word length.
- **Interactive gameplay:** Accept player input, display results, and allow additional games.

## Algorithms and Data Structures

This project explores several fundamental computer science concepts:

- **Recursion and backtracking:** Search the board for valid sequences of letters while tracking visited positions.
- **Trie data structure:** Organize dictionary words for efficient lookup and prefix-based pruning.
- **Search optimization:** Use dictionary prefixes to avoid exploring paths that cannot produce valid words.
- **Algorithm design:** Compare board-driven and dictionary-driven strategies for finding valid words.

## Technologies

- Python 3
- Python standard library
- Pytest for testing

## Running the Game

Run the game from the project directory:

```bash
python3 boggle.py
```

To view available command-line options:

```bash
python3 boggle.py -h
```

The game uses a cube configuration file and a word dictionary. Ensure the required files are present in the expected locations before running the program.

## Project Structure

The implementation is organized around separate components for game mechanics and dictionary management:

- `boggle.py` — Game entry point and user interface.
- `my_game_manager.py` — Game mechanics, board management, word validation, and search.
- `trie_dictionary.py` — Trie-based dictionary implementation.
- `boggle_game.py` — Game interface.
- `boggle_dictionary.py` — Dictionary interface.
- `cubes.txt` — Letter configurations for the cubes.
- `words.txt` — Dictionary of valid words.

## Learning Objectives

The project provides practical experience with recursive algorithms, data structures, interface-based design, testing, and performance considerations when searching large collections of words.
