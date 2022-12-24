import textwrap


class UI:
  def __init__(self):
    # Initialize any necessary instance variables here
    pass

  def get_input(self, input_prompt):
    # Prompt the user for input and return the user's response
    return input(f'{input_prompt}')

  def print_output(self, output):
    # Print the given output to the console
    trimmed_output = output.strip()
    wrapped_text = textwrap.fill(
      trimmed_output,
      width=50,
      tabsize=1,
      initial_indent='\t',
      subsequent_indent='\t'
    )
    print(wrapped_text)
