"""Compare an exact separable-ODE solution with Euler's method."""

import math


def euler(f, t0, y0, step, number_of_steps):
    """Return the time points and Euler approximations."""
    times = [t0]
    values = [y0]

    for index in range(number_of_steps):
        time = t0 + index * step
        value = values[-1] + step * f(time, values[-1])
        times.append(t0 + (index + 1) * step)
        values.append(value)

    return times, values


def derivative(t, y):
    """Right-hand side of dy/dt = -2y."""
    return -2 * y


def exact_solution(t):
    """Exact solution for y(0) = 1."""
    return math.exp(-2 * t)


def main():
    initial_time = 0.0
    initial_value = 1.0
    final_time = 1.0
    step = 0.2
    number_of_steps = round((final_time - initial_time) / step)

    times, approximations = euler(
        derivative, initial_time, initial_value, step, number_of_steps
    )

    print("EDO: y' = -2y, condición inicial: y(0) = 1")
    print(f"Intervalo: [{initial_time}, {final_time}], paso h = {step}")
    print(f"{'t':>5} {'Euler':>14} {'Exacta':>14} {'Error absoluto':>16}")

    for time, approximation in zip(times, approximations):
        exact = exact_solution(time)
        error = abs(exact - approximation)
        print(f"{time:5.1f} {approximation:14.8f} {exact:14.8f} {error:16.8f}")


if __name__ == "__main__":
    main()