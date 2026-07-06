import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Simplified Bidirectional DC Bus EV Charging Simulation
# ---------------------------------------------------------
# This is a system-level educational simulation, not a
# validated industrial charger or WPT hardware model.
# ---------------------------------------------------------

os.makedirs("figures", exist_ok=True)
os.makedirs("data", exist_ok=True)

# Simulation settings
time_min = np.linspace(0, 60, 601)
dt_h = (time_min[1] - time_min[0]) / 60

dc_bus_nominal_v = 800
bus_resistance_ohm = 0.015
battery_capacity_kwh = 500
initial_soc = 0.35

ambient_temp_c = 25
thermal_resistance_c_per_kw = 1.8
thermal_time_constant_s = 900

# Scenario:
# 0 to 30 min: charging at 200 kW
# 30 to 60 min: discharging / grid-support at 80 kW
vehicle_power_kw = np.where(time_min <= 30, 200, -80)

# Converter efficiency model
load_fraction = np.abs(vehicle_power_kw) / 350
efficiency = 0.965 - 0.02 * load_fraction**2
efficiency = np.clip(efficiency, 0.90, 0.98)

# Electrical behaviour
current_a = vehicle_power_kw * 1000 / dc_bus_nominal_v
dc_bus_voltage_v = dc_bus_nominal_v - current_a * bus_resistance_ohm

loss_kw = np.abs(vehicle_power_kw) * (1 / efficiency - 1)

# SOC calculation
soc = [initial_soc]
for p in vehicle_power_kw[:-1]:
    soc.append(soc[-1] + (p * dt_h) / battery_capacity_kwh)
soc = np.clip(np.array(soc), 0, 1)

# Simple thermal trend
temperature_c = [ambient_temp_c]
for loss in loss_kw[:-1]:
    target_temp = ambient_temp_c + loss * thermal_resistance_c_per_kw
    dt_s = dt_h * 3600
    next_temp = temperature_c[-1] + (target_temp - temperature_c[-1]) * dt_s / thermal_time_constant_s
    temperature_c.append(next_temp)

temperature_c = np.array(temperature_c)

# Save results
results = pd.DataFrame({
    "time_min": time_min,
    "vehicle_power_kw": vehicle_power_kw,
    "dc_bus_voltage_v": dc_bus_voltage_v,
    "current_a": current_a,
    "efficiency": efficiency,
    "loss_kw": loss_kw,
    "temperature_c": temperature_c,
    "soc": soc
})

results.to_csv("data/simulation_results.csv", index=False)

# Save assumptions
assumptions = pd.DataFrame({
    "parameter": [
        "DC bus nominal voltage",
        "Bus resistance",
        "Battery capacity",
        "Initial SOC",
        "Charging power",
        "Discharging power",
        "Ambient temperature",
        "Thermal resistance",
        "Thermal time constant"
    ],
    "value": [
        "800 V",
        "0.015 ohm",
        "500 kWh",
        "35%",
        "200 kW",
        "80 kW",
        "25 C",
        "1.8 C/kW",
        "900 s"
    ]
})

assumptions.to_csv("data/simulation_assumptions.csv", index=False)

# ---------------------------------------------------------
# Plot 1: Architecture diagram
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 3))
ax.axis("off")

boxes = [
    (0.05, 0.45, "Grid-side\nInput"),
    (0.28, 0.45, "Converter\nStage"),
    (0.51, 0.45, "DC Bus\n800 V"),
    (0.74, 0.45, "Vehicle-side\nBattery / Load")
]

for x, y, label in boxes:
    ax.text(
        x, y, label,
        ha="center", va="center",
        bbox=dict(boxstyle="round,pad=0.5", edgecolor="black", facecolor="white")
    )

for x1, x2 in [(0.13, 0.23), (0.36, 0.46), (0.59, 0.69)]:
    ax.annotate(
        "",
        xy=(x2, 0.45),
        xytext=(x1, 0.45),
        arrowprops=dict(arrowstyle="<->", lw=1.5)
    )

ax.text(
    0.5, 0.15,
    "Simplified bidirectional power-flow architecture for system-level EV charging analysis",
    ha="center"
)

plt.tight_layout()
plt.savefig("figures/architecture_diagram.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# Plot 2: Voltage and current response
# ---------------------------------------------------------
plt.figure(figsize=(9, 5))
plt.plot(time_min, dc_bus_voltage_v, label="DC bus voltage (V)")
plt.xlabel("Time (minutes)")
plt.ylabel("Voltage (V)")
plt.title("DC Bus Voltage Response")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("figures/voltage_response.png", dpi=300)
plt.close()

plt.figure(figsize=(9, 5))
plt.plot(time_min, current_a, label="Current (A)")
plt.axhline(0, linestyle="--")
plt.xlabel("Time (minutes)")
plt.ylabel("Current (A)")
plt.title("Charging and Discharging Current")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("figures/current_response.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# Plot 3: Power-flow behaviour
# ---------------------------------------------------------
plt.figure(figsize=(9, 5))
plt.plot(time_min, vehicle_power_kw, label="Vehicle-side power (kW)")
plt.axhline(0, linestyle="--")
plt.xlabel("Time (minutes)")
plt.ylabel("Power (kW)")
plt.title("Bidirectional Power-Flow Scenario")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("figures/power_flow_charging_discharging.png", dpi=300)
plt.close()

# ---------------------------------------------------------
# Plot 4: Efficiency loss and thermal trend
# ---------------------------------------------------------
plt.figure(figsize=(9, 5))
plt.plot(time_min, loss_kw, label="Estimated converter loss (kW)")
plt.xlabel("Time (minutes)")
plt.ylabel("Loss (kW)")
plt.title("Estimated Efficiency Loss")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("figures/efficiency_loss_trend.png", dpi=300)
plt.close()

plt.figure(figsize=(9, 5))
plt.plot(time_min, temperature_c, label="Estimated component temperature (C)")
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (C)")
plt.title("Basic Thermal-Loading Trend")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("figures/thermal_loading_trend.png", dpi=300)
plt.close()

print("Simulation completed successfully.")
print("Generated files:")
print("- data/simulation_results.csv")
print("- data/simulation_assumptions.csv")
print("- figures/architecture_diagram.png")
print("- figures/voltage_response.png")
print("- figures/current_response.png")
print("- figures/power_flow_charging_discharging.png")
print("- figures/efficiency_loss_trend.png")
print("- figures/thermal_loading_trend.png")
