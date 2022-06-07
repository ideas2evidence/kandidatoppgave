

library(XML)
library(tidyverse)

xmlfile <- xmlParse("resources/p828932869599.xml", encoding="UTF-8")

nodes <- getNodeSet(xmlfile, "//Single | //Multi | //Open | //Grid")

# Spørsmål
map_chr(nodes, function(x) xmlValue(getNodeSet(x, "Name")))
map_chr(nodes, xmlName)
map_chr(nodes, function(x) xmlAttrs(x)["VariableType"]) # NA = "Normal" (Ordinære spørsmål)
map_chr(nodes, function(x) xmlValue(getNodeSet(x, "FormTexts/FormText/Text")[1]))

# Svaralternativer
answerpath <- ".//SingleAnswers/Answer | .//MultiAnswers/Answer | .//Grid3DAnswers/Answer | .//GridAnswers/GridAnswer"

map(nodes,
    function(x) {
      tibble(
        value = map_chr(getNodeSet(x, answerpath), function(y) xmlAttrs(y)["Precode"]),
        label = as.character(xmlValue(getNodeSet(x, answerpath)))
        )
      }
    )