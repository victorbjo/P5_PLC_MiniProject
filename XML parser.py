import xml.sax
import numpy as np
matrix = []
class MatrixHandler( xml.sax.ContentHandler ):
    count = 0
    def __init__(self):
        self.CurrentData = ""
        self.row = ""
        self.entry = ""

   # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "matrix":
            title = attributes["title"]
            print(title);
        if tag == "row":
            matrix.append([])

   # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "entry":
            matrix[self.count].append(int(self.entry))
        elif tag == "row":
            self.count += 1
        self.CurrentData = ""
      
   # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "row":
            self.row = content
        elif self.CurrentData == "entry":
            self.entry = content
class HomogeneousTransform():
    def __init__(self, matrix):
        self.matrix = matrix
    def prettyPrint(self):
        print()
        for x in range (len(self.matrix)):
            print("   ".join([str(lst) for lst in self.matrix[x]]))
            print()
    def transpose(self):
        x = np.array(self.matrix)
        x = np.transpose(x)
        return x
    
if ( __name__ == "__main__"):
   
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = MatrixHandler()
    parser.setContentHandler( Handler )

    parser.parse("test.xml")
    Matrix = HomogeneousTransform(matrix)
    Matrix.prettyPrint()
    Matrix.transpose()
