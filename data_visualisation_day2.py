#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt 

#sample data for energy  consumption over 6 month (in mwh)
import matplotlib.pyplot as plt

#Sample data for energy consumption over 6 months (in Mich)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
energy_consumption= [1200, 1300, 1100, 1500, 1400, 1600]


#Create a Line plot
plt.plot(months, energy_consumption, marker='o', color='b', linestyle='--')

#Add titles and Labels
plt.title('Energy Consumption Over 6 Months')
plt.xlabel('Month')
plt.ylabel('Energy Consumption (MWh)')
plt.show()


# In[7]:


import matplotlib.pyplot as plt
months = ['Jan','Feb','Mar','Apr','May','Jun']
energy_consumption = [1200,1300,1100,1500,1400,1600]

plt.bar(months,energy_consumption,color='b')

plt.title('Energy Consumption Over 6 Months')
plt.xlabel('Month')
plt.ylabel('Energy Consumption (MWh)')
plt.show()


# In[9]:


import matplotlib.pyplot as plt

# Data for energy consumption over 6 months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
energy_consumption = [1200, 1300, 1100, 1500, 1400, 1600]

# Create a pie chart
plt.figure(figsize=(8, 8))  # Set the figure size
plt.pie(
    energy_consumption, 
    labels=months, 
    autopct='%1.1f%%',  # Show percentages
    startangle=90,  # Start angle at 90 degrees
    colors=['lightblue', 'lightgreen', 'orange', 'pink', 'violet', 'yellow'],  # Custom colors
    explode=[0, 0.1, 0, 0, 0, 0]  # Highlight February slightly
)

# Add a title
plt.title('Energy Consumption Distribution Over 6 Months', fontsize=14)

# Show the plot
plt.show()


# In[11]:


import matplotlib.pyplot as plt

# Data for energy consumption over 6 months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
energy_consumption = [1200, 1300, 1100, 1500, 1400, 1600]

# Assign numeric values to months for the x-axis
month_numbers = range(1, len(months) + 1)

# Create a scatter plot
plt.scatter(month_numbers, energy_consumption, color='purple', s=100, edgecolors='black')

# Add labels and title
plt.title('Energy Consumption Over 6 Months', fontsize=14)
plt.xlabel('Months', fontsize=12)
plt.ylabel('Energy Consumption (MWh)', fontsize=12)

# Replace numeric x-ticks with month names
plt.xticks(month_numbers, months)

# Show the plot
plt.show()


# In[13]:


# Sample data for energy consumption and carbon emissions
carbon_emissions = [400, 500, 450, 300, 350, 550] # in kg CO2

#Create a scatter plot
plt.scatter(energy_consumption, carbon_emissions, color='red')

#Add titles and Labels
plt.title('Energy Consumption vs Carbon Emissions')
plt.xlabel('Energy Consumption (MWh)')
plt.ylabel('Carbon Emissions (kg CO2)')
plt.show()


# In[15]:


import matplotlib.pyplot as plt
import numpy as np

# Sample data (e.g., energy consumption values)
data = [1200, 1300, 1100, 1500, 1400, 1600, 1800, 2000, 2200, 2300, 2500]

# Create a histogram with 5 bins
plt.hist(data, bins=5, color='b', edgecolor='black')

# Add titles and labels
plt.title('Energy Consumption Distribution')
plt.xlabel('Energy Consumption (MWh)')
plt.ylabel('Frequency')

# Show the plot
plt.show()



# In[27]:


#histogram 
import matplotlib.pyplot as plt 
import numpy as np
data = np.random.normal(170,10,250)
plt.hist(data, bins=30);
plt.show()


# In[29]:


import numpy as np 
import matplotlib.pyplot as plt 

#y-axis values 
y1=[2,3,4.5]

#y-axis values
y2=[1,1.5,5]

#function to plot 
plt.plot(y1)
plt.plot(y2)

plt.legend(["blue","green"],loc="lower right")

plt.show()

