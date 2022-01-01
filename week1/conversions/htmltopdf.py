import pdfkit

# INSTALL wkhtmltopdf AND SET PATH IN CONFIGURATION
# These two Steps could be eliminated By Installing wkhtmltopdf -
# - and setting it's path to Environment Variables
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# CONVERT HTML FILE TO PDF WITH PDFKIT
pdfkit.from_file('museum.html', 'museum.pdf', configuration=config,
                 options={'page-height': '2500', 'page-width': '1270', 'encoding': "UTF-8"})
