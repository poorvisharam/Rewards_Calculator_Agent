def enforce_single_word(output: str) -> str:
    words = output.strip().lower().split()
    return words[0] if len(words) == 1 else "other" 
