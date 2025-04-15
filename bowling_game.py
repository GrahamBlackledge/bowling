"""
Bowling Game Implementation
A module for calculating bowling game scores.
"""


class BowlingGame:
    def __init__(self):
        # Initialize a new game with 10 frames
        # Each frame has up to 2 rolls (except the 10th frame which can have 3)
        self.rolls = []
        self.current_roll = 0

    def roll(self, pins):
        """
        Records a roll in the game.

        Args:
            pins: Number of pins knocked down in this roll
        """
        self.rolls.append(pins)
        self.current_roll += 1

    def score(self):
        """Calculate the score for the current game."""
        score = 0
        frame_index = 0

        for frame in range(9):
            if self._is_strike(frame_index):
                # Strike
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                # Spare
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                # Open frame ---- Now adds both rolls 
                score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2

            # Logic for handling 10th frame
        if frame_index < len(self.rolls):
            if self._is_strike(frame_index):   #strike
                print("DEBUG 10th frame: STRIKE path")
                score += 10   
                if (frame_index + 1) < len(self.rolls):  
                    score += self.rolls[frame_index + 1]
                if (frame_index + 2) < len(self.rolls):
                   score +=  self.rolls[frame_index + 2]
            elif self._is_spare(frame_index):
                print("DEBUG 10th frame: SPARE path")
            # Spare
                score += 10
                if (frame_index + 2) < len(self.rolls):
                    score += self.rolls[frame_index + 2]
        else:
            # Open frame
            if (frame_index + 1) < len(self.rolls):
                print("DEBUG 10th frame: OPEN path")
                print(f"DEBUG 10th frame: Indices {frame_index}, {frame_index+1}")
                score += self.rolls[frame_index] + self.rolls[frame_index + 1]
            else:
                score += self.rolls[frame_index]

            
                          

        return score

    def _is_strike(self, frame_index):
        """
        Check if the roll at frame_index is a strike.

        Args:
            frame_index: Index of the roll to check

        Returns:
            True if the roll is a strike, False otherwise
        """
        return frame_index < len(self.rolls) and self.rolls[frame_index] == 10

    def _is_spare(self, frame_index):
        """
        Check if the rolls at frame_index and frame_index + 1 form a spare.

        Args:
            frame_index: Index of the first roll in a frame

        Returns:
            True if the rolls form a spare, False otherwise
        """
        return frame_index + 1 < len(self.rolls) and self.rolls[frame_index] + self.rolls[frame_index + 1] == 10

    def _strike_bonus(self, frame_index):
        """
        Calculate the bonus for a strike.

        Args:
            frame_index: Index of the strike roll

        Returns:
            The value of the next two rolls after the strike
        """
        return self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def _spare_bonus(self, frame_index):
        """
        Calculate the bonus for a spare.

        Args:
            frame_index: Index of the first roll in a spare

        Returns:
            The value of the roll after the spare
        """
        return self.rolls[frame_index + 2]