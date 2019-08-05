# iso3_lookup

Small python package to lookup country iso3 codes from the country name and visa-versa. 

## Install 
```
pip3 install iso3-lookup
```

## About
Does exactly what it says on the tin - user can quickly go between iso3 codes and country name,
currently isn't very intelligent so just used the lowercase of each for the lookup, the underlying data
comes from [this](https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes) excellent package however
also need to sort the link out between these two as currently very manual and want to auto-update if changes.  

## Usage 
`get_iso3(country)` - get the iso3 code from the country name.
`get_country(iso3)` - get the country name from the iso3 code.

## TODO
- Create a better link between underlying data and functions so dont have to pull whole thing onto local machine,
could easily do this by querying the raw github file, this however would rely on an internet connection.
- Create fuzzy-logic rules when searching for country names -> some such as United Kingdom of Great Britain and Northern Ireland
are very clunky and should be easy to get this to match with Great Britain and United Kingdom for example. 



