# Sam Solheim
# 11/18/2020
# description: Assignment 7 -- Utilizing .csv files to create graphs,
#                              and interpret data, specifically data related to
#                              'Biodiversity in National Parks' in the United States

import csv
import matplotlib.pyplot as plt

def display_fields(data):
    """
    parameter: data is an input data read in from csv.Dict
    display_fields prints out all of the fields (columns) in the data set
    """
    for field in data.fieldnames:
        print(field)

def process_data(data, natl_park):
    """
    input: data: a set of National Park statistics
    prints out the 
    """
    
    spec_concern = [] #create empty list for Species of Concern
    threat_spec = [] #create empty list for Threatened species
    end_species = [] #create empty list for Endangered species
    
    #loop through all of the data
    for row in data:
        if row["Park Name"] == natl_park and row["Conservation Status"] == "Species of Concern":
            spec_concern.append(row["Common Names"])
        elif row["Park Name"] == natl_park and row["Conservation Status"] == "Threatened":
            threat_spec.append(row["Common Names"])
        elif row["Park Name"] == natl_park and row["Conservation Status"] == "Endangered":
            end_species.append(row["Common Names"])
    
    print("The number of Species of Concern at", natl_park, "is:", len(spec_concern))
    print("The number of Threatened Species at", natl_park, "is:", len(threat_spec))
    print("The number of Endangered species at", natl_park, "is:", len(end_species))

def gen_stats_n_scatter(data, data2):
    """
    inputs: data: a data set of National Park names and their geographic characteristics
            data2: a set of National Park statistics on wildlife and their conservation status (among other information)
    Purpose: prints out a nested list that contains data about each national park in the following order:
            [["Park Name"], # of "Species of Concern", # of "Threatened" Species, # of "Endangered" Species, # of Species "In Recovery",
            # of "Not Native" Species, # of Species of "Unknown" Nativeness], [...]]
    Returns: natl_park_stats
    """
    
    count = 0
    
    natl_park_names = [] #create an empty list for the names of the national parks
    natl_park_stats = [] #create an empty list for an individual park's statistics

    for row in data:
        if row["Park Name"]:
            natl_park_names.append(row["Park Name"])
            count += 1
    
    # loop through all of data2, create a new nested list with the information regarding species in every national park
    # Note: The names of species are not a concern with my analysis, so I am only using the amount of species in each relevant category,
    #       there are way too many species in a single park to focus on all their names
    count2 = 0
    spec_concern = 0
    threat_spec = 0
    end_species = 0
    in_recov = 0
    
    not_native = 0
    unknown_native = 0
    filler_var = 0
    
    for row in data2:
        # The following nested if/elif statements below test that the information counted is all for a specific national park,
        # and then checks whether a second desireable requirement is met, from here, there are several other variables
        # that are tested and accounted for
        if row["Park Name"] == natl_park_names[count2] and row["Conservation Status"] == "Species of Concern":
            if row["Nativeness"] == "Not Native":
                spec_concern += 1
                not_native += 1
            elif row["Nativeness"] == "Unknown":
                spec_concern += 1
                unknown_native += 1
            else:
                spec_concern += 1
                
        elif row["Park Name"] == natl_park_names[count2] and row["Conservation Status"] == "Threatened":
            if row["Nativeness"] == "Not Native":
                threat_spec += 1
                not_native += 1
            elif row["Nativeness"] == "Unknown":
                threat_spec += 1
                unknown_native += 1
            else:       
                threat_spec += 1
                
        elif row["Park Name"] == natl_park_names[count2] and row["Conservation Status"] == "Endangered":
            if row["Nativeness"] == "Not Native":
                end_species += 1
                not_native += 1
            elif row["Nativeness"] == "Unknown":
                end_species += 1
                unknown_native += 1
            else:       
                end_species += 1
                
        elif row["Park Name"] == natl_park_names[count2] and row["Conservation Status"] == "In Recovery":
            if row["Nativeness"] == "Not Native":
                in_recov += 1
                not_native += 1
            elif row["Nativeness"] == "Unknown":
                in_recov += 1
                unknown_native += 1
            else:       
                in_recov += 1
                
        #Weeds out species that meet none of the Conservation Status criteria above, needed to update to include Nativeness variable
        elif row["Park Name"] == natl_park_names[count2]:
            if row["Nativeness"] == "Not Native":
                filler_var += 1
                not_native += 1
            elif row["Nativeness"] == "Unknown":
                filler_var += 1
                unknown_native += 1
            else:
                filler_var += 1
        
        # The following section of code allows for a nested list of important data for each National Park, and
        # it also sets all necessary variables back to zero
        elif row["Park Name"] != natl_park_names[count2]:
            temp_list = [natl_park_names[count2], spec_concern, threat_spec, end_species, in_recov, not_native, unknown_native]
            natl_park_stats.append(temp_list)
            spec_concern = 0
            threat_spec = 0
            end_species = 0
            in_recov = 0
            not_native = 0
            unknown_native = 0
            
            count2 += 1
    #To include the data from the last park
    temp_list = [natl_park_names[count2], spec_concern, threat_spec, end_species, in_recov, not_native, unknown_native]
    natl_park_stats.append(temp_list)
    
