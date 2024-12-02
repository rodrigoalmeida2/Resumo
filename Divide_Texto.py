class TextSplitter:
    """divide o texto em partes menores."""
    
    @staticmethod
    def split(text, max_tokens):
        """Divide o texto com base no limite de tokens."""
        words = text.split()
        parts = []
        current_part = []
        current_length = 0

        for word in words:
            current_length += len(word) + 1  # Inclui o espaço
            if current_length > max_tokens:
                parts.append(' '.join(current_part))
                current_part = [word]
                current_length = len(word) + 1
            else:
                current_part.append(word)
        parts.append(' '.join(current_part))
        return parts
