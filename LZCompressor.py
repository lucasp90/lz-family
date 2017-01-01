"""
LZ Compressor module
"""

import Utils

RLE_MATCH_COUNT = 4

class RLE:
    """
    Run Length Encoder-Decoder
    """

    def __init__(self):
        self.match_count = RLE_MATCH_COUNT


    def encode(self, char_sequence):
        """
        Given a sequence of characters, returns its RLE representation.
        @arguments:
        - char_sequence (str): a sequence to be encoded.
        """
        encoded_sequence = ""
        current_index = 0
        while current_index < len(char_sequence):
            repetitions = Utils.consecutive_repetitions(char_sequence[current_index:])
            if len(repetitions) < self.match_count:
                encoded_sequence += repetitions
            else:
                rep_code = str(len(repetitions[self.match_count:]))
                encoded_sequence += repetitions[:self.match_count] + rep_code
            current_index += len(repetitions)
        return encoded_sequence

    def decode(self, encoded_sequence):
        """
        Given a sequence of characters, decodes it using the RLE method.
        @arguments:
        - char_sequence (str): a sequence to be decoded.
        """
        decoded_sequence = ""
        current_index = 0
        while current_index < len(encoded_sequence):
            repetitions = Utils.consecutive_repetitions(encoded_sequence[current_index:])
            current_index += len(repetitions)
            if len(repetitions) < self.match_count:
                decoded_sequence += repetitions
            else:
                rep_code = ""
                rep_character = repetitions[0]
                while current_index < len(encoded_sequence) and encoded_sequence[current_index].isdigit():
                    rep_code += encoded_sequence[current_index]
                    current_index += 1
                decoded_sequence += repetitions + rep_character * int(rep_code)
        return decoded_sequence

