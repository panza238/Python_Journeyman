"""An executable directory!"""
import sys

segments = sys.argv[1:]
full_text = ' '.join(segments)
output = f'# words: {len(full_text.split())}, # chars: {sum(len(w) for w in full_text.split())}'
print(output)
