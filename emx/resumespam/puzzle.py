import operator


class LetterValue():
  def __init__(self, name, value):
    self.name = name
    self.value = value

  def __repr__(self):
    return self.name


class Puzzle():

  SYMBOLS = {
      '<': operator.lt,
      '>': operator.gt,
      '=': operator.eq,
    }

  def __init__(self, input_str):
    """
    Processed input string and initlizes order dict
    """
    input_str = input_str.split('\n')[2:-1]
    self.processed = [i[1:] for i in input_str]
    self.letter_dict = {
      0: LetterValue("A", -2),
      1: LetterValue("B", -1),
      2: LetterValue("C", 1),
      3: LetterValue("D", 2),
    }

  def swap(self, i, j):
    """
    Swaps the order depending on inequality relation
    """
    temp = self.letter_dict.get(i).value
    self.letter_dict.get(i).value = self.letter_dict.get(j).value
    self.letter_dict.get(j).value = temp

  def main_loop(self, input_str):
    """
    Processes letter dict depending on given conditions/inequalities
    """
    for ipos, i in enumerate(input_str):
      for k, j in enumerate(i):
        if j in ('<', '>', '='):
          if self.SYMBOLS.get(j)(self.letter_dict.get(ipos).value, self.letter_dict.get(k).value):
            pass
          else:
            self.swap(ipos, k)

  def __call__(self):
    for _ in range(4):  # To normalize the order depending on previous inequalities and we have 4 variables here.
      self.main_loop(self.processed)
    print(self.letter_dict)
    output = " ABCD\n"
    for i in self.letter_dict.values():
      out_inter = i.__repr__()
      for j in self.letter_dict.values():
        if i.value > j.value:
          out_inter = out_inter + ">"
        elif i.value == j.value:
          out_inter = out_inter + "="
        else:
          out_inter = out_inter + "<"
      output = output+out_inter + "\n"
    return output.rstrip()
