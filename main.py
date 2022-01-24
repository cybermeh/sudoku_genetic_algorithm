from sudoku import Sudoku

if __name__ == '__main__':
    s = Sudoku(
        number_of_candidates=500,
        number_of_elites=80,
        number_of_generations=1000,
        number_of_mutations=0,
        selection_rate=0.85
    )

    s.load('input.txt')

    r = s.solve()

    if r:
        s.save('output.txt', r)
