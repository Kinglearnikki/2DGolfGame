# GolfGame_OOP
Get ready for a 2D golfing experience! Use your mouse to direct the ball and adjust your power. The objective of the game is to complete each hole in as few strokes and little time as possible while navigating through courses with varying obstacles that become more complex with each level.
Golfing will be pretty simple but different terrains and obstacles like sand traps, water hazards, and various walls affect your ball differently, requiring a different strategy. Starting on an easier course, the difficulty ramps up with each level, introducing more challenging terrains and obstacles.
Shoot fast and shoot well, your time and shots will both be tracked in the scoreboard.

Features and Functionalities:
Course Design: The game offers 5 unique golf courses with diverse terrains, including grass, sand and ice traps, and water hazards. Each course presents different challenges and strategies.
Player Controls: Users can interact with the game through intuitive controls, adjusting the aim and power of their shots.
Score Tracking: The game keeps track of the number of strokes and time per hole/level
Obstacles and Hazards: The golf course is filled with obstacles like trees and walls. Hitting some of these obstacles may result in penalty strokes and time loss, adding a strategic layer to the game.
Achievements and Rewards: Unlockable achievements recognize players for various in-game accomplishments. Rewards, such as new equipment or customization options, motivate players to achieve milestones.

Domain Model Diagram
Conceptual Classes:
Player: Represents the human player participating in the game, storing their score and achievements.
Golf Ball: Models the in-game character, influenced based on attributes such as skill level and experience points.
Course: Defines the characteristics of a golf course, including its name, difficulty level, and various terrain types.
Hole: Represents an individual hole on a golf course, storing information like par value, number, and specific obstacles.
Obstacle: Represents different obstacles on the golf course, such as bunkers, trees, and water hazards, affecting gameplay.
Scoreboard: Keeps track of the player's performance by recording the number of strokes per hole and the total score.
Scorecard: Manages player’s score and displays it to the player
Achievement: Represents in-game accomplishments, tracking the player's progress.
Reward: Represents funny animations that play when the player achieves something
