# Bidirectional DC Bus EV Charging Architecture Simulation

**Independent Technical Project | 2026**  
**Author:** Debopriya Das  
**Repository:** Bidirectional DC Bus EV Charging Simulation  

## 1. Aim of the Project

This independent technical project studies a simplified bidirectional EV charging architecture with a grid-side input, converter stage, DC bus and vehicle-side battery/load. The aim is to analyse system-level behaviour relevant to high-power EV charging, distributed DC systems and bidirectional charging research.

The project was developed as preparation for doctoral research in bidirectional wireless power transfer, EV charging architecture analysis, reliability monitoring and prototype-oriented power-system research.

This is a simplified simulation study. It does not claim to represent a validated industrial EV charger or a full wireless power transfer hardware model.

## 2. System Architecture

The simulated architecture consists of four main blocks:

1. Grid-side input  
2. Converter stage  
3. DC bus / DC link  
4. Vehicle-side battery or load  

The model considers bidirectional power flow. In the first scenario, power flows from the grid-side system toward the vehicle battery during charging. In the second scenario, power flows from the vehicle side back toward the DC bus during discharging or grid-support operation.

The simplified architecture diagram is available in:

`figures/architecture_diagram.png`

## 3. Simulation Assumptions

The simulation uses the following simplified assumptions:

| Parameter | Value |
|---|---|
| DC bus nominal voltage | 800 V |
| Bus resistance | 0.015 ohm |
| Battery capacity | 500 kWh |
| Initial state of charge | 35% |
| Charging power | 200 kW |
| Discharging power | 80 kW |
| Ambient temperature | 25°C |
| Thermal resistance | 1.8°C/kW |
| Thermal time constant | 900 s |

The full assumptions file is available in:

`data/simulation_assumptions.csv`

## 4. Simulation Method

The simulation was implemented in Python using NumPy, pandas and Matplotlib. The model calculates:

- DC bus voltage behaviour
- Charging and discharging current
- Vehicle-side power-flow direction
- Converter efficiency assumption
- Estimated converter losses
- Basic thermal-loading trend
- State-of-charge behaviour

The full Python script is available in:

`src/simulate_dc_bus.py`

## 5. Results

### 5.1 DC Bus Voltage Response

The voltage response shows how the DC bus voltage changes under charging and discharging current conditions. The simplified model includes voltage drop based on current flow and bus resistance.

Output file:

`figures/voltage_response.png`

### 5.2 Current Response

The current plot shows the change in current direction between charging and discharging operation. Positive current represents charging behaviour, while negative current represents reverse power flow.

Output file:

`figures/current_response.png`

### 5.3 Bidirectional Power Flow

The power-flow plot shows two operating modes:

- Charging phase at 200 kW
- Discharging / grid-support phase at 80 kW

This supports system-level reasoning about bidirectional EV charging architectures and vehicle-grid interaction.

Output file:

`figures/power_flow_charging_discharging.png`

### 5.4 Efficiency-Loss Trend

The efficiency-loss plot estimates converter losses under different power conditions. Higher charging power creates higher estimated losses, while lower discharging power produces lower loss levels.

Output file:

`figures/efficiency_loss_trend.png`

### 5.5 Thermal-Loading Trend

The thermal-loading trend estimates how component temperature may rise due to converter losses. This is a simplified first-order approximation and is intended only for basic system-level interpretation.

Output file:

`figures/thermal_loading_trend.png`

## 6. Relevance to BiWPT and High-Power EV Charging Research

This project is relevant to the BiWPT Doctoral Network because it connects to several themes of the advertised PhD position:

- System-level analysis of EV charging architectures
- Distributed DC system behaviour
- Bidirectional charging and discharging scenarios
- Power-flow analysis
- Efficiency-loss estimation
- Basic thermal-management reasoning
- Reliability-aware infrastructure monitoring
- Prototype-oriented technical documentation

Although the project does not implement wireless power transfer hardware, it provides preparation for analysing the surrounding electrical and system-level architecture required for high-power bidirectional EV charging.

## 7. Limitations

This project uses simplified assumptions and should not be interpreted as an industrial-grade EV charging model. The following areas are not yet included:

- Detailed converter switching model
- Closed-loop converter control design
- Realistic battery electrochemical model
- High-fidelity thermal simulation
- Wireless charging pad design
- Magnetic coupling and misalignment modelling
- Fleet-level charging demand
- Experimental hardware validation

## 8. Possible Next Steps

Future work could extend this project by adding:

1. Closed-loop DC bus voltage control  
2. DC-DC converter control comparison  
3. Battery state-of-charge dependent charging behaviour  
4. More realistic thermal modelling  
5. Wireless charging pad misalignment sensitivity analysis  
6. Fleet-level charging demand simulation for heavy-duty electric vehicles  
7. Fault and anomaly detection using EV charging telemetry signals  

## 9. Tools Used

- Python  
- NumPy  
- pandas  
- Matplotlib  
- GitHub  
- Basic control systems and power electronics assumptions  

## 10. Summary

This project demonstrates a simplified but relevant system-level simulation of a bidirectional DC bus EV charging architecture. It supports preparation for research in high-power EV charging, distributed DC systems, bidirectional power flow, reliability monitoring and prototype-oriented system analysis.
