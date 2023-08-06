def bashlex_iter(part):
    if hasattr(part, 'word'):
        yield part.word
    elif hasattr(part, 'op'):
        yield part.op
    elif hasattr(part, 'kind') and part.kind == "redirect":
        yield part.type
        yield from bashlex_iter(part.input)
        yield from bashlex_iter(part.output)
    elif hasattr(part, 'parts'):
        for sub in part.parts:
            yield from bashlex_iter(sub)

def bashlex_commands(part):
    if hasattr(part, 'kind'):
        if part.kind == "command":
            buffer = []
            i = 0
            while i < len(part.parts):
                sub = part.parts[i]
                if not (hasattr(sub, "kind") and sub.kind == "word"):
                    if buffer:
                        yield part, buffer
                        buffer = []
                    i += 1
                    continue
                if hasattr(sub, 'parts'):
                    for nested in sub.parts:
                        yield from bashlex_commands(nested)
                buffer.append(sub.word)
                i += 1
            if buffer:
                yield part, buffer
        elif part.kind == "commandsubstitution":
            yield from bashlex_commands(part.command)
        elif part.kind == "list":
            for part in part.parts:
                yield from bashlex_commands(part)