#     print(natl_park_stats)
    
    park_scores = []
    count3 = 0
    spec_at_risk = 0
    invasive = 0
    inv_per_at_risk = 0
    #s
    
    for i in natl_park_stats:
        spec_at_risk = natl_park_stats[count3][1] + natl_park_stats[count3][2] + natl_park_stats[count3][3] + natl_park_stats[count3][4]
        invasive = natl_park_stats[count3][5] + natl_park_stats[count3][6]
        invasive_per_at_risk = float(format((invasive/spec_at_risk), ".2f"))
        park_scores.append([natl_park_stats[count3][0], spec_at_risk, invasive, invasive_per_at_risk])
        count3 += 1
    print(park_scores)
    
#     The following section of the code was utilized to determine the highest and lowest scores out of the National Parks
#     but was not utilized in the final graph of collected data
# 
#     min_score = 100
#     max_score = 0
#     min_list = []
#     max_list = []
#     count4 = 0
#     
#     for f in park_scores:
#         if park_scores[count4][3] <= min_score:
#             min_score = park_scores[count4][3]
#             min_list.append([park_scores[count4][0], park_scores[count4][3]])
#             count4 += 1
#         elif park_scores[count4][3] >= max_score:
#             max_score = park_scores[count4][3]
#             max_list.append([park_scores[count4][0], park_scores[count4][3]])
#             count4 += 1
#         else:
#             count4 += 1
#     print(min_list)
#     print(max_list)
    
    #The following section uses the data from the generated list to create a scatterplot
    np_names = []
    np_scores = []
    color = 'black'
    size = 10
    count5 = 0
    x_bar = []
    
    for g in park_scores:
        np_scores.append(park_scores[count5][3])
        x_bar.append(count5)
        count5 += 1
    
    np_scores.sort()
    print(np_scores)

    plt.scatter(x_bar, np_scores, c=color, s=size, alpha=1)
    plt.xlabel("National Parks in the United States (Individual Names Not Listed)")
    plt.ylabel("Ratio of Non-Native Species Per At Risk Species")
    plt.title("Conservation in National Parks")
    plt.show()

def main():
    #open file data
    infile_parks = open("parks.csv", "r", encoding="utf8")
    infile_species = open("species.csv", "r", encoding="utf8")
    park_scores = 0
    
    #create variable to read through the data
    parks_data = csv.DictReader(infile_parks)
    species_data = csv.DictReader(infile_species)
    #process_data function was initially used to doublecheck accuracy of gen_stats formula, formulas do not work at the same time
#     process_data(species_data, 'Zion National Park')
    
    #Sorts through data and creates a list with more readily usable info
    gen_stats_n_scatter(parks_data, species_data)

main()










