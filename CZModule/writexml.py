# -*- coding: utf8 -*-

from xml.dom.minidom import Document


class writexml(object):

    def __init__(self):
        self.doc=Document()

    def appendnode(self,fathernode,childnode):

        fathernode.append(childnode)

    def create_node(self,tag="",attribute_name=None,attribute_value=None,nodetext=None):

        if (attribute_name is None or attribute_value is None) and nodetext is None:
            node=self.doc.createElement(tagName=tag)
            return node

        elif (not attribute_name is None and not attribute_value is None) and nodetext is None:
             node=self.doc.createElement(tagName=tag)
             node.setAttribute(attribute_name,attribute_value)
             return node

        elif not attribute_name is None and not attribute_value is None and not nodetext is None:
             node=self.doc.createElement(tagName=tag)
             node.setAttribute(attribute_name, attribute_value)
             node_text=self.doc.createTextNode(nodetext)
             node.appendChild(node_text)

             return node

        elif (attribute_name is None or attribute_value is None) and not nodetext is None:
              node = self.doc.createElement(tagName=tag)
              node_text = self.doc.createTextNode(nodetext)
              node.appendChild(node_text)

              return  node
        else:
               return

    def savexml(self,xmlf=""):

        with open(xmlf,'w') as xmlf:
             self.doc.writexml(xmlf, addindent=' ', encoding='utf-8', newl="\n")



