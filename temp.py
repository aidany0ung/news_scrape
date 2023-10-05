# Create a dictionary of important geographic abbreviations and their full names

dictio = {"NY": "New York",
          "NYC": "New York",
          "UK": "United Kingdom",
          "US": "United States",
            "USA": "United States",
            "U.S.": "United States",
            "U.S.A.": "United States",
            "U.K.": "United Kingdom",
            "U.K": "United Kingdom",
            "UAE": "United Arab Emirates",
            "U.A.E.": "United Arab Emirates",
            "U.A.E": "United Arab Emirates",
            "USSR": "Soviet Union",
            "AK": "Alaska",
            "AL": "Alabama",
            "AR": "Arkansas",
            "AS": "American Samoa",
            "AZ": "Arizona",
            "CA": "California",
            "CO": "Colorado",
            "CT": "Connecticut",
            "DC": "District of Columbia",
            "DE": "Delaware",
            "FL": "Florida",
            "GA": "Georgia",
            "GU": "Guam",
            "European": "Europe"}

# Read in nations.json
import json
with open('backend/nations.json') as f:
    nations = json.load(f)

for k,v in dictio.items():
    nations[k] = v

# Dump the dictionary to nations.json
with open('backend/nations.json','w') as f:
    json.dump(nations,f)


