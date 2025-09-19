---
title: "Pune's Transportation Problem: Overcrowded PMPML Buses"
date: 2024-09-19
permalink: /posts/2024/09/pune-transportation-analysis/
tags:
  - urban planning
  - public transport
  - data analysis
  - pune
  - transportation policy
excerpt: >
  <blockquote style="border-left: 4px solid #28a745; padding-left: 1rem; font-style: italic; margin: 1rem 0; background-color: #f8fff8; padding: 1rem; color: #1b1b1b;">
  An in-depth analysis of Pune's public transportation challenges, examining the causes of 
  overcrowded PMPML buses and proposing data-driven solutions for improving urban mobility 
  in one of India's fastest-growing metropolitan areas.
  </blockquote>
---

# 1. Introduction

Pune is a large city and along with its satellite city, Pimpri-Chinchwad, have an estimated population of 7 million people. The transport needs for the two cities and various villages surrounding the cities are immense. Pune, like every other city, faces the monumental task of ensuring that people move from one place to another efficiently. 

Plenty of people use two-wheelers and cars but just as many if not more use public transport especially buses and metro. However, the existing bus and metro systems are inadequate. While metro line 1 and 2 have been built and are attracting an increasing number of passengers, metro can only serve the major hubpoints. The last mile connectivity within public transport still depends on buses. 

The population of Pune has exploded over the last few years. This combines with the increase in two- and four-wheelers which end up crowding the roads. This report will detail the problems, their main causes, and the solutions can be undertaken to solve this problem.

# 2. A Deep Dive into the Problem

Pune's population has exploded over the past couple of years. We can see in the table and chart below that Pune's population has increased from 12 lakhs to over an estimated 44.3 lakhs. There is a steep increase in population for Pune and has reached an estimated 45 lakhs in 2024.

<div class="table-container">
  <table>
    <colgroup>
      <col style="width: 50%;">
      <col style="width: 50%;">
    </colgroup>
    <thead>
      <tr>
        <th>Year</th>
        <th>Population (lakhs)</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>1981</td><td>12.0</td></tr>
      <tr><td>1991</td><td>18.7</td></tr>
      <tr><td>2001</td><td>25.4</td></tr>
      <tr><td>2011</td><td>31.3</td></tr>
      <tr><td>2024*</td><td>44.3</td></tr>
    </tbody>
  </table>
</div>

