**************************************************************************************************
This output shows how a substation overload can lead
to cascading failures. The demand of the region "City"
was first increased to 300 MW. City is connected to 
substations S1 and S2. Because of equal load distribution,
S1 and S2 both received 150 MW from City. S1 was then 
overloaded because its capacity is only 100 MW, but it
was receiving 150 MW from City along with whatever amount
it was receiving from Data Center, another connected region.
A warning message then appeared stating that S1 is being
taken offline due to being overloaded. The loads were then
redistributed which caused S2 to overload, because it was
now receiving the full load of both City and Data Center.
Three warning messages were then displayed, stating that
S2 has been taken offline due to overload, and City and 
Data Center now have no active substations to receive their
load. This results in a full blackout in both the City and
the Data Center. The final grid status is then shown, where
S1 and S2 are both offline.

This test displays how one overload can affect multiple 
different substations and regions that at first do not seem
to be connected. All that was changed was an increase in 
demand from City, but this caused S1 and S2 to be taken offline
which resulted in City and Data Center experiencing blackout.
Cascading failures are a real threat when it comes to cyber
security, as a hacker could shut down multiple substations/regions
while only needing to disrupt one.

Output:

Grid Status
-----------------------------------------
S1     [OVERLOADED]           200/100 MW
S2     [████████████████████] 200/200 MW
S3     [█████████████████░░░] 130/150 MW
-----------------------------------------

WARNING: S1 is overloaded and is being shut down

Grid Status
-----------------------------------------
S1     [OFFLINE]              0/100   MW
S2     [OVERLOADED]           400/200 MW
S3     [█████████████████░░░] 130/150 MW
-----------------------------------------

WARNING: S2 is overloaded and is being shut down
WARNING: all substations connected to City are offline
WARNING: all substations connected to Data Center are offline

Grid Status
-----------------------------------------
S1     [OFFLINE]              0/100   MW
S2     [OFFLINE]              0/200   MW
S3     [█████████████████░░░] 130/150 MW
-----------------------------------------
**************************************************************************************************
**************************************************************************************************
Here, at first every region is powered and every substation
is active and not overloaded. However, a cyber attack on S1 causes
it to go offline. This means the loads of City and Data Center are
redistributed to S2, which overloads it and causes it to shut down.

This attack on S1 causes S2 to also fail, and there is a blackout
in both City and Data Center

Output:

Grid Status
-----------------------------------------
S1     [████████████████████] 100/100 MW
S2     [█████████████░░░░░░░] 100/150 MW
S3     [█████████████████░░░] 130/150 MW
-----------------------------------------

WARNING: cyber attack on S1

Grid Status
-----------------------------------------
S1     [OFFLINE]              0/100   MW
S2     [OVERLOADED]           200/150 MW
S3     [█████████████████░░░] 130/150 MW
-----------------------------------------

WARNING: S2 is overloaded and is being shut down
WARNING: all substations connected to City are offline
WARNING: all substations connected to Data Center are offline

Grid Status
-----------------------------------------
S1     [OFFLINE]              0/100   MW
S2     [OFFLINE]              0/150   MW
S3     [█████████████████░░░] 130/150 MW
-----------------------------------------
**************************************************************************************************