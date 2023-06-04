import pandas as pd
from pyfzf import FzfPrompt


max_opts = "-p 80% --reverse --ansi --prompt='python is pretty dope > ' --info=inline"

# Copying Monokai Extended
# but I should just be able to import any .tmTheme
# head spinning from .tmTheme XML file layout
MONOKAI = {
        "red": (249, 38, 114),
        "orange": (253, 151, 31),
        "green": (166, 226, 46),
        "blue": (102, 217, 239),
        "purple": (190, 132, 255)
        }


class FuzzyPanda(FzfPrompt):

    def __init__(self, fzf_executable, df, default_opts=max_opts, colorscheme=MONOKAI):
        self.df = df
        self.colorscheme = colorscheme
        super().__init__(fzf_executable, default_opts)

    def comb(self):
        "Quickly and interactively subset a DataFrame."
        col = self.prompt(
                self.df.columns,
                "--header='columns in the dataframe...'")
        value_of_interest = self.prompt(
                self.df[col].unique(),
                "--header='unique values in the chosen column.'")
        return self.df[self.df[col] == value_of_interest]

    def groom(self):
        "Load the DataFrame into fzf row by row."
        # TODO: imitate df.__repr__()
        pass

    def colorize(self, string, color):
        "Print an ansi-colorized string via rgb tuple."
        print(self.__colo_rgb__(string, self.colorscheme[color]))

    def __colo_rgb__(self, string, rgb):
        "Prepend an RGB ansi color escape code to a string."
        r, g, b = rgb
        return f"\x1b[38;2;{r};{g};{b}m{string}\x1b[0m"

    def colorize_columns(self):
        # cols = self.df.columns
        # and then replace the keys with ansi color codes
                                                    # how do i runover???!??!!
                                                    # i have n columns
        # for i in range(cols): % len(self.colorscheme)
        # self.df.itertuples()
        pass


def test():
    jim = FuzzyPanda('fzf-tmux', pd.read_csv("05-30-2023.csv"))
    colo = jim.colorize('cow', 'red')
    colo = jim.colorize('cow', 'orange')
    colo = jim.colorize('cow', 'green')
    colo = jim.colorize('cow', 'blue')
    colo = jim.colorize('cow', 'purple')
    with open('cow', 'w') as f:
        f.write(jim.df.__repr__())
    # print(colo)


test()
