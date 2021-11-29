"""Plot frustration scan."""
import pickle
from simplicial_kuramoto.frustration_scan import plot_order_1d
from simplicial_kuramoto.plotting import draw_simplicial_complex

if __name__ == "__main__":

    folder = "./results/"
    for i in range(3):
        filename = f"complex_{i}"
        path = path = folder + filename + ".pkl"

        plot_order_1d(path=path, filename=filename + ".pdf")

        Gsc, results, alpha1, alpha2 = pickle.load(open(path, "rb"))
        draw_simplicial_complex(Gsc, filename=filename + "_graph.pdf")
