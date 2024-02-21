# Super Six Strategy Tester

## Overview
The Super Six Strategy Tester is a project aimed at testing different strategies in the game "Super Six" against each other. 

## Game Rules
- Before the game starts, an equal number of sticks is distributed to each of the two to six participating players.
- The goal of the game is to be the first player to get rid of all their sticks.
- In the first round, each player takes turns rolling the die. If a player rolls a "6", they can place a stick in the corresponding hole of the container. If the slot matching the rolled number is already occupied, the player must remove the stick from that slot and take it back to their own stick supply.
- From the second round onwards, each player can continue rolling the die until they have to take one or all sticks, or they can choose to stop earlier.

## Project Structure
- **classes**: This directory contains the necessary classes for the game, each in a separate .py file
- **functions/strategies.py**: This file contains the implemented strategies for the game. Strategies are functions that return False when a stop condition is reached, and True to continue the game. All strategies have to be added to the **strat_list** to be available in the simulation.
- **functions/play_super_six**: This file contains the actual implementation of the game.
- Top-level files call the functions from the **functions** directory to run simulations.

## Getting Started
To get started with the Super Six Strategy Tester, follow these steps:
1. Clone the repository.
2. Install the required dependencies.
3. Modify and run the files in the top-level directory
4. Possibly implement further/own strategies to test.

## Contributing
Contributions to the project are welcome! If you have a new strategy to add or want to improve the existing ones, feel free to submit a pull request.

## License
This project is licensed under the EUPL v. 1.2 License - see the [LICENSE](LICENSE) file for details.