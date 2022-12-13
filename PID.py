def pid_control(kp, ki, kd, setpoint, actual_value, prev_error, prev_control_signal):
    error = setpoint - actual_value  # Calculate the error at time t
    control_signal = (kp * (error - prev_error)  # Proportional term
                      + ki * error  # Integral term
                      + kd * (error - 2 * prev_error + prev_control_signal))  # Derivative term
    return control_signal, error  # Return the control signal and the error for use in the next time step

# Example usage
prev_error = 8
prev_control_signal = 0
kp = 8
ki = 6
kd = 1.6
setpoint = 100
actual_value = 97

control_signal, error = pid_control(kp, ki, kd, setpoint, actual_value, prev_error, prev_control_signal)
print(f"Control signal: {control_signal}, error: {error}")


