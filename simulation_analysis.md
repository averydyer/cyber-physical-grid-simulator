# Simulation Scenarios and Output Analysis

---

## Scenario 1: Demand Spike Causing Cascading Failure

### Explanation

This output demonstrates how a **substation overload can trigger cascading failures across the grid**.

The demand of the region **City** was increased to **300 MW**. City is connected to substations **S1** and **S2**. Because load is distributed equally across connected substations, both **S1** and **S2** initially receive **150 MW** from City.

However, **S1 has a capacity of only 100 MW**, meaning it becomes overloaded when it receives 150 MW from City along with additional load from **Data Center**, another connected region.

Once S1 becomes overloaded, a **warning message is triggered** and the substation is automatically taken offline. The system then attempts to redistribute the load. Because **S2 is the only remaining active substation connected to City and Data Center**, it receives the full load from both regions.

This causes **S2 to overload**, triggering another shutdown. At this point, both **City** and **Data Center** no longer have any active substations connected to them, resulting in a **complete blackout** in both regions.

This example shows how **a single overload can propagate through the grid**, affecting infrastructure that may initially appear unrelated.

### Cybersecurity Implication

Cascading failures represent a major cybersecurity risk. A malicious actor could intentionally manipulate demand or disrupt a single substation, causing failures to propagate across multiple regions and substations.

---

### Output

Grid Status
S1 [OVERLOADED] 200/100 MW
S2 [████████████████████] 200/200 MW
S3 [█████████████████░░░] 130/150 MW

WARNING: S1 is overloaded and is being shut down

Grid Status
S1 [OFFLINE] 0/100 MW
S2 [OVERLOADED] 400/200 MW
S3 [█████████████████░░░] 130/150 MW

WARNING: S2 is overloaded and is being shut down
WARNING: all substations connected to City are offline
WARNING: all substations connected to Data Center are offline

Grid Status
S1 [OFFLINE] 0/100 MW
S2 [OFFLINE] 0/200 MW
S3 [█████████████████░░░] 130/150 MW

---

# Scenario 2: Cyber Attack Triggering Cascading Failure

### Explanation

In this scenario, the grid initially operates under **normal conditions**. All substations are active and none are overloaded.

However, a **cyber attack disables substation S1**, causing it to go offline. Because **City** and **Data Center** are connected to S1 and S2, their load is automatically redistributed to **S2**.

This redistribution pushes S2 beyond its capacity, causing it to overload and subsequently shut down.

As a result, both **City** and **Data Center** lose access to any active substations and experience a **complete power outage**.

This scenario highlights how **a single cyber attack on one substation can cascade into failures across multiple regions**, amplifying the impact of the attack.

### Cybersecurity Implication

This demonstrates how attackers can cause **large-scale disruption with minimal effort**. By targeting a single piece of infrastructure, they may trigger cascading failures affecting multiple substations and regions.

---

### Output

Grid Status
S1 [████████████████████] 100/100 MW
S2 [█████████████░░░░░░░] 100/150 MW
S3 [█████████████████░░░] 130/150 MW

WARNING: cyber attack on S1

Grid Status
S1 [OFFLINE] 0/100 MW
S2 [OVERLOADED] 200/150 MW
S3 [█████████████████░░░] 130/150 MW

WARNING: S2 is overloaded and is being shut down
WARNING: all substations connected to City are offline
WARNING: all substations connected to Data Center are offline

Grid Status
S1 [OFFLINE] 0/100 MW
S2 [OFFLINE] 0/150 MW
S3 [█████████████████░░░] 130/150 MW

---

# Scenario 3: Load Redistribution for Grid Resilience

### Explanation

This scenario demonstrates the **newly implemented load redistribution function**, which attempts to rebalance load when a substation becomes overloaded.

Before redistribution, **S2 is overloaded** because it is receiving load from **City**, **Data Center**, and **Water Treatment Plant** that exceeds its capacity.

During redistribution, the system identifies that **Water Treatment Plant is also connected to S3**, which has available capacity. A portion of Water Treatment Plant's load is therefore transferred from **S2 to S3**.

This transfer eliminates the overload at S2 and stabilizes the system.

After redistribution:

- **S2 is operating exactly at capacity**
- **S3 absorbs the additional load**
- No substations are overloaded

### Cybersecurity Implication

The redistribution function introduces **grid resilience mechanisms**. By dynamically balancing load, the system becomes more resistant to cascading failures and makes it more difficult for attackers to trigger widespread outages.

A key aspect of cybersecurity is **engineering systems that remain stable even when components fail or are attacked**.

---

### Output

 BEFORE REDISTRIBUTION:

Grid Status
-----------------------------------------
S1     [███████████████░░░░░] 150/200 MW
S2     [OVERLOADED]           165/150 MW
S3     [█████████████░░░░░░░] 65/100  MW
-----------------------------------------


 AFTER REDISTRIBUTION:

Grid Status
-----------------------------------------
S1     [███████████████░░░░░] 150/200 MW
S2     [████████████████████] 150/150 MW
S3     [████████████████░░░░] 80/100  MW
-----------------------------------------

---