**Table 1: Population of Pune (lakhs), 1981 to 2011**<br>
_Sources: 1981 to 2011 data is from 1981 to 2011 census. The 2024 data is estimated by [Census 2011](https://www.census2011.co.in/)._

![Pune population](/assets/posts/pune_transportation_analysis/Pune population chart.png){: width="900" height="500"}

**Figure 1: Population of Pune (lakhs), 1981 to 2011**<br>
_Sources: 1981 to 2011 data is from 1981 to 2011 census. The 2024 data is estimated by [Census 2011](https://www.census2011.co.in/)._

Due to the increasing population, the population density of both cities has also increased. The only anomaly is Pune's population density decreasing but this is because of the inclusion of more than 20 villages within the Pune Municipal Corporation's (PMC) limits.

![Pune population](/assets/posts/pune_transportation_analysis/Pune population (with villages).png){: width="900" height="500"}

**Figure 2: Population density of Pune (with new villages), 1981 - 2024**<br>
_Sources: Final calculations by author. 1981, 1991, 2001, and 2011 Pune area data taken from census. 2024 Pune area data taken from Capacity Building Commission (CBC)._

Without the new villages, the population density of Pune is closer to around 18,000 per square kilometre. There is still a problem of congestion of people. As such, the need for a proper public transport system has become much more essential as well.

![Pune population](/assets/posts/pune_transportation_analysis/Pune population (without villages).png){: width="900" height="500"}

**Figure 3: Population density of Pune (without new villages), 1981 - 2024**<br>
_Sources: Final calculations by author. 1981, 1991, 2001, and 2011 Pune area data taken from census. 2024 Pune area is taken same as 2011 area._

There are around **1932 total buses** within all depots as reported in August 2024 by PMPML. This is an increase from July 2024 but a decrease from August 2023. According to PMPML depotwise statistics, the number of buses is decreasing. Around August 2020, there were close to 2500 buses but this number has been slowly decreasing and now sits at 1932 buses. There is more news that PMPML's fleet will shrink even more (Bengur, 2024). This is catastrophic as this means that the already congested buses will be even more congested if more buses are not quickly added to the fleet.

![PMPML fleet](/assets/posts/pune_transportation_analysis/PMPML fleet.png){: width="900" height="500"}

**Figure 4: The number of buses, total and per day, in PMPML’s fleet from 2020 to 2024**<br>
_Source: PMPML’s depotwise statistics, August 2020 to August 2024. August 2022 data is from August 2023 statistics._

## 2.1 The Causes

### 2.1.1 Not Enough Buses

One of the main causes of overcongestion in buses is that there are just not enough buses that are operating on some of the routes. The following table shows the number of buses that flow to and from the major bus stations or depots. This data, which has been calculated from PMPML bus timings, is the expected number of buses that should be flowing down the routes.

<div class="table-container">
  <table>
    <colgroup>
      <col style="width: 65%;">
      <col style="width: 35%;">
    </colgroup>
    <thead>
      <tr>
        <th>Route</th>
        <th>Number of Buses</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>Pune Station to/from Swargate</td><td>420</td></tr>
      <tr><td>Shivajinagar to/from Swargate</td><td>406</td></tr>
      <tr><td>Katraj to/from Nigdi</td><td>384</td></tr>
      <tr><td>Bhosari to/from Pune station</td><td>302</td></tr>
      <tr><td>Manapa to/from Lohegaon</td><td>250</td></tr>
      <tr><td>Narhegaon to/from Swargate</td><td>232</td></tr>
    </tbody>
  </table>
</div>

**Table 2: Total number of buses on 7 major routes in Pune**<br>
_Source: Final calculations by author. Bus and route timings provided by PMPML._

However, PMPML's own statistics show that only **1566 buses** are on all the routes compared to the full fleet of 1932 buses. As such, many of the busy routes as shown below as well as the other routes which have been allocated fewer buses are getting even lower amount of buses than allotted. This means that:

a) There are already a lower number of buses overall due to the shrinking fleet compared to past years.<br>
b) There is also a lower number of buses on average on road per day.

This means that there is a double effect on severity of the situation where one is occurring over the long run and one is persisting over the short run.

An example of this is **Senapati Bapat Road** and subsequently Law College road which connects from Pune University Road down to the SNDT college bus stop that is under Nal Stop metro station. 

![SB Road](/assets/posts/pune_transportation_analysis/SB Road.png){: width="450" height="250"}

**Figure 5: Senapati Bapat Road to SNDT College route**<br>
_Source: Google Maps_

The route is only served by two buses, 276 and 277, which come from Chinchwad and Bhosari respectively. Both of them are filled to the brim by the time they reach anywhere close to Senapati Bapat road. It also does not help the fact that 277 is scheduled every hour and 276, which is scheduled every 15 minutes, fails to meet its timetable leading large gaps between the previous and the next bus.

### 2.1.2 Availability to Commuters

Public buses are incredibly cheap to ride on. According to PMPML's fare calculator, a journey of 20 kilometers will only cost a consumer **25 rupees**. One of the busiest routes within PMPML's routes is Katraj – Nigdi as shown in table 2. The route is around 34 kilometres. It will cost only **35 rupees** to go from one depot to another. 

This is one of the main reasons as to why commuters flock to public buses. It is cheap and has an extensive route network. As such, even if there is congestion on buses, commuters do not think of the alternative which is either an auto-rickshaw or a 2/4-wheeler if they have one. Based on Government of Maharashtra's traffic card, an auto-rickshaw will register around **500 rupees** for a trip like Katraj – Nigdi.

### 2.1.3 Tight Schedule, Lax Implementation

A tight bus schedule will only ever be as good as the bus drivers that follow it. Clearly, based on the example given earlier and many instances faced by commuters, the non-compliance to the schedule leads to immense delays in commuters' journeys. There is a complaint system that has been set up where a commuter can call a hotline to inform that a bus did not arrive. However, the fact that this responsibility has been given to the commuters just shows the organizational holes in PMPML's management.

