def str_str(haystack: str, needle: str) -> int:
    
    return haystack.find(needle)

def main() -> None:
    
    h = "sadbutsad"
    n = "sad"
    print(str_str(h, n))
    
    h1 = "leetcode"
    n1 = "leeto"
    print(str_str(h1, n1))
    
if __name__ == "__main__":
    main()