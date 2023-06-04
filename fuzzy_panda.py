import pandas as pd
from pyfzf import FzfPrompt


# Is this a DataFrame with an FzfPrompt wrapper?
# Or an FzfPrompt with a DataFrame attribute?
# God -- the latter seems ridiculous.
class FuzzyPanda():

    # let the user choose between 'fzf' or 'fzf-tmux'
    # what's the most pythonic way to do it?
    def __init__(self, df, fzf_opts=None, fzf_executable='fzf'):
        self.df = df
        self.fzf = FzfPrompt(fzf_executable, fzf_opts)

    def __doc__(self):
        return "Wraps a given pandas DataFrame with a pyfzf.FzfPrompt class."

    def prompt(self, col=None, opts=None):
        if col is None:
            return self.fzf.prompt(self.df.columns, "+m")
        return self.fzf.prompt(self.df[col], opts)
