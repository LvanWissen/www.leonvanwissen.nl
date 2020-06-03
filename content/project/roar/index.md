---
title: roar
subtitle: Reconstructions and Observations in Archival Resources
summary: Ontology to describe Reconstructions and Observations in Archival Resources
tags:
- roar
- Linked Data
- rdf
- ontology
- archives
date: "2019-06-24"

# Optional external URL for project (replaces project detail page).
external_link: "https://w3id.org/roar"

image:
  caption: roar
  focal_point: Smart

links:
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
slides: example
---

*Voor een Nederlandse beschrijving, zie de website van Menno den Engelse: http://www.islandsofmeaning.nl/roar/*

Most modern archivists will tell you they create indexes (with the help of volunteers), not identifications. Which makes sense. But often researchers, genealogists, and sometimes even archivists want to reconstruct lives, locations or other entities from the available sources. The roar ontology was designed to fascilitate this. 

The roar vocabulairy will let you describe the people and places you find in a specific document [=source]. Each person and place mentioned in the source is something what we call is an 'Observation', which can be used as a piece of the puzzle later on. The Observation holds the information that is described about the entity (e.g. Person, Location) in the source. You're encouraged to use existing vocabularies (`bio`, `schema`, `sem`) to describe these statements. The example below shows the modelling of a PersonObservation. 

```
@prefix saa: <https://data.create.humanities.uva.nl/datasets/bevolkingsregisters/> .
@prefix br: <https://data.create.humanities.uva.nl/datasets/bevolkingsregisters/ontology/> .
@prefix bri: <https://data.create.humanities.uva.nl/datasets/bevolkingsregisters/Index/> .
@prefix brl: <https://data.create.humanities.uva.nl/datasets/bevolkingsregisters/Location/> .
@prefix brp: <https://data.create.humanities.uva.nl/datasets/bevolkingsregisters/Person/> .
@prefix bro: <https://data.create.humanities.uva.nl/datasets/bevolkingsregisters/Occupation/> .

brp:saaId22154618 a roar:PersonObservation ;
    rdfs:label "Jacob van Lennep" ;
    bio:birth [ a bio:Birth, sem:Event ;
            rdfs:label "Geboorte van Jacob van Lennep"@nl ;
            bio:place brl:be473917-5165-58d4-8706-ae9f683c1606 ;  # Amsterdam
            bio:principal brp:saaId22154618 ;
            sem:hasActor [ a sem:Role ;
                    rdfs:label "Jacob van Lennep" ;
                    sem:roleType br:Role/a1afdfc3-c2b8-5a29-b837-f41e948db9bc> ;
                    rdf:value brp:saaId22154618 ] ;
            sem:hasTimeStamp "1802-03-24"^^xsd:datetime ] ;
    schema:birthDate "1802-03-24"^^xsd:datetime ;
    schema:birthPlace brl:be473917-5165-58d4-8706-ae9f683c1606 ; # Amsterdam
    schema:hasOccupation bro:874babe7-6931-513a-aa64-5e5accaa211c ;  # Rijksadvocaat
    schema:homeLocation brl:75d03fc0-f64e-54f1-9da3-546b0c851868 ; # Keizersgracht 712
    pnv:hasName [ a pnv:PersonName ;
            rdfs:label "Jacob van Lennep" ;
            pnv:baseSurname "Lennep" ;
            pnv:givenName "Jacob" ;
            pnv:literalName "Jacob van Lennep" ;
            pnv:surnamePrefix "van" ] ;
    roar:documentedIn bri:saaId22154618 ;
    roar:hasLocation [ rdfs:label "Amsterdam" ;
            sem:hasTimeStamp "1802-03-24"^^xsd:datetime ;
            rdf:value brl:be473917-5165-58d4-8706-ae9f683c1606 ;  # Amsterdam
            roar:role "birthplace" ],
        [ rdfs:label "Keizersgracht 712" ;
            sem:hasEarliestBeginTimeStamp "1851-01-01"^^xsd:datetime ;
            sem:hasEarliestEndTimeStamp "1851-01-01"^^xsd:datetime ;
            sem:hasLatestBeginTimeStamp "1853-12-31"^^xsd:datetime ;
            sem:hasLatestEndTimeStamp "1853-12-31"^^xsd:datetime ;
            rdf:value brl:75d03fc0-f64e-54f1-9da3-546b0c851868 ;  # Keizersgracht 712
            roar:role "home location" ] ;
    void:inDataset saa:saa_index_op_bevolkingsregister_1851-1853_20181004 .
```

The list of Observations in the sources immediately serves as an index to the collection. In this step, any disambiguation is not yet done, which means that the same person can be mentioned and expressed multiple times in the sources and thus in multiple Observations. For this, roar lets you describe 'Reconstructions' that put the puzzle together. A PersonReconstruction can be derived from Observations in a birth certificate, a notary deed, a newspaper article, a diary or a photograph. A reconstruction always links to all Observations that have lead to the modelling of a single Reconstruction by specifing a `prov:wasDerivedFrom` statement. 

Reconstructions can be made manually, but also in an automated process. When using algorithms, changing parameters could even result in multiple reconstructions for different purposes, or with varying probabilities of the same person or location. With the `prov` ontology you may annotate who made what Reconstruction when, and which software or parameters where used in doing so.

The vocabulary is described and published at https://w3id.org/roar. Feel free to send in remarks, contributions or other comments! 

{{< figure src="roar-graph.png" title="Figure 1 - roar overview" lightbox="false">}}

