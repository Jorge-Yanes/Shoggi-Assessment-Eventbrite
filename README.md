# Shoggi Assessment

<p align="center"><img width=70% src="https://raw.githubusercontent.com/Jorge-Yanes/Shoggi-Assessment-Eventbrite/master/media/logo.png"></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)

## Basic Overview of the Game

<p><img width=30% src="https://raw.githubusercontent.com/Jorge-Yanes/Shoggi-Assessment-Eventbrite/master/media/shogi-board.png" align="right">Shogi, also known as Japanese chess, is a two-player strategy board game native to Japan. In this game, two players face each other across a board composed of rectangles in a grid of 9 rows by 9 columns yielding an 81 square board. Each player has a set of 20 flat wedge-shaped pentagonal pieces of slightly different sizes, each of them with different moves. The usual goal of a game is for one player to checkmate the other player's king, winning the game.</p>


## Project Overview

This project, currently, is a partial implementation of the game in Python. Currently the project has different classes developed:

<ul>
  <li>Piece class, contains all the common properties for all the different pieces.</li>
  <li>Cell class, contains the position of the piece.</li>
  <li>Board class, contains an array of Cells and a first development scheme of the final board. </li>
  <li>A class for each of the pieces, that contains a function to see whether a movement is allowed or not. ( Not all the pieces are implemented )</li>
  <li>A test class for each of the pieces, which checks all the allowed and not allowed movements for each of the pieces both when they are crowned and when they are not.</li>
</ul>