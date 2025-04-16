"""
Bowling Game Implementation
A module for calculating bowling game scores.
"""


class BowlingGame:
    def __init__(self):
        # Initialize a new game with 10 frames
        # Each frame has up to 2 rolls (except the 10th frame which can have 3)
        self.rolls = []
        

    def roll(self, pins):
        """
        Records a roll in the game.

        Args:
            pins: Number of pins knocked down in this roll
        """
        self.rolls.append(pins)
        

    def score(self):
        """Calculate the score for the curent game."""
        score, frame_index = self._score_frames_1_to_9()
        score += self._score_10th_frame(frame_index)
        return score


    def _score_frames_1_to_9(self):
        #Handles acoring for frames 1 to 9
        score = 0
        frame_index = 0

        for _ in range(9):
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
        
        return score, frame_index

            
        
    def _score_10th_frame(self, frame_index):
       #Handles 10th frame logic
        if frame_index >= len(self.rolls):
            return 0  # No rolls to process

        if self._is_strike(frame_index):  #Strike
            base = 10
            bonus1 = self.rolls[frame_index + 1] if (frame_index + 1) < len(self.rolls) else 0
            bonus2 = self.rolls[frame_index + 2] if (frame_index + 2) < len(self.rolls) else 0
            return base + bonus1 + bonus2

        elif self._is_spare(frame_index): #spare
            base = 10
            bonus = self.rolls[frame_index + 2] if (frame_index + 2) < len(self.rolls) else 0
            return base + bonus

        else:
            # Open frame
            roll1 = self.rolls[frame_index] if (frame_index) < len(self.rolls) else 0
            roll2 = self.rolls[frame_index + 1] if (frame_index + 1) < len(self.rolls) else 0
            return roll1 + roll2

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