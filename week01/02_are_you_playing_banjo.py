"""
Kata: Are You Playing Banjo?

Goal:
Return "<name> plays banjo" if the name starts with 'R' (case-insensitive),
otherwise return "<name> does not play banjo".

Concepts practiced:
- String indexing
- Case normalization using .lower()
- Conditional logic
- Clean return statements
"""

def are_you_playing_banjo(name: str) -> str:
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


if __name__ == "__main__":
    print(are_you_playing_banjo("Rick"))   # Rick plays banjo
    print(are_you_playing_banjo("Alice"))  # Alice does not play banjo
