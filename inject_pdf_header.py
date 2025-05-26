from PyPDF2 import PdfReader, PdfWriter
import sys
reader = PdfReader(sys.argv[1])
writer = PdfWriter()
for page in reader.pages:
    writer.add_page(page)
writer.add_metadata({
    "/CertNode-ICS": "ICS-2025-0001",
    "/Certified-By": "certnode.io",
    "/Certification-Date": "2025-05-30"
})
with open("certified_output.pdf", "wb") as f: writer.write(f)
print("Certified PDF generated with trust metadata.")