# 3. What the Government Can Do

## 3.1 Increase the Fleet and Number of Buses Along Major Hotspots

An obvious solution is to increase the fleet and simultaneously increase the number of buses along crowded routes. However, it seems to be more complicated than it should be considering that PMPML has delayed bus purchase decision as of August 2024 (PunePulse, 2024). It is imperative that the fleet size is increased to well beyond **2500 buses** at least and many of them to be deployed in the major routes.

PMPML has already identified that there are four major routes:
- **Warje – Kharadi**
- **Kothrud – Vishrantwadi** 
- **Dhayari – Hadapsar**
- **Aundh – Katraj** (which can extend ahead of Aundh towards Kalewadi and Bhosari)

![Possible routes](/assets/posts/pune_transportation_analysis/possible routes.png){: width="600" height="330"}

**Figure 6: 4 major corridors that have been identified by PMPML**<br>
_Source: PMPML_

The addition of buses in the fleet should focus on these major corridors to alleviate traffic.

## 3.2 Pune Metro

One major addition in Pune's public transport is the Pune metro. However, it should not be mistaken as the savior of Pune's public transport woes. It will not reduce traffic but merely redirect it in the slightest. One major reason for this is due to **induced demand**. Since the metro has been developed, commuters expect others to use the metro and as such may choose to take 2-wheelers or 4-wheelers expecting for the roads to have less traffic.

Two major areas where the Pune metro does not serve yet are **Katraj and Hadapsar**. Although the detailed project report for Swargate – Katraj metro extension has been released, the commencement of operations is in 2027 (PuneMetroRail, 2024). There is also consideration to extend Line 3, which starts from Hinjewadi, towards Hadapsar.

## 3.3 Peak Hour Adjustments

PMPML should also learn from Pune metro's lessons of increasing the rate of metro during peak hours while slowing it down during off-peak hours. This will cater to the higher number of commuters during morning and evening peak hours where as opposed to constant number of buses as it is in the present, there are higher rates of buses taking commuters which will reduce the stress on the latter buses that will run through the route.

## 3.4 Restrictions on Vehicles

According to PunekarNews (2022), the number of vehicles is similar to the city's population. The number of two-wheelers in 2018 was around **26 lakhs** which is close to half of the city's population in 2024. This means that there is an even higher number of two-wheelers in 2024.

![Pune's vehicle population](/assets/posts/pune_transportation_analysis/Pune's vehicle population.png){: width="900" height="500"}

**Figure 7: Pune’s Vehicle Population, 2000 - 2018**<br>
_Source: Statistics compiled by Regional Transport Office (RTO), data released by Pune Data Store_

As such, there must be restrictions enacted on vehicles, especially on 2-wheelers. One such restriction is the **driving restriction policy (DPR)** which has significant effect in improving public transport (Zhang, Long, & Chen, 2019). Zhang et al. found that around 5-25% of public transport passenger volume increased due to DPRs. This can be tried in certain areas of Pune to test its effectiveness.

# 4. Conclusion

In conclusion, Pune's public buses face overcongestion due to lack of number of buses which are both due to long term decline in fleet size and short term sub-optimal number of buses running every day. It is also due to the cheap fares that attract large number of commuters. This combined with low number of buses is a big problem. At last, there is also lax implementation. 

Overall, the solutions are that PMPML and Pune metro must tackle this problem together as this is not a standalone effort. There must also be better road planning including the design of flyovers and taking into account the choke points. Lastly, peak hour adjustments and driving restriction policies must be tried and tested within certain areas. If successful, the policies can be taken citywide.

---

# References

