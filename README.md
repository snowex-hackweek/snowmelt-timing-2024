# snowmelt-timing-2024

## Seasonal snowmelt timing

The purpose of this project is to explore different data and methodologies that, when combined, will help us better understand seasonal snowmelt timing. Amongst other types of data, team members will be exposed to Sentinel-1 SAR data, SNOTEL data, MODIS snow products, SWE reanalysis products, and SnowEx snow pit data. This project is intentionally more flexible, if you have ideas adjacent to this work, let's find ways to build it in! **This project is a spiritual successor to the 2022 snowex hackweek project snowmelt-timing, check out our [repo](https://github.com/snowex-hackweek/snowmelt-timing) and [presentation](https://docs.google.com/presentation/d/1czTH2q2nH_Lf7uoYkDXu03mFaJVkOE3GxtXRAFWuBhg/edit?usp=sharing).** 

### Collaborators

| Name | Personal goals | Can help with | Role |
| ------------- | ------------- | ------------- | ------------- |
| Eric Gagliano | I want to learn how different types of snowmelt data can compliment each other! | I can help with SAR / snowmelt theory, data access | project lead (hopefully co-lead??) |
| Emma Boudreau | I want to learn specific python libraries for working with these data  | I can help with understanding our dataset, programming in R  | Project Lead |
| Lexi Arlen | Learn remote sensing workflows & python packages | machine learning and python (scipy, scikit-learn) | Team Member |
| Jesse Pisel | learning more about state of the art in remote sensing and snowmelt | machine learning, deep learning, project management | Project Helper |
| Andrea Bruckmeier | learn to use github, resolve merge conflicts, get to know the wet snow datasets and datasets with an SWE or LWC output | I am familiar with wet snow reagrding avalanches | Team Member  |
| Molly Tedesche | ... | ... | ... |
| Savalan Naseiry | ... | ... | ... |
| Randall Bonnell | Explore applicability of GPR for C-band wet snow validation | GPR LWC calculations, C-band lit review | Team Member |

### The problem

Snowmelt timing has high spatial and temporal variability, and different types of data and methodologies that attempt to measure properties of snowmelt have their own strengths and weaknesses. This project hopes to address these challanges, leveraging the strengths of disparate appraoches to better characterize the evolution of snowmelt.

## Data and Methods

### Data

Briefly describe and provide citations for the data that will be used (size, format, how to access).

Some ideas:
* Sentinel-1 C-band RTC
* MODIS snow products
* Harmonized Landsat / Sentinel-2 optical
* SnowEx snow pit data
* SNOTEL automatic weather station data
* SWE reanalysis products

### Existing methods

How would you or others traditionally try to address this problem? Provide any relevant citations to prior work.

SAR snowmelt toolbox and snow wetness tools I've built:
* https://github.com/egagli/sar_snowmelt_timing
* https://github.com/egagli/wet_snow_threshold_localization

### Proposed methods/tools

**TBD!**

What new approaches would you like to implement for addressing your specific question(s) or application(s)?


### Additional resources or background reading

**TBD!**

Optional: links to manuscripts or technical documents providing background information, context, or other relevant information.

* shameless plug: Gagliano, E., Shean, D., Henderson, S., & Vanderwilt, S. (2023). Capturing the onset of mountain snowmelt runoff using satellite synthetic aperture radar. Geophysical Research Letters, 50, e2023GL105303. https://doi.org/10.1029/2023GL105303

## Project goals and tasks

### Project goals

**TBD!**

The goal of this project is to explore different data and methodologies that, when combined, will help us better understand seasonal snowmelt timing.

* Goal 1 (provide a timeseris of different datasets displaying outputs that help to understand seasonal snowmelt timing)
* Goal 2 (comparison of datasets)

### Tasks

**TBD!**

What are the individual tasks or steps that need to be taken to achieve each of the project goals identified above? What are the skills that participants will need or will learn and practice to complete each of these tasks? Think about which tasks are dependent on prior tasks, or which tasks can be performed in parallel.

* Task 1 (get an overview of the datasets that include information on snow melt and wet snow)
* Task 2 (each of the team memeber focuses on one or two datasets to explore and compare)
* Task 3 (bring all outputs together)


## Project Results

**TBD!**

We focussed on the Grand Mesa (CO) location in the winter season 2019/2020. We were looking through the available data for this location and could plot time series for various SWE, temperature and LWC measurements. Our group's main goal was to provide an overview of the data that is available and what the output of each dataset can tell us in terms of snow melt and wet snow. 
We had a look at: 
* Sentinel-1 C-band RTC
* MODIS snow products
* Harmonized Landsat / Sentinel-2 optical
* SnowEx snow pit data
* SNOTEL automatic weather station data
* SWE reanalysis products
The result shows comparisons over a timeseries [link]

At a different location, the Jemez Mountain (NM), we compared the LWC of the snow pit data to the GPR data for three specific dates, on which both datasets were available. The code for this can be found here: [https://github.com/snowex-hackweek/snowmelt-timing-2024/blob/main/contributors/andrea/LWC_pits.ipynb]


