# Bidirectional DC Bus EV Charging Simulation

This independent technical project explores a simplified bidirectional EV charging architecture with a grid-side input, converter stage, DC bus and vehicle-side load.

The aim is to study system-level behaviour relevant to high-power EV charging, distributed DC systems and bidirectional charging research.

## Scope

This is a simplified simulation study, not a hardware implementation. The project focuses on:

- DC bus voltage behaviour
- Charging and discharging power-flow scenarios
- Converter efficiency assumptions
- Estimated losses under different power levels
- Basic thermal-load trend estimation
- System-level bottleneck discussion

## Relevance

This project supports preparation for research in bidirectional wireless power transfer, high-power EV charging architectures, distributed DC systems, reliability monitoring and prototype-oriented system analysis.

## Tools

- Python
- NumPy
- pandas
- Matplotlib
- Jupyter Notebook
- Basic control systems and power electronics assumptions

## Planned Outputs

- Architecture diagram
- Voltage and current response plot
- Charging vs discharging power-flow plot
- Efficiency-loss and thermal-loading trend
- Short technical report

- ## Generated Results

The simulation generates:

- `figures/architecture_diagram.png`
- `figures/voltage_response.png`
- `figures/current_response.png`
- `figures/power_flow_charging_discharging.png`
- `figures/efficiency_loss_trend.png`
- `figures/thermal_loading_trend.png`
- `data/simulation_results.csv`
- `data/simulation_assumptions.csv`

## Key Interpretation

The simulation compares charging and discharging behaviour in a simplified bidirectional DC bus architecture. It tracks DC bus voltage, current direction, power-flow behaviour, estimated converter losses and basic thermal-loading trends.

The purpose is to support system-level reasoning for high-power EV charging, distributed DC systems, bidirectional charging and reliability-aware infrastructure analysis.
