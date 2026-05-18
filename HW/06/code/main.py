import numpy as np

import matplotlib.pyplot as plt


def gauss_newton(residual_func, jacobian_func, c0, tol=1e-6, max_iterations=100):
    """
    @Implements the Gauss-Newton method for non-linear least squares.
    @Parameters:
        residual_func (callable): Function that returns the residual vector r(c).
        jacobian_func (callable): Function that returns the Jacobian matrix J(c).
        c0 (array-like): Initial guess for the parameters c.
        tol (float): Tolerance for the stopping criterion.
        max_iterations (int): Maximum number of iterations to perform.
        
    @Returns: np.ndarray: The optimized parameters c.
    """
    # Initialize starting point as a float array
    c = np.array(c0, dtype=float)
    
    for k in range(max_iterations):
        # Compute the residual vector
        r = residual_func(c)
        
        # Compute the Jacobian
        A = jacobian_func(c)
        
        # Solve the normal equations for the Gauss-Newton step delta_c:
        # A^T A \delta c = -A^T r
        A_T = A.T
        normal_matrix = A_T @ A
        normal_vector = -A_T @ r
        
        delta_c = np.linalg.solve(normal_matrix, normal_vector)
        
        # Update
        c = c + delta_c
        
        # Stop when ||\delta c|| is sufficiently small
        if np.linalg.norm(delta_c) < tol:
            print(f"Converged in {k + 1} iterations.")
            break
    else:
        print("Warning: Reached maximum iterations without converging.")
        
    return c


if __name__ == "__main__":
    # Fit the model: f(t, c) = c0 * exp(c1 * t)
    # Sample data
    t_data = np.array([1, 2, 3, 4, 5])
    y_data = np.array([1.2, 2.8, 5.1, 8.9, 14.7])
    
    # Define the residual function: r(c) = Model(c) - Data
    def calculate_residual(c):
        return c[0] * np.exp(c[1] * t_data) - y_data

    # Define the Jacobian matrix function
    def calculate_jacobian(c):
        # The Jacobian has dimensions (number_of_data_points) x (number_of_parameters)
        J = np.empty((len(t_data), 2))
        # Partial derivative wrt c0: exp(c1 * t)
        J[:, 0] = np.exp(c[1] * t_data)
        # Partial derivative wrt c1: c0 * t * exp(c1 * t)
        J[:, 1] = c[0] * t_data * np.exp(c[1] * t_data)
        
        return J

    c_initial = [1.0, 1.0]

    c_optimized = gauss_newton(calculate_residual, calculate_jacobian, c_initial)
    
    print("\nInitial guess c(0):", c_initial)
    print("Optimized parameters c:", c_optimized)

    # Plot the data points and fitted curve
    t_fit = np.linspace(t_data.min(), t_data.max(), 300)
    y_fit = c_optimized[0] * np.exp(c_optimized[1] * t_fit)

    plt.style.use("seaborn-v0_8-whitegrid")
    fig, ax = plt.subplots(figsize=(10, 6), dpi=120)

    ax.scatter(
        t_data,
        y_data,
        s=60,
        color="#27d643",
        edgecolor="white",
        linewidth=0.8,
        alpha=0.9,
        label="Data points",
        zorder=3,
    )
    ax.plot(
        t_fit,
        y_fit,
        color="#1f77b4",
        linewidth=2.5,
        label="Fitted curve",
        zorder=2,
    )

    ax.set_xlabel("t", fontsize=12)
    ax.set_ylabel("y", fontsize=12)
    ax.set_title("Gauss-Newton Exponential Fit", fontsize=15, weight="bold", pad=12)
    ax.legend(frameon=True, fancybox=True, framealpha=0.95, shadow=True)
    ax.grid(True, linestyle="--", linewidth=0.6, alpha=0.7)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    fig.tight_layout()
    fig.savefig("gauss_newton_exponential_fit.png", dpi=300, bbox_inches="tight")
