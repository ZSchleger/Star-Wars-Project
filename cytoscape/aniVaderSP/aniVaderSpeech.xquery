let $starWarsColl := collection('verbTaggedClean-xml/?select=*.xml')
for $sp in $starWarsColl//sp[speaker[contains(lower-case(.), "anakin") or contains(lower-case(.), "vader")]]
let $mTitle := $sp ! base-uri() ! tokenize(., '/')[last()] ! substring-before(., '.xml')
where $sp/verb
let $speaker := $sp//speaker/string()
let $distinctVerbs := $sp//verb[not(. = preceding::verb)]
for $verb in $distinctVerbs
 for $s in $speaker 
return concat($speaker, "  ", $verb, "  ", $mTitle, "&#xA;")