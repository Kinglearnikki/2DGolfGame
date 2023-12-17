# GolfGame_OOP

**TO DO**
_Updated Dec 15, 2023 8:13PM_

- [DONE]Add timer
- [DONE]Add number of strokes
- Add different levels
- Add menu to enter different levels
- [In progress: Clive]Add back to main menu button (in each level)
- Add obstacles
- Add different Balls with different attributes
- Add terrains
- Add scorecard
- Add database to save scorecard
- Add scoreboard (inside scoreboard kay ang sud sa scorecard na makuha sa database)

---

Get ready for a 2D golfing experience! Use your mouse to direct the ball and adjust your power. The objective of the game is to complete each hole in as few strokes and little time as possible while navigating through courses with varying obstacles that become more complex with each level.
Golfing will be pretty simple but different terrains and obstacles like sand traps, water hazards, and various walls affect your ball differently, requiring a different strategy. Starting on an easier course, the difficulty ramps up with each level, introducing more challenging terrains and obstacles.
Shoot fast and shoot well, your time and shots will both be tracked in the scoreboard.

**Features and Functionalities:**

1. Course Design: The game offers 5 unique golf courses with diverse terrains, including grass, sand and ice traps, and water hazards. Each course presents different challenges and strategies.
2. Player Controls: Users can interact with the game through intuitive controls, adjusting the aim and power of their shots.
3. Score Tracking: The game keeps track of the number of strokes and time per hole/level
4. Obstacles and Hazards: The golf course is filled with obstacles like trees and walls. Hitting some of these obstacles may result in penalty strokes and time loss, adding a strategic layer to the game.
5. Achievements and Rewards: Unlockable achievements recognize players for various in-game accomplishments. Rewards, such as new equipment or customization options, motivate players to achieve milestones.

**Domain Model Diagram**

- **Conceptual Classes:**
  1. Player: Represents the human player participating in the game, storing their score and achievements.
  2. Golf Ball: Models the in-game character, influenced based on attributes such as skill level and experience points.
  3. Course: Defines the characteristics of a golf course, including its name, difficulty level, and various terrain types.
  4. Hole: Represents an individual hole on a golf course, storing information like par value, number, and specific obstacles.
  5. Obstacle: Represents different obstacles on the golf course, such as bunkers, trees, and water hazards, affecting gameplay.
  6. Scoreboard: Keeps track of the player's performance by recording the number of strokes per hole and the total score.
  7. Scorecard: Manages player’s score and displays it to the player
  8. Achievement: Represents in-game accomplishments, tracking the player's progress.
  9. Reward: Represents funny animations that play when the player achieves something
