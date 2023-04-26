<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    exclude-result-prefixes="xs math"
    version="3.0">
    
<xsl:variable name="verbTagged" as="document-node()+" select="collection('verbTagged-xml')"/>    
    
<xsl:mode on-no-match="shallow-copy"/>
    
    <xsl:template match="/">
        
     <xsl:for-each select="$verbTagged">
         <xsl:variable name="filename" as="xs:string" select="current() ! base-uri() ! tokenize(., '/')[last()]"/>
         <xsl:result-document method="xml" indent="yes" href="{$filename}">
             
            <xsl:apply-templates/>
             
         </xsl:result-document>
         
         
     </xsl:for-each>
        
     
    </xsl:template>
    
    <xsl:template match="verb[verb]">
        
        <verb lemma="{@lemma}">
            <xsl:sequence select="string()"/>
        </verb>
        
    </xsl:template>
    
</xsl:stylesheet>