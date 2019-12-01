# Grey Lit Search

This is a simple package that allows users to download pdf files associated with a google search.

It is intended to be used by the scientific research community to speed up grey literature searches.

## Installing

After downloading the source code find the setup.py and run the following

```
python setup.py install
```

This should install they grey\_lit\_search package on your system,
including an executable called "greysearch" which you should be able
to run from command line.

## Example usage

greysearch --url "search url" --results 20

see below on how to obtain the search URL


## Obtaining the search url

In your browser open up a google search and enter your search term

After clicking search, you should a page with your search results.
If you are happy with the search, then copy the URL from the browser address bar.

You can then use this URL as input into the greysearch program

Note that there may be a lot of weird letters and numbers in the address, this is OK copy the whole thing

Make to put the whole search between quotation marks when running on the command line

for example, the following URL was obtained by searching for "depressing +pdf"

greysearch --url "https://www.google.com.au/search?sxsrf=ACYBGNTN2I-ZiNy4qYPUnn1yfmPMg3ZFFw%3A1575175967610&ei=H0fjXZruJMq9rQHTl7_IBQ&q=depression+%2Bpdf&oq=depression+%2Bpdf&gs_l=psy-ab.3...48781.57571..57803...2.3..0.259.2314.0j13j1......0....1..gws-wiz.......0i71.frhhqm73guY&ved=0ahUKEwja-Yfg05PmAhXKXisKHdPLD1kQ4dUDCAs&uact=5"

## Limiting the number of results

By default, the program will search for 100 results (this is also the maximum amount possible)

If you want to limit the number of searches you can include --results #number when calling the program
 
For example, if you want only 20 results you can do

greysearch --url "searchurl" --results 20

