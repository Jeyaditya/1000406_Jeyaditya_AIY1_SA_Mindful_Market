# 1000406_Jeyaditya_AIY1_SA_Mindful_Market

# Mindful Market – Sustainable Shopping Tracker

## Introduction

Mindful Market is a web application built using Streamlit that helps users reflect on the environmental impact of their shopping habits. The application allows users to record their purchases, estimate carbon emissions, and track their sustainability progress over time.

The goal of this project is not to provide exact scientific measurements, but to encourage awareness, responsibility, and better decision-making when it comes to everyday consumption.

---

[Link to access Mindful Market] (https://1000406-jeyaditya-aiy1-sa-mindfulmarket.streamlit.app/)

## Purpose of the Project

This project was created to:

- Promote environmentally responsible shopping behavior
- Help users understand how product choices and shipping distance affect carbon emissions
- Provide meaningful feedback through visuals and progress indicators
- Present sustainability concepts in a simple, interactive way

---

## Key Features

### Purchase Entry System

Users can log purchases by providing:

- Product category
- Price
- User country and district
- Shipper country and district

Based on this information, the application estimates:

- Total CO₂ impact
- Transport distance between countries
- Whether the purchase is eco-friendly

---

### Country and District Selection

- Separate dropdown menus for country and district selection
- Improves realism and accuracy in distance calculations
- Supports multiple countries with predefined districts

---

### Eco Score Calculation

- A dynamic eco score is calculated based on cumulative CO₂ impact
- The score updates automatically after every purchase
- The score ranges from 0 to 100, where higher values indicate better sustainability

---

### Mascot Feedback System

- An animated mascot reacts to the user’s eco score
- Different expressions reflect poor, moderate, or good sustainability performance
- The mascot displays short messages that guide and encourage the user

---

### Eco Badges

- Users earn eco badges based on their eco score
- Badges act as milestones and motivation for improvement
- Badge status updates automatically as purchases are added

---

### Purchase History

- Displays all recorded purchases in a clear table format
- Includes:
  - Product information
  - Price
  - Estimated CO₂ impact
  - Transport distance
  - Eco-friendly classification
  - Mascot reaction per purchase
- Built with safeguards to prevent data errors from older sessions

---

## Eco-Friendly Criteria

A purchase is classified as eco-friendly when:

- The total estimated CO₂ impact is less than or equal to 50 kg

This threshold can be adjusted in the code for future refinements.

---

## Technology Used

- Python
- Streamlit
- Pandas
- Standard Python libraries (math, datetime, os)
- Embedded CSS for simple animations

---

## Credits
* Student name- Jeyaditya
* CRS facilitator- Syed Ali Beema S
* School name- Jain Vidyalaya IB World School
