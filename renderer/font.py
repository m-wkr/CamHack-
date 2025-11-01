def bold(text: str) -> str:
    t_bold = ''
    for ch in text:
        if ch >= 'A' and ch <= 'Z':
            ch = chr(ord(ch) - ord('A') + 0x1D5D4)
        
        elif ch >= 'a' and ch <= 'z':
            ch = chr(ord(ch) - ord('a') + 0x1D5EE)
        
        elif ch >= '0' and ch <= '9':
            ch = chr(ord(ch) - ord('0') + 0x1D7EC)

        t_bold += ch
    return t_bold

def underline(text: str) -> str:
    return ''.join([c + '\u035f' for c in text])