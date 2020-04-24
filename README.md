# Card-game                      
Pre-requisites: Python,pygame

## Rules of the Game:
- There are 4 players who play this game. Each player receives 13 cards each. Let us denote the players as P1,P2,P3 and P4.
- P1 and P3 are a team, as are P2 and P4.
- P1 first declares a suit as trump, based on which suit he has most.
- The priority order for cards is 2,3,4,..,J,Q,K,A.
- P1 plays a card, then P2,P3 and P4.
  - The player who has played the highest card of the same suit as the one P1 has played wins the deal.
  - Next card will be played by the guy who won the previous deal.
- If someone doesn't have any cards left of the suit that was played by the first player, he can play the cards of the trump suit.
  - Trump suit supercedes all other suits.
  - If someone doesn't have any trump, then he can play a card of any other suit as well, but that will be superceded by the original suit.
- If a team wins 7 deals, they win the game.
- The team which wins, gets to decide the trump suit for the next game.

## Walkthrough of the game:

By default, the user in 1 player game is p4, in two player(rival) p3 and p4, in two player(team) p2 and p4, and so on.

The cards for user will be visible only when the cursor is hovering over their cards in their turn. So, each player can view their cards only in their turn. This way, 2 or more players can also play the game.

![](/Readme_images/Start.png)
![](/Readme_images/trump.png)
![](/Readme_images/Deal.png)
![](/Readme_images/Winner.png)
![](/Readme_images/Trump.png)
![](/Readme_images/notrump.png)
![](/Readme_images/new.png)
![](/Readme_images/win.png)

Since team 2 wins, in the next game, trump suit will be decided by p2.
