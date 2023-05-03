let $starWarsColl := collection('verbTaggedClean-xml/?select=*.xml')
let $sd := $starWarsColl//sd
let $anakinSD := $sd[contains(lower-case(.), "anakin") and contains(lower-case(.), "lightsaber")]
let $vaderSD := $sd[contains(lower-case(.), "vader") and contains(lower-case(.), "lightsaber")]
let $aniVaderSD := ($anakinSD, $vaderSD)
for $a in $aniVaderSD
let $mTitle := $a ! base-uri() ! tokenize(., '/')[last()] ! substring-before(., '.xml')
let $verbs := $a//verb/text() ! normalize-space() ! lower-case(.)
return 
  <result>
    <mTitle>{ $mTitle }</mTitle>
    <verbs>{ $verbs }</verbs>
  </result>