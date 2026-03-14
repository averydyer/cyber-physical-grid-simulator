# Cyber-Physical Power Grid Simulation

A Python-based simulation of a simplified electrical power grid used to study **cyber-physical failures, load redistribution, and cascading outages**.  

The project models interactions between **power substations and demand regions** to explore how failures or cyber attacks can propagate through critical infrastructure.

---

# Project Overview

Modern power grids are complex cyber-physical systems where failures in one component can propagate through interconnected infrastructure. This simulator models a simplified grid in order to demonstrate:

- substation overload conditions
- load redistribution across infrastructure
- cascading failure scenarios
- the impact of cyber attacks on grid stability

The simulation is intended as a **learning and analysis tool** for understanding resilience challenges in critical infrastructure.

---

# System Architecture

The simulation consists of three core components:

### Substation
Represents a power distribution node with:
- maximum power capacity
- current load
- operational status (online/offline)

Substations detect overload conditions and may shut down to prevent damage.

### Region
Represents a demand source (such as a city or facility).  
Each region distributes its load across connected substations.

### GridController
The central simulation engine that:
- resets loads
- distributes demand across substations
- monitors overload conditions
- handles shutdown events
- displays grid status

---

# Current Features

- Substation modeling (3 substations)
- Region demand modeling (4 regions)
- Load distribution across connected substations
- Substation overload detection and shutdown
- Grid controller simulation logic
- Terminal-based substation load visualization
- Cyber attack scenario simulation (substation shutdown)
- Grid resilience through dynamic load redistribution

---

# Example Simulation Behavior

The simulator demonstrates how failures propagate through interconnected systems.  

Example scenarios include:

- **Demand spikes** causing substation overload
- **Cyber attacks** disabling infrastructure
- **Load redistribution** preventing cascading failures

Detailed walkthroughs of these scenarios can be found in: simulation_analysis.md

This file contains:

- explanations of simulation scenarios
- step-by-step analysis of grid behavior
- terminal output examples
- cybersecurity implications of cascading failures

---

# Project Structure

- `cybergrid.py` – main simulation engine
- `simulation_analysis.md` – explanation of simulation scenarios and results

---

# Future Features

Planned improvements to the simulator include:

- Cascading failure detection and propagation across substations
- Critical infrastructure prioritization (e.g., water treatment plants vs residential regions)
- Logging system for grid events and attack scenarios
- Simulation timelines for multi-step grid evolution
- Resilience analysis to measure grid robustness under different attack conditions
- Configurable grid topology through external configuration files

---

# Educational Purpose

This project explores how **cybersecurity risks intersect with physical infrastructure systems**.  

Understanding cascading failures and resilience strategies is essential for protecting critical systems such as power grids, water treatment plants, and transportation infrastructure.

---

# Author

Avery Dyer