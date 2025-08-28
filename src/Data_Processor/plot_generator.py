from bokeh.plotting import figure, output_file, save
from bokeh.layouts import column
from bokeh.models import ColumnDataSource
import pandas as pd

"""This wil generate visualization with test data and mapped results"""
class PlotGenerator:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def generate_visualization(self, selected_functions, output_html="visualization.html"):
        train_data = self.db_manager.get_training_data()
        ideal_data = self.db_manager.get_ideal_functions_data()
        test_data = self.db_manager.get_test_data()
        train_df = pd.DataFrame(
            [(t.x, t.y1, t.y2, t.y3, t.y4) for t in train_data],
            columns=["x", "y1", "y2", "y3", "y4"])
        ideal_df = pd.DataFrame(
            [(i.x,) + tuple(getattr(i, f"y{j}") for j in range(1, 51)) for i in ideal_data],
            columns=["x"] + [f"y{j}" for j in range(1, 51)])
        test_df = pd.DataFrame(
            [(t.x, t.y, t.delta_y, t.ideal_function_no) for t in test_data],
            columns=["x", "y", "delta_y", "ideal_function_no"])
        plots = []
        for i in range(1, 5):
            y_label = f"y{i}"
            ideal_label = selected_functions[y_label]  
            ideal_idx = int(ideal_label[1:])  
            p = figure(
                title=f"Training {y_label} vs Ideal {ideal_label}",
                x_axis_label="x", y_axis_label="y")
            p.circle(train_df["x"], train_df[y_label],
                     size=5, color="blue", alpha=0.5, legend_label=f"Training {y_label}")
            p.line(ideal_df["x"], ideal_df[f"y{ideal_idx}"],
                   line_width=2, color="green", legend_label=f"Ideal {ideal_label}")
            mapped_points = test_df[test_df["ideal_function_no"] == ideal_label.upper()]
            if not mapped_points.empty:
                p.triangle(mapped_points["x"], mapped_points["y"],
                           size=8, color="red", alpha=0.7, legend_label="Mapped Test")
            p.legend.location = "top_left"
            plots.append(p)
        output_file(output_html)
        save(column(*plots))
        print(f"Visualization saved to {output_html}")
