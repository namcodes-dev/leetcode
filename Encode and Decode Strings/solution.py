class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string."""
        encoded = ""
        for s in strs:
            # Use length of string and a delimiter to separate strings
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s):
        """Decodes a single string to a list of strings."""
        decoded = []
        i = 0
        while i < len(s):
            # Find the position of the delimiter
            j = s.find('#', i)
            print("j= ", j)
            # Get the length of the string
            length = int(s[i:j])
            print("length= ", length)
            # Extract the string using the length
            decoded.append(s[j+1:j+1+length])
            # Move to the next string
            i = j + 1 + length
        return decoded

codec = Codec()

# Example: Encoding
input_strings = ["hello", "world"]
encoded = codec.encode(input_strings)
print("Encoded:", encoded)  # Output: "5#hello5#world"

# Example: Decoding
decoded = codec.decode(encoded)
print("Decoded:", decoded)  # Output: ["hello", "world"]