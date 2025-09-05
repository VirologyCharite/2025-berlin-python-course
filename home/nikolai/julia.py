import marimo

__generated_with = "0.14.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap
    import matplotlib.colors as mcolors

    return ListedColormap, mcolors, np, plt


@app.function
def map(z, factor=2, offset=2):
    return z**factor+offset


@app.cell
def _(np):
    def make_grid(real_range, img_range, real_points, img_points):
        real_points = np.linspace(*real_range, num=real_points)
        imag_points = np.linspace(*img_range, num=img_points)
        real_grid, imag_grid = np.meshgrid(real_points, imag_points)
        return real_grid + imag_grid * 1j
    
    return (make_grid,)


@app.cell
def _(np):
    def map_grid(power, offset, grid, R, n_iter):
        R_sqaure = R**2
        out = np.zeros(shape=grid.shape)
        for i, row in enumerate(grid):
            for j, z in enumerate(row):
                iter = 0
                while iter < n_iter and np.square(z) < R_sqaure:
                    z = z**power + offset
                    iter += 1
                else:
                    if iter == n_iter:
                        out[i][j] = -1
                    else:
                        out[i][j] = iter
            
        return out
        
    return (map_grid,)


@app.cell
def _(Z):
    Z
    return


@app.cell
def _(ListedColormap, mcolors, np, plt):
    def plot_result(Z):
        Z_masked = np.ma.masked_where(Z == -1, Z)
    
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
        # Plot 1: Using masked array
        im1 = ax1.imshow(Z_masked, cmap='viridis', origin='lower', extent=[-2, 2, -2, 2])
        ax1.imshow(np.ma.masked_where(Z != -1, Z), cmap=ListedColormap(['black']), 
                   origin='lower', extent=[-2, 2, -2, 2])
        ax1.set_title('Method 1: Masked Array')
        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        plt.colorbar(im1, ax=ax1)
    
        # Method 2: Custom colormap
        # Create custom colormap where -1 maps to black
        def create_custom_cmap(base_cmap='viridis', special_value=-1, special_color='black'):
            # Get the base colormap
            base = plt.cm.get_cmap(base_cmap)
        
            # Create array of colors
            colors = base(np.linspace(0, 1, 256))
        
            # Create custom colormap
            cmap = ListedColormap(colors)
        
            # Set color for values outside normal range
            cmap.set_bad(special_color)
        
            return cmap
    
        # Normalize data excluding -1 values
        data_for_norm = Z[Z != -1]
        vmin, vmax = data_for_norm.min(), data_for_norm.max()
    
        # Create custom normalization
        norm = mcolors.Normalize(vmin=vmin, vmax=vmax)
    
        # Plot with custom handling
        Z_plot = Z.copy()
        Z_plot = np.ma.masked_where(Z == -1, Z_plot)
    
        im2 = ax2.imshow(Z_plot, cmap='viridis', norm=norm, origin='lower', extent=[-2, 2, -2, 2])
        ax2.imshow(np.ma.masked_where(Z != -1, np.ones_like(Z)), 
                   cmap=ListedColormap(['black']), origin='lower', extent=[-2, 2, -2, 2])
        ax2.set_title('Method 2: Custom Normalization')
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        plt.colorbar(im2, ax=ax2)
    
        plt.tight_layout()
        plt.show()
    
        # Method 3: Simple approach if you just want one plot
        plt.figure(figsize=(8, 6))
    
        # Mask the -1 values
        Z_masked = np.ma.masked_where(Z == -1, Z)
    
        # Plot the main data
        plt.imshow(Z_masked, cmap='viridis', origin='lower', extent=[-2, 2, -2, 2])
    
        # Overlay black color for -1 values
        plt.imshow(np.ma.masked_where(Z != -1, Z), cmap=ListedColormap(['black']), 
                   origin='lower', extent=[-2, 2, -2, 2])
    
        plt.colorbar(label='Value')
        plt.title('Heatmap with -1 Values in Black')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()
    return


@app.cell
def _(mo):
    # Create and display all sliders at once
    exp, c_real, c_img, xmin, xmax, ymin, ymax, count, R, iter = (
        mo.ui.slider(1, 10, label="exp", step=0.01, debounce=True),
        mo.ui.slider(-10, 10, label="c_real", step=0.01, debounce=True), 
        mo.ui.slider(-10, 10, label="c_img", step=0.01, debounce=True),
        mo.ui.slider(-4, 4, label="xmin", step=0.01, debounce=True),
        mo.ui.slider(-4, 4, label="xmax", step=0.01, debounce=True),
        mo.ui.slider(-4, 4, label="ymin", step=0.01, debounce=True),
        mo.ui.slider(-4, 4, label="ymax", step=0.01, debounce=True),
        mo.ui.slider(100, 2000, label="count", step=10, debounce=True),
        mo.ui.slider(1, 10, label="R", debounce=True),
        mo.ui.slider(100, 4000, label="iter", step=100, debounce=True),
    )

    return R, c_img, c_real, count, exp, iter, xmax, xmin, ymax, ymin


@app.cell
def _(R, c_img, c_real, count, exp, iter, xmax, xmin, ymax, ymin):
    print(
    exp.value,
        c_real.value,
        c_img.value, 
        xmin.value,
        xmax.value,
        ymin.value,
        ymax.value,
        count.value,
        R.value, 
        iter.value
    )
    return


@app.cell
def _(
    R,
    c_img,
    c_real,
    count,
    exp,
    iter,
    make_grid,
    map_grid,
    xmax,
    xmin,
    ymax,
    ymin,
):
    Z = map_grid(
        exp.value, 
        c_real.value+1j*c_img.value, 
        make_grid(
            (xmin.value,xmax.value),
            (ymin.value,ymax.value),
            count.value,
            count.value
        ), 
        R.value, 
        iter.value
    )
    return (Z,)


@app.cell
def _(ListedColormap, Z, np, plt):
    Z_masked = np.ma.masked_where(Z == -1, Z)
    
    fig, ax1 = plt.subplots(1, 1, figsize=(12, 5))

    # Plot 1: Using masked array
    im1 = ax1.imshow(Z_masked, cmap='viridis', origin='lower', extent=[-2, 2, -2, 2])
    ax1.imshow(np.ma.masked_where(Z != -1, Z), cmap=ListedColormap(['black']), 
               origin='lower', extent=[-2, 2, -2, 2])
    ax1.set_title('Method 1: Masked Array')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    plt.colorbar(im1, ax=ax1)

    plt.show()
    return


@app.cell
def _(R, c_img, c_real, count, exp, iter, xmax, xmin, ymax, ymin):
    [exp, c_real, c_img, xmin, xmax, ymin, ymax, count, R, iter]
    return


if __name__ == "__main__":
    app.run()
