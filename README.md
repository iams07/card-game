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
