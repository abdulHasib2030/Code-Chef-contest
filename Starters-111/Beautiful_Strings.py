MOD = 10**9 + 7

def countBeautifulStrings(N, S):
    freq = [0] * 26  # Frequency array for each lowercase English letter

    # Count the frequency of each character in string S
    for char in S:
        freq[ord(char) - ord('a')] += 1

    result = 1  # Initialize the result to 1

    # Calculate the count of unique beautiful strings
    for i in range(26):
        result = (result * (freq[i] + 1)) % MOD

    return result-1

# Input reading and processing
T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    result = countBeautifulStrings(N, S)
    print(result)
