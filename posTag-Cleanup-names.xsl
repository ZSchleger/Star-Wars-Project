<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    exclude-result-prefixes="xs math"
    version="3.0">
    
<xsl:variable name="nameTagged" as="document-node()+" select="collection('nameTagged-xml')"/>
    
<xsl:mode on-no-match="shallow-copy"/>
    
    <xsl:template match="/">
        
     <xsl:for-each select="$nameTagged">
         <xsl:variable name="filename" as="xs:string" select="current() ! base-uri() ! tokenize(., '/')[last()]"/>
         <xsl:result-document method="xml" indent="yes" href="nameTaggedClean-xml/{$filename}">
             
            <xsl:apply-templates/>
             
         </xsl:result-document>
         
         
     </xsl:for-each>
        
     
    </xsl:template>
    
    <xsl:template match="name[name]">
        
        <name type="{@type}">
            <xsl:sequence select="string()"/>
        </name>
        
    </xsl:template>
    
</xsl:stylesheet>