from xml.dom.minidom import parse, parseString

dom1 = parse('mydata.xml')  # parse an XML file by name

datasource = open('mydata.xml')
dom2 = parse(datasource)  # parse an open file

dom3 = parseString('<myxml>Some data<empty/> some more data</myxml>')