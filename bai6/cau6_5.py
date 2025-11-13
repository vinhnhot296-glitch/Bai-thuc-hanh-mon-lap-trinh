class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))

# Example usage
print(py_solution().reverse_words('hello .py'))