Bengur, D. (2024, June 17). Pax demand more buses as PMPML fleet shrinks. *Hindustan Times.* [Link](https://www.hindustantimes.com/cities/pune-news/pax-demand-more-buses-as-pmpml-fleet-shrinks-101718563117101.html)

Capacity Building Commission. (2023). *Annual Capacity Building Plan 2023-24.* [Link](https://cbc.gov.in/sites/default/files/completed-acbps/Pune_Municipal_Corporation_ACBP.pdf)

Census of India. (1991). *Census Population Data 1991.* Pune Municipal Corporation. [Link](https://www.pmc.gov.in/sites/default/files/census-population-data-1991.pdf)

Census of India. (2001). *Census Population Data 2001.* Pune Municipal Corporation. [Link](https://pmc.gov.in/sites/default/files/census-population-data-2001.pdf)

Census of India. (2011). *Census Population Data 2011.* Pune Municipal Corporation. [Link](https://pmc.gov.in/sites/default/files/census-population-data-2011.pdf)

Census2011. (2022). *Pune Population 2024.* [Link](https://www.census2011.co.in/census/city/375-pune.html)

Google Maps. (2024). *Google Maps Directions.* [Link](https://www.google.com/maps/dir/Sai+Crane+Service,+Range+Hill+Corner,+Chattushringi,+Gokhalenagar,+Pune,+Maharashtra+411038/Sndt+Over+Bridge,+Pandurang+Colony,+Erandwane,+Pune,+Maharashtra+411004/@18.5236229,73.8087533,14z/data=!3m1!4b1!4m14!4m13!1m5!1m1!)

Mahatme, A. W. (2021, May 28). *District Census Handbook, Pune – Census 1981.* Census India. [Link](https://censusindia.gov.in/nada/index.php/catalog/29711)

Motor Vehicles Department, Maharashtra. (2022). *Revised Tariff Card Auto Rickshaw (English).* [Link](https://transport.maharashtra.gov.in/Site/Upload/GR/Auto%20English%201.pdf)

Pune Mahanagar Parivahan Mahamandal Limited. (2020). *Depotwise Monthly Statistical Report August 2020.* Open Data Pune Corporation. [Link](http://opendata.punecorporation.org/Citizen/CitizenDatasets/Index?categoryId=19)

Pune Mahanagar Parivahan Mahamandal Limited. (2022, February 4). *Depotwise Monthly Statistical Report August 2021.* Open Data Pune Corporation. [Link](http://opendata.punecorporation.org/Citizen/CitizenDatasets/Index?categoryId=19)

Pune Mahanagar Parivahan Mahamandal Limited. (2023, October 13). *Depotwise Statistical Report for the month of August 2023.* PMPML. [Link](https://pmpml.org/assets/media_center/1698209633966e17937455c15c2ef8bed3c48a8972.pdf)

Pune Mahanagar Parivahan Mahamandal Limited. (2024, October 10). *Depotwise Statistical Report for the month of August 2024.* PMPML. [Link](https://pmpml.org/assets/media_center/172855449144de55410b031492390c01315e8e7d90.pdf)

Pune Mahanagar Parivahan Mahamandal Limited. (2024). *Route Map Image.* PMPML. [Link](https://pmpml.org/plugins/images/home/route_map_image.png)

Pune Mahanagar Parivahan Mahamandal Limited. (n.d.). *Route No.* PMPML. [Link](https://pmpml.org/assets/schedule/170866629042bbb3b37009c5fd5bea2b0df59c1b62.pdf)

Pune Metro. (2024, September). *Swargate-Katraj DPR.* Pune Metro Rail. [Link](https://punemetrorail.org/download/Swargate-Katraj%20DPR.pdf)

Punekar News. (2022, October 25). *Number of vehicles in Pune almost matches city’s population.* Punekar News. [Link](https://www.punekarnews.in/number-of-vehicles-in-pune-almost-matches-citys-population/)

PunePulse. (2024, August 10). *Pune PMPML delays bus purchase decision.* Pune Pulse. [Link](https://www.mypunepulse.com/pune-pmpml-delays-bus-purchase-decision/)

Regional Transport Office. (n.d.). *Vehicle Population Statistics for RTO Pune – 2000–2018.* Open Data Pune Corporation. [Link](http://opendata.punecorporation.org/Citizen/CitizenDatasets/Index?categoryId=51)

Zhang, L., Long, R., & Chen, H. (2019). Do car restriction policies effectively promote the development of public transport? *World Development.* [DOI/Link if available]
