import pandas as pd

# Data for the additional companies
more_companies_data = {
    "Company Name": [
        "Tech Mahindra", "Mphasis", "Mindtree", "Zensar Technologies", "L&T Infotech",
        "Hindalco Industries", "JSW Steel", "Tata Steel", "Vedanta Resources", "Coal India",
        "Indian Oil Corporation", "Bharat Petroleum", "Hindustan Petroleum", "GAIL", "ONGC",
        "Nestle India", "Britannia Industries", "Dabur", "Amul", "Parle Products",
        "Apollo Hospitals", "Fortis Healthcare", "Max Healthcare", "Cipla", "Biocon",
        "Infosys", "Techno Electric", "IndiGo", "SpiceJet", "Jet Airways",
        "Airtel Payments Bank", "Paytm", "PhonePe", "Reliance Jio", "Vodafone Idea",
        "Zomato", "Swiggy", "Ola", "Uber India", "DHL India",
        "Flipkart", "Snapdeal", "Amazon India", "Myntra", "Ajio",
        "Future Group", "Reliance Retail", "Shoppers Stop", "Spencer's Retail", "Big Bazaar",
        "HDFC Bank", "Kotak Mahindra Bank", "Yes Bank", "Federal Bank", "Bank of Baroda",
        "Adani Group", "Bharat Electronics Limited", "Larsen & Toubro", "Sun Pharmaceutical Industries", "Tata Motors",
        "Godrej Consumer Products", "Maruti Suzuki", "Bajaj Auto", "Hero MotoCorp", "Eicher Motors",
        "Mahindra & Mahindra", "Ashok Leyland", "TVS Motor Company", "Voltas", "Blue Star",
        "Havells India", "Schneider Electric India", "Siemens India", "ABB India", "Crompton Greaves",
        "Bosch India", "Honeywell India", "3M India", "LG Electronics India", "Samsung India",
        "Panasonic India", "Sony India", "Godrej & Boyce", "Whirlpool India", "IFB Industries",
        "DHL Supply Chain", "FedEx India", "Blue Dart", "Delhivery", "Gati Ltd."
    ],
    "Company Description": [
        "IT services and consulting firm", "IT services provider", "Digital transformation and technology consulting", "IT solutions and services", "IT consulting and services firm",
        "Metals and mining company", "Steel production", "Steel manufacturing", "Natural resources and mining", "Coal mining and production",
        "Oil refining and marketing", "Oil and gas company", "Oil and gas refining", "Natural gas processing and distribution", "Oil and gas exploration",
        "FMCG with a focus on food products", "FMCG company focused on dairy and bakery products", "Consumer goods company", "Dairy cooperative", "FMCG food products",
        "Healthcare and hospital chain", "Healthcare services", "Hospital and healthcare services", "Pharmaceutical manufacturing", "Biotechnology company",
        "IT consulting and outsourcing", "Renewable energy and infrastructure services", "Low-cost airline", "Budget airline", "Full-service airline",
        "Mobile banking and financial services", "Digital payments and e-commerce", "Digital wallet and UPI service", "Telecom and digital services", "Telecommunications company",
        "Online food delivery service", "Online food delivery platform", "Ride-hailing service", "Ride-hailing service", "Logistics and courier services",
        "E-commerce platform", "E-commerce marketplace", "E-commerce marketplace", "Fashion and lifestyle e-commerce", "Fashion e-commerce",
        "Retail conglomerate", "Retail arm of Reliance Industries", "Retail chain", "Retail chain", "Supermarket chain",
        "Private sector bank", "Private sector bank", "Private sector bank", "Private sector bank", "Public sector bank",
        "Conglomerate with interests in energy, resources, logistics, and agribusiness", "State-owned aerospace and defense company", "Engineering, construction, manufacturing, technology, and financial services conglomerate", "Multinational pharmaceutical company", "Automotive manufacturing company",
        "Leading FMCG company in personal care and household products", "Automobile manufacturing", "Motorcycle manufacturing", "Motorcycle and scooter manufacturing", "Commercial vehicle manufacturing",
        "Automobile manufacturing and defense", "Commercial vehicle manufacturing", "Two-wheeler manufacturing", "Cooling appliances and air conditioners", "Air conditioning and commercial refrigeration",
        "Electrical equipment and home appliances", "Energy management and automation solutions", "Electrical engineering and automation", "Engineering and technology solutions", "Power and energy solutions",
        "Engineering and technology solutions", "Automation and safety products", "Industrial and consumer products", "Consumer electronics and home appliances", "Consumer electronics and smartphones",
        "Consumer electronics and home appliances", "Consumer electronics and smartphones", "Manufacturing and engineering", "Home appliances and electronics", "Home appliances and electronics",
        "Logistics and supply chain management", "Logistics and courier services", "Courier and logistics services", "E-commerce logistics and supply chain", "Logistics and supply chain solutions"
    ],
    "Industry": [
        "IT Services", "IT Services", "IT Services", "IT Services", "IT Services",
        "Metals and Mining", "Steel", "Steel", "Mining", "Coal",
        "Oil and Gas", "Oil and Gas", "Oil and Gas", "Oil and Gas", "Oil and Gas",
        "FMCG", "FMCG", "FMCG", "Dairy", "FMCG",
        "Healthcare", "Healthcare", "Healthcare", "Pharmaceuticals", "Biotechnology",
        "IT Services", "Energy", "Aviation", "Aviation", "Aviation",
        "Fintech", "Fintech", "Fintech", "Telecom", "Telecom",
        "Food Delivery", "Food Delivery", "Transport", "Transport", "Logistics",
        "E-commerce", "E-commerce", "E-commerce", "E-commerce", "E-commerce",
        "Retail", "Retail", "Retail", "Retail", "Retail",
        "Banking", "Banking", "Banking", "Banking", "Banking",
        "Conglomerate", "Aerospace and Defense", "Engineering and Construction", "Pharmaceuticals", "Automotive",
        "FMCG", "Automotive", "Automotive", "Automotive", "Automotive",
        "Automotive", "Automotive", "Automotive", "Consumer Electronics", "Consumer Electronics",
        "Consumer Electronics", "Energy", "Energy", "Energy", "Energy",
        "Engineering", "Automation", "Technology", "Consumer Electronics", "Consumer Electronics",
        "Consumer Electronics", "Consumer Electronics", "Manufacturing", "Consumer Electronics", "Consumer Electronics",
        "Logistics", "Logistics", "Logistics", "Logistics", "Logistics"
    ],
    "Headquarters Location": [
        "Mumbai", "Bengaluru", "Bengaluru", "Pune", "Mumbai",
        "Mumbai", "Mumbai", "Jamshedpur", "Mumbai", "Kolkata",
        "New Delhi", "Mumbai", "Mumbai", "New Delhi", "New Delhi",
        "Gurgaon", "Bengaluru", "New Delhi", "Anand", "Mumbai",
        "Chennai", "Gurgaon", "New Delhi", "Mumbai", "Bengaluru",
        "Bengaluru", "Kolkata", "Gurgaon", "Gurgaon", "Mumbai",
        "New Delhi", "Noida", "Bengaluru", "Mumbai", "Mumbai",
        "Gurgaon", "Bengaluru", "Bengaluru", "New Delhi", "Mumbai",
        "Bengaluru", "New Delhi", "Bengaluru", "Bengaluru", "Mumbai",
        "Mumbai", "Mumbai", "Mumbai", "Kolkata", "Mumbai",
        "Ahmedabad", "Bengaluru", "Mumbai", "Mumbai", "Mumbai",
        "Mumbai", "New Delhi", "Pune", "New Delhi", "Chennai",
        "Mumbai", "New Delhi", "New Delhi", "Chennai", "Mumbai",
        "Bengaluru", "Chennai", "Hosur", "Mumbai", "Mumbai",
        "Noida", "Gurgaon", "Gurgaon", "Mumbai", "Bangalore",
        "Gurgaon", "New Delhi", "Mumbai", "New Delhi", "Hyderabad"
    ],
    "Founded Year": [
        1986, 1992, 1999, 2001, 1997,
        1958, 1982, 1907, 1979, 1975,
        1964, 1952, 1952, 1984, 1956,
        1959, 1918, 1884, 1946, 1929,
        1983, 2001, 2000, 1935, 1978,
        1981, 1963, 2006, 1984, 1992,
        2015, 2010, 2015, 2007, 2008,
        2008, 2014, 2010, 2013, 1988,
        2007, 2010, 2000, 2007, 2007,
        1987, 2006, 1991, 1920, 1987,
        1994, 1985, 2004, 1961, 1945,
        1959, 1980, 1984, 1945, 1955,
        1945, 1948, 1975, 1954, 1930,
        1940, 1974, 1940, 1968, 1962,
        1951, 1953, 1948, 1955, 1962,
        1965, 1981, 1994, 1999, 2003
    ]
}
# Creating a DataFrame
df_sample = pd.DataFrame(more_companies_data)

# Writing the DataFrame to the original Excel file
output_file_path = 'sd/Dataset_filled.xlsx'
df_sample.to_excel(output_file_path, index=False)

output_file_path