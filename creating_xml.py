#!/usr/bin/env python
import lxml.etree as ET   # or import xml.etree.ElementTree as ET
import csv

root = ET.Element('presidents')


with open('DATA/presidents.csv') as pres_in:
    rdr = csv.reader(pres_in)
    for tm, fn, ln, bp, bs, py in rdr:
        p = ET.SubElement(root, 'president', term=tm)
        ET.SubElement(p, 'firstname').text = fn
        ET.SubElement(p, 'lastname').text = ln
        ET.SubElement(p, 'birthplace').text = bp
        ET.SubElement(p, 'birthstate').text = bs
        ET.SubElement(p, 'party').text = py

print(ET.tostring(root, pretty_print=True).decode())

doc = ET.ElementTree(root)
doc.write('potus.xml', pretty_print=True, xml_declaration=True)


tr = doc.find('.//president[@term="26"]')
print(tr.find('firstname').text)
print(tr.find('lastname').text)

