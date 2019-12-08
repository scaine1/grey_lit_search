# Grey Lit Search

A simple package to aid the scientific research community in performing a grey literature searches.  A user can copy a url from a google search and the script will download all pdfs associated with a google search.

## Getting Started


You will need to have python installed on your system. If you do not already have python installed on your system see the Prerequisites section.

### Prerequisites
In order to get the script to work you will need  python to be installed on your system.
If you don't already have python installed I recommend that you install it via the anaconda distribution.
This will be a rather large download in order to get this simple package to work, but it very simple for people to do.

go to  https://www.anaconda.com/distribution/ and download for your operating system (i.e Windows, Mac or Linux)


### Installing

This will require the use of terminal or some form of command line interface.

First create a directory where you want the files to be downloaded. Perhaps a folder called grey_lit_search in your home directory or documents folder (Avoid using spaces in your names, while you can get things to work it will cause numerious hassles when working in terminal)

#### Windows users
If you installed python via anaconda then open the anaconda prompt (search in windows for anaconda prompt)

#### Mac OSX users
open the terminal program, click the launch pad icon and type "terminal" into the search box

#### navigate to the directory you created in the terminal program
in order to navigate to your directory can use the "change directory" command, which is 
```
cd grey_lit_search
```

This may be frustrating or intimidating for those who have not used terminal before. If you are having trouble you may want to do a quick goolge search and find a tutorial on how to navigate within the terminal

#### clone the source code
One you have navigated to the directory you can run the following command to pull down the source code

```
git clone https://github.com/scaine1/grey_lit_search.git
```

This should have created a directory called grey\_lit\_search. Go into the directory

```
cd grey_lit_search
```
If you get an error here and it looks like the error is saying you do not have git on your system.
Follow the relevent instructions for your OS at https://www.atlassian.com/git/tutorials/install-git


#### install via setup.py

Then install via the following command

```
python setup.py install
```

This should have installed the grey\_lit\_search package on your system. Including an executable script called greysearch which you can run in the anaconda prompt. See below for examples

#### cleanup the source code
You can now safely delete the directory with the source code. grey_lit_search has been installed on your system. 
See below on how to use.


## How to use

Once installed you should have a command line script that can be used to download google search results.

open an anaconda prompt and navigate to a directory you wish to download the data to.

to run the program you type the following

```
greysearch --url "search url"
```

see the following section on how to obtain the search url.

NOTE THAT YOU MUST PUT THE URL INSIDE THE QUOTATION MARKS.

## Obtaining the search url

In your browser of choice (firefox, chrome etc) go to the google search page and  enter your search term.

After clicking search you should have page with your search results.
If you are happy with the search as you have defined it, copy the URL from the browser address bar.

This is your search url and is what needs to be pasted inside the quotation marks in the greysearch program.

Note that there may be a lot of weird letters and numbers in the address, this is OK, copy the whole thing

for example, the following URL was obtained by searching for "depression +pdf"

greysearch --url "https://www.google.com.au/search?sxsrf=ACYBGNTN2I-ZiNy4qYPUnn1yfmPMg3ZFFw%3A1575175967610&ei=H0fjXZruJMq9rQHTl7_IBQ&q=depression+%2Bpdf&oq=depression+%2Bpdf&gs_l=psy-ab.3...48781.57571..57803...2.3..0.259.2314.0j13j1......0....1..gws-wiz.......0i71.frhhqm73guY&ved=0ahUKEwja-Yfg05PmAhXKXisKHdPLD1kQ4dUDCAs&uact=5"


## Limiting the number of results

By default, the program will search for 100 results (this is also the maximum amount possible)

If you want to limit the number of searches you can include --results #number when calling the program

For example, if you want only 20 results you can do

greysearch --url "searchurl" --results 20

## What the program produces

When you run the greysearch program a number of pdf files will be downloaded and some text files will be produced.

A directory will be created with the form  YYYYMMDD_HHMMSS where YYYY stands for year, MM for month etc.

This is to ensure that successive calls of the program do not overwrite the results and you always know when the program was run.

Inside the dated folder you should see the following files

* google-search-term.txt
* google-search-result.html
* results_summary.txt
* and a number of directories corresponding to your search results starting at 000

### google-search-term.txt
This is a copy of the search url you used to create the search.

### google-search-result.html
This is a copy of the html response google provided to your search url. You can actually open this with your browser to see the page rendered as it would have looked like at the time*.

*please note that this is an offline copy of the the html saved at the time you did the search. Any links that exist on the page may have changed between the time you made the search and when you click on them. For example if the google search you made had a link to "my awesome myspace page" and 10 years later to click the link, "my awesome myspace page" may not actually exist anymore.

### results_summary.txt
This is a text file that contains the search result number and the link to the pdf or webpage corresponding to the search result.


### search directories

Each search result will get its own directory (starting at 000)

Inside the directory will be either

* a pdf file that was downloaded
* a text file

In cases where the search result referenced a website instead of a pdf file, a text file called website_link.txt will be placed in the folder and the contents of the txt file will be a url to the site in question.

Occasionally the program will fail to download a pdf file for one reason or another. This can happen for a number of reasons including a slow internet connection  / big pdf file or an issue with ssl certificates or something else.

When the program fails to download the pdf it will instead create a text file called filename.failed.txt
This should hopefully be a rare occurrence, but if it happens it is intended that the user navigates to this directory, opens the txt file and retrieves the link from the filename.failed.txt and manually downloads the file themselves.



## Authors

* **Simon Caine**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* thanks to **Billie Thompson** - for a nice readme template - [PurpleBooth](https://github.com/PurpleBooth/a-good-readme-template)
