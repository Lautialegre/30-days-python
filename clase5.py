empty_list = []
print(empty_list)

numbers = [1, 2, 3, 4, 5, 6]
print(len(numbers))

print(numbers[0])
print(numbers[2]) 
print(numbers[5])

mixed_data_types = ["lautaro",21,1.75,"single","Tomas brid 162"]

it_companies = ["Facebook","Google","Microsoft","Apple","IBM","Oracle","Amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[3])
it_companies[0] = "GitHub"
print(it_companies)
it_companies.append("X")
it_companies.insert(6,"TikTok")
it_companies[0].upper()
## it_companies = "#".join(it_companies)  
isincompany = "TikTok" in it_companies
print(isincompany)
it_companies.sort() 
it_companies.reverse()
print(it_companies[0:3])
print(it_companies[3:5])
it_companies.remove(it_companies[0])
it_companies.remove(it_companies[6])
it_companies.clear() 

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
full_stack.append('Python')
full_stack.append('SQL')
print(full_stack)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print("Min age:", min_age)
print("Max age:", max_age)
ages.append(min_age)
ages.append(max_age)
# Find the median age (one middle item or two middle items divided by two)
median_age = ages[len(ages) // 2] if len(ages) % 2 == 1 else (ages[len(ages) // 2 - 1] + ages[len(ages) // 2]) / 2
print("Median age:", median_age)

average_age = sum(ages) / len(ages)
print("Average age:", average_age)

max_min_diff = max_age - min_age
print("Difference between max and min age:", max_min_diff)

min_average_diff = abs(min_age - average_age)
max_average_diff = abs(max_age - average_age)
print("Difference between min age and average age:", min_average_diff)
print("Difference between max age and average age:", max_average_diff)  

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

middle_index = len(countries) // 2
middle_country = countries[middle_index]
print("Middle country:", middle_country)
print(len(countries))
if len(countries) % 2 == 0:
    first_half = countries[:middle_index]
    second_half = countries[middle_index:]
else:
    first_half = countries[:middle_index]
    second_half = countries[middle_index + 1:]

print("First half of the countries list:", first_half)
print("Second half of the countries list:", second_half)

# unpack the first three countries and the rest of the countries

scandic_countries =['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *rest_countries = scandic_countries

print("First country:", first_country)
print("Second country:", second_country)    
print("Third country:", third_country)
print("Rest of the countries:", rest_countries)