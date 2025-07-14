from collections import Counter


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Count the frequency of each character
        char_count = Counter(s)
        # Sort characters by their lexicographical order in descending order
        sorted_keys = sorted(char_count.keys(), reverse=True)

        result = []
        n = len(sorted_keys)

        for i in range(n - 1):
            key = sorted_keys[i]
            while char_count[key] > repeatLimit:
                # Find the next available character
                next_key = ""
                for j in range(i + 1, n):
                    if char_count[sorted_keys[j]] > 0:
                        next_key = sorted_keys[j]
                        break

                # If no valid next character exists, break the loop
                if not next_key:
                    break

                # Add the current character up to the repeat limit
                result.append(key * repeatLimit)
                char_count[key] -= repeatLimit

                # Add one instance of the next character
                result.append(next_key)
                char_count[next_key] -= 1

            # Add remaining instances of the current character (if any)
            result.append(key * char_count[key])
            char_count[key] = 0

        # Add any remaining characters from the last position onward
        for key in sorted_keys:
            result.append(key * min(char_count[key], repeatLimit))

        return "".join(result)
