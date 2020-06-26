from random import randint

from bokeh.plotting import figure, output_file, show

if __name__ == "__main__":
    output_file('graficado_simple.html')
    fig = figure()

    total_vals = int(input('Cuántos valores quieres graficar? '))
    x_vals = list(range(total_vals))
    y_vals = []

    for x in x_vals:
        y_vals.append(randint(1,100))

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)