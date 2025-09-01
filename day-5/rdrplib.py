import sys
import plotly.graph_objects as go

from utils import parse_dna_structure

ENTRY_STEM = 0
ENTRY_GROOVE = 1
ACTIVE_SITE = 2
EXIT_GROOVE = 3
EXIT_STEM = 4


class RdrpFig:
    # x and y of the origin.
    ORIGIN = 0.0, 0.0

    def __init__(self, rna, structure, config):
        self.rna = rna
        self.structure = structure
        self.config = config

    def get_coords(self):
        origin_x, origin_y = self.ORIGIN
        v_gap = self.config["vertical_gap"]
        h_gap = self.config["horizontal_gap"]
        divider_gap = self.config["divider_gap"]

        self.active_site_top = self.ORIGIN
        self.active_site_bottom = (
            origin_x,
            origin_y - len(self.fragments["structure"][ACTIVE_SITE]) * v_gap,
        )

    def draw_active_site(self, fig):
        active_site = self.fragments["rna"][ACTIVE_SITE]
        active_site_length = len(active_site)
        y = []
        y_top = self.active_site_top[1]
        v_gap = self.config["vertical_gap"]

        for i in range(active_site_length):
            y.append(y_top - i * v_gap)

        colors = [self.config["colors"][nt] for nt in active_site]

        fig.add_trace(
            go.Scatter(
                x=[self.active_site_top[0]] * 2,
                y=[y[0], y[-1]],
                mode="lines",
                line=dict(color="#EEE"),
            )
        )

        fig.add_trace(
            go.Scatter(
                x=[self.active_site_top[0]] * active_site_length,
                y=y,
                mode="text",
                text=list(active_site),
                textposition="middle center",
                textfont={
                    "size": self.config['fontsize'],
                    "color": colors,
                },
            )
        )
        

    def save_figure(self, filename, show_grid=False):
        print(
            f"Producing figure in {filename} with font size {self.config['fontsize']}.",
            file=sys.stderr,
        )

        fig = go.Figure()

        fig.update_layout(
            plot_bgcolor='white',    # Background of the plotting area
            paper_bgcolor='white'    # Background of the entire figure
        )

        if show_grid:
            fig.update_xaxes(title_text="X")
            fig.update_yaxes(title_text="Y")
        else:
            fig.update_layout(
                xaxis=dict(
                    showgrid=False,    # Remove grid lines
                    showticklabels=False,  # Remove tick labels
                    showline=False,    # Remove axis line
                    zeroline=False     # Remove zero line
                ),
                yaxis=dict(
                    showgrid=False,
                    showticklabels=False,
                    showline=False,
                    zeroline=False
                )
            )
        self.fragments = parse_dna_structure(self.rna, self.structure)
        self.get_coords()
        self.draw_active_site(fig)

        fig.write_image(filename)
