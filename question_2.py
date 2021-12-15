# Author: SMR (AMDG) 12/15/21

# Initial Input Statements
int_velo1=input("Enter the Initial Velocity: ")
final_velo1=input("Enter the Final Velocity: ")
time1=input("Enter the time: ")

# Converting to Integers
int_velo2= int(int_velo1)
final_velo2=int(final_velo1)
time2=int(time1)

# Calculating the Average Acceleration
avg_acceleration= ((final_velo2-int_velo2)/(time2))

# Final Statement
print("The average acceleration is {0}." .format(avg_acceleration))