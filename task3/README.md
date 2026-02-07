The script downloads information about universities for multiple countries using a public API.

Data fetching for each country is done in a separate thread to speed up the process.

After all threads finish, the results are printed to the console.
Universities are grouped by country and displayed as a numbered list.

For each country, up to 20 university names are shown.
