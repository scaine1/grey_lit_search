# Grey Lit Search

This is a simple package that allows users to download pdf files associated with a google search.

It is intended to be used by the scientific research community to speed up grey literature searches.

## Example usage

In your browser open up a google search and enter your search term
You will likely want to include +pdf in your search term

e.g if seaching for depressions input  "depression +pdf" into the google seach

After clicking search copy the url from the browser. Then use the url as input into
they Grey Lit Search program

e.g.

greysearch --url "https://www.google.com.au/search?sxsrf=ACYBGNTN2I-ZiNy4qYPUnn1yfmPMg3ZFFw%3A1575175967610&ei=H0fjXZruJMq9rQHTl7_IBQ&q=depression+%2Bpdf&oq=depression+%2Bpdf&gs_l=psy-ab.3...48781.57571..57803...2.3..0.259.2314.0j13j1......0....1..gws-wiz.......0i71.frhhqm73guY&ved=0ahUKEwja-Yfg05PmAhXKXisKHdPLD1kQ4dUDCAs&uact=5"

By default the program will search for 100 results (this is the maximum amount possible)

If you want to limit the number of searches you can include a --results. For example if you want only 20 results you can do

greysearch --url "" --results 20